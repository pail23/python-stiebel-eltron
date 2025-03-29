import asyncio
import logging

from enum import Enum

from dataclasses import dataclass
from pymodbus.client import AsyncModbusTcpClient

_LOGGER: logging.Logger = logging.getLogger(__package__)


ENERGY_DATA_BLOCK_NAME = "Energy Data"


class IsgRegisters(Enum):
    """ISG Register base class."""


@dataclass
class ModbusRegister:
    """Register data class."""

    address: int
    name: str
    unit: str
    min: float | None
    max: float | None
    data_type: int
    key: IsgRegisters

    @property
    def is_virtual_register(self) -> bool:
        """Registers with an address above"""


class RegisterType(Enum):
    """Register type enum."""

    INPUT_REGISTER = 1
    HOLDING_REGISTER = 2


@dataclass
class ModbusRegisterBlock:
    """Register block data class."""

    base_address: int
    count: int
    name: str
    registers: dict
    register_type: RegisterType


def get_register_descriptor(descriptors: list[ModbusRegister], address: int) -> ModbusRegister | None:
    """Find the descriptor with a given address."""
    for descriptor in descriptors:
        if descriptor.address == address:
            return descriptor
    return None


class StiebelEltronAPI:
    """Stiebel Eltron API."""

    def __init__(
        self,
        register_blocks: list[ModbusRegisterBlock],
        host: str,
        port: int = 502,
        slave: int = 1,
    ) -> None:
        """Initialize Stiebel Eltron communication."""
        self._slave = slave
        self._lock = asyncio.Lock()
        self._host = host
        self._client: AsyncModbusTcpClient = AsyncModbusTcpClient(host=host, port=port)
        self._register_blocks = register_blocks
        self._data = {}

    async def close(self) -> None:
        """Disconnect client."""
        _LOGGER.debug("Closing connection to %s", self._host)
        async with self._lock:
            self._client.close()

    async def connect(self) -> None:
        """Connect client."""
        _LOGGER.debug("Connecting to %s", self._host)
        async with self._lock:
            await self._client.connect()

    @property
    def is_connected(self) -> bool:
        """Check modbus client connection status."""
        if self._client is None:
            return False
        return self._client.connected

    @property
    def host(self) -> str:
        """Return the host address of the Stiebel Eltron ISG."""
        return self._host

    def get_register_descriptor(self, register: IsgRegisters) -> ModbusRegister | None:
        """Get the descriptor of a register."""
        for registerblock in self._register_blocks:
            descriptor = get_register_descriptor(
                list(registerblock.registers.values()),
                register.value,
            )
            if descriptor is not None:
                return descriptor
        return None

    def get_register_value(self, register: IsgRegisters) -> float:
        """Get a value form the registers. The async_udpate needs to be called first."""
        return self._data[register]

    async def write_register_value(self, register: IsgRegisters, value: int | float) -> None:
        """Writes a modbus register."""
        descriptor = self.get_register_descriptor(register)
        if descriptor is not None:
            await self._client.write_register(descriptor.address - 1, value=self.convert_value_to_modbus(value, descriptor), slave=1)
        else:
            raise ValueError("invalid register")

    async def read_input_registers(self, slave, address, count):
        """Read input registers."""
        _LOGGER.debug(f"Reading {count} input registers from {address} with slave {slave}")
        async with self._lock:
            return await self._client.read_input_registers(address, count=count, slave=slave)

    async def read_holding_registers(self, slave, address, count):
        """Read holding registers."""
        _LOGGER.debug(f"Reading {count} holding registers from {address} with slave {slave}")
        async with self._lock:
            return await self._client.read_holding_registers(address, count=count, slave=slave)

    def convert_value_from_modbus(self, register, register_description: ModbusRegister) -> float | int | None:
        """Convert a modbus value to a python value."""
        if register_description.data_type == 2:
            value = self._client.convert_from_registers([register], self._client.DATATYPE.INT16)
            if value == -32768:
                return None
            return float(value) * 0.1
        elif register_description.data_type == 6:
            value = self._client.convert_from_registers([register], self._client.DATATYPE.UINT16)
            if value == 32768:
                return None
            return value
        elif register_description.data_type == 7:
            value = self._client.convert_from_registers([register], self._client.DATATYPE.INT16)
            if value == -32768:
                return None
            return value * 0.01
        elif register_description.data_type == 8:
            value = self._client.convert_from_registers([register], self._client.DATATYPE.UINT16)
            if value == 32768:
                return None
            return value

    def convert_value_to_modbus(self, value: int | float, register_description: ModbusRegister) -> int:
        """Convert a modbus value to a python value."""
        if register_description.data_type == 2:
            register = self._client.convert_to_registers([int(value * 10)], self._client.DATATYPE.INT16)
            return register[0]
        elif register_description.data_type == 6:
            register = self._client.convert_to_registers([int(value)], self._client.DATATYPE.UINT16)
            return register[0]
        elif register_description.data_type == 7:
            register = self._client.convert_to_registers([int(value * 100)], self._client.DATATYPE.INT16)
            return register[0]
        elif register_description.data_type == 8:
            register = self._client.convert_to_registers([int(value)], self._client.DATATYPE.UINT16)
            return register[0]
        else:
            raise ValueError("invalid register type")

    async def async_update(self):
        """Request current values from heat pump."""
        result: dict = {}
        for registerblock in self._register_blocks:
            heat_pump_data = None
            if registerblock.register_type == RegisterType.INPUT_REGISTER:
                heat_pump_data = await self.read_input_registers(
                    slave=self._slave,
                    address=registerblock.base_address,
                    count=registerblock.count,
                )
            elif registerblock.register_type == RegisterType.HOLDING_REGISTER:
                heat_pump_data = await self.read_holding_registers(
                    slave=self._slave,
                    address=registerblock.base_address,
                    count=registerblock.count,
                )

            if heat_pump_data is not None and not heat_pump_data.isError():
                for i in range(0, registerblock.count):
                    descriptor = get_register_descriptor(
                        list(registerblock.registers.values()),
                        i + registerblock.base_address + 1,
                    )
                    if descriptor is not None:
                        result[descriptor.key] = self.convert_value_from_modbus(heat_pump_data.registers[i], descriptor)

        self._data = result
