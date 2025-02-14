"""Modbus api for stiebel eltron heat pumps. This file is generated. Do not modify it manually."""

from . import ModbusRegister, ModbusRegisterBlock, StiebelEltronAPI, IsgRegisters


class LwzSystemValuesRegisters(IsgRegisters):
    ACTUAL_ROOM_T_HC1 = 1
    SET_ROOM_TEMPERATURE_HC1 = 2


LWZ_SYSTEM_VALUES_REGISTERS = {
    LwzSystemValuesRegisters.ACTUAL_ROOM_T_HC1: ModbusRegister(
        address=1,
        name="ACTUAL ROOM T HC1",
        unit="°C",
        min=-20.0,
        max=60.0,
        data_type=2,
        key=LwzSystemValuesRegisters.ACTUAL_ROOM_T_HC1,
    ),
    LwzSystemValuesRegisters.SET_ROOM_TEMPERATURE_HC1: ModbusRegister(
        address=2,
        name="SET ROOM TEMPERATURE HC1",
        unit="°C",
        min=-20.0,
        max=60.0,
        data_type=2,
        key=LwzSystemValuesRegisters.SET_ROOM_TEMPERATURE_HC1,
    ),
}


class LwzStiebelEltronAPI(StiebelEltronAPI):
    def __init__(self, host: str, port: int = 502, slave: int = 1) -> None:
        super().__init__(
            [
                ModbusRegisterBlock(
                    base_address=0,
                    count=2,
                    name="System Values",
                    registers=LWZ_SYSTEM_VALUES_REGISTERS,
                ),
            ],
            host,
            port,
            slave,
        )
