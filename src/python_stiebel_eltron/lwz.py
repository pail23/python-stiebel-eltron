"""Modbus api for stiebel eltron heat pumps. This file is generated. Do not modify it manually."""

from . import (
    ModbusRegister,
    ModbusRegisterBlock,
    StiebelEltronAPI,
    IsgRegisters,
    RegisterType,
)


class LwzSystemValuesRegisters(IsgRegisters):
    ACTUAL_ROOM_T_HC1 = 1
    SET_ROOM_TEMPERATURE_HC1 = 2
    RELATIVE_HUMIDITY_HC1 = 3
    ACTUAL_ROOM_T_HC2 = 4
    SET_ROOM_TEMPERATURE_HC2 = 5
    RELATIVE_HUMIDITY_HC2 = 6
    OUTSIDE_TEMPERATURE = 7
    ACTUAL_VALUE_HC1 = 8
    SET_VALUE_HC1 = 9
    ACTUAL_VALUE_HC2 = 10
    SET_VALUE_HC2 = 11
    FLOW_TEMPERATURE = 12
    RETURN_TEMPERATURE = 13
    PRESSURE_HTG_CIRC = 14
    FLOW_RATE_ = 15
    ACTUAL_DHW_T = 16
    DHW_SET_TEMPERATURE = 17
    VENTILATION_AIR_ACTUAL_FAN_SPEED = 18
    VENTILATION_AIR_SET_FLOW_RATE = 19
    EXTRACT_AIR_ACTUAL_FAN_SPEED = 20
    EXTRACT_AIR_SET_FLOW_RATE = 21
    EXTRACT_AIR_HUMIDITY = 22
    EXTRACT_AIR_TEMP = 23
    EXTRACT_AIR_DEW_POINT = 24
    DEW_POINT_TEMP_HC1 = 25
    DEW_POINT_TEMP_HC2 = 26
    COLLECTOR_TEMPERATURE = 27
    HOT_GAS_TEMPERATURE = 28
    HIGH_PRESSURE = 29
    LOW_PRESSURE = 30
    COMPRESSOR_STARTS = 31
    COMPRESSOR_SPEED = 32
    MIXED_WATER_AMOUNT = 33


class LwzSystemParametersRegisters(IsgRegisters):
    OPERATING_MODE = 1001
    ROOM_TEMPERATURE_DAY_HK1 = 1002
    ROOM_TEMPERATURE_NIGHT_HK1 = 1003
    MANUAL_HC_SET_HK1 = 1004
    ROOM_TEMPERATURE_DAY_HK2 = 1005
    ROOM_TEMPERATURE_NIGHT_HK2 = 1006
    MANUAL_HC_SET_HK2 = 1007
    GRADIENT_HK1 = 1008
    LOW_END_HK1 = 1009
    GRADIENT_HK2 = 1010
    LOW_END_HK2 = 1011
    DHW_SET_DAY = 1012
    DHW_SET_NIGHT = 1013
    DHW_SET_MANUAL = 1014
    MWM_SET_DAY = 1015
    MWM_SET_NIGHT = 1016
    MWM_SET_MANUAL = 1017
    DAY_STAGE = 1018
    NIGHT_STAGE = 1019
    PARTY_STAGE = 1020
    MANUAL_STAGE = 1021
    ROOM_TEMPERATURE_DAY_HK1_COOLING = 1022
    ROOM_TEMPERATURE_NIGHT_HK1_COOLING = 1023
    ROOM_TEMPERATURE_DAY_HK2_COOLING = 1024
    ROOM_TEMPERATURE_NIGHT_HK2_COOLING = 1025
    RESET = 1026
    RESTART_ISG = 1027


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
    LwzSystemValuesRegisters.RELATIVE_HUMIDITY_HC1: ModbusRegister(
        address=3,
        name="RELATIVE HUMIDITY HC1",
        unit="%",
        min=0.0,
        max=100.0,
        data_type=2,
        key=LwzSystemValuesRegisters.RELATIVE_HUMIDITY_HC1,
    ),
    LwzSystemValuesRegisters.ACTUAL_ROOM_T_HC2: ModbusRegister(
        address=4,
        name="ACTUAL ROOM T HC2",
        unit="°C",
        min=-20.0,
        max=60.0,
        data_type=2,
        key=LwzSystemValuesRegisters.ACTUAL_ROOM_T_HC2,
    ),
    LwzSystemValuesRegisters.SET_ROOM_TEMPERATURE_HC2: ModbusRegister(
        address=5,
        name="SET ROOM TEMPERATURE HC2",
        unit="°C",
        min=-20.0,
        max=60.0,
        data_type=2,
        key=LwzSystemValuesRegisters.SET_ROOM_TEMPERATURE_HC2,
    ),
    LwzSystemValuesRegisters.RELATIVE_HUMIDITY_HC2: ModbusRegister(
        address=6,
        name="RELATIVE HUMIDITY HC2",
        unit="%",
        min=0.0,
        max=100.0,
        data_type=2,
        key=LwzSystemValuesRegisters.RELATIVE_HUMIDITY_HC2,
    ),
    LwzSystemValuesRegisters.OUTSIDE_TEMPERATURE: ModbusRegister(
        address=7,
        name="OUTSIDE TEMPERATURE",
        unit="°C",
        min=-60.0,
        max=80.0,
        data_type=2,
        key=LwzSystemValuesRegisters.OUTSIDE_TEMPERATURE,
    ),
    LwzSystemValuesRegisters.ACTUAL_VALUE_HC1: ModbusRegister(
        address=8,
        name="ACTUAL VALUE HC1",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=LwzSystemValuesRegisters.ACTUAL_VALUE_HC1,
    ),
    LwzSystemValuesRegisters.SET_VALUE_HC1: ModbusRegister(
        address=9,
        name="SET VALUE HC1",
        unit="°C",
        min=0.0,
        max=65.0,
        data_type=2,
        key=LwzSystemValuesRegisters.SET_VALUE_HC1,
    ),
    LwzSystemValuesRegisters.ACTUAL_VALUE_HC2: ModbusRegister(
        address=10,
        name="ACTUAL VALUE HC2",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=LwzSystemValuesRegisters.ACTUAL_VALUE_HC2,
    ),
    LwzSystemValuesRegisters.SET_VALUE_HC2: ModbusRegister(
        address=11,
        name="SET VALUE HC2",
        unit="°C",
        min=0.0,
        max=65.0,
        data_type=2,
        key=LwzSystemValuesRegisters.SET_VALUE_HC2,
    ),
    LwzSystemValuesRegisters.FLOW_TEMPERATURE: ModbusRegister(
        address=12,
        name="FLOW TEMPERATURE",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=LwzSystemValuesRegisters.FLOW_TEMPERATURE,
    ),
    LwzSystemValuesRegisters.RETURN_TEMPERATURE: ModbusRegister(
        address=13,
        name="RETURN TEMPERATURE",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=LwzSystemValuesRegisters.RETURN_TEMPERATURE,
    ),
    LwzSystemValuesRegisters.PRESSURE_HTG_CIRC: ModbusRegister(
        address=14,
        name="PRESSURE HTG CIRC",
        unit="bar",
        min=0.0,
        max=6.0,
        data_type=2,
        key=LwzSystemValuesRegisters.PRESSURE_HTG_CIRC,
    ),
    LwzSystemValuesRegisters.FLOW_RATE_: ModbusRegister(
        address=15,
        name="FLOW RATE ",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=LwzSystemValuesRegisters.FLOW_RATE_,
    ),
    LwzSystemValuesRegisters.ACTUAL_DHW_T: ModbusRegister(
        address=16,
        name="ACTUAL DHW T",
        unit="°C",
        min=10.0,
        max=65.0,
        data_type=2,
        key=LwzSystemValuesRegisters.ACTUAL_DHW_T,
    ),
    LwzSystemValuesRegisters.DHW_SET_TEMPERATURE: ModbusRegister(
        address=17,
        name="DHW SET TEMPERATURE",
        unit="°C",
        min=10.0,
        max=65.0,
        data_type=2,
        key=LwzSystemValuesRegisters.DHW_SET_TEMPERATURE,
    ),
    LwzSystemValuesRegisters.VENTILATION_AIR_ACTUAL_FAN_SPEED: ModbusRegister(
        address=18,
        name="VENTILATION AIR ACTUAL FAN SPEED",
        unit="Hz",
        min=0.0,
        max=100.0,
        data_type=6,
        key=LwzSystemValuesRegisters.VENTILATION_AIR_ACTUAL_FAN_SPEED,
    ),
    LwzSystemValuesRegisters.VENTILATION_AIR_SET_FLOW_RATE: ModbusRegister(
        address=19,
        name="VENTILATION AIR SET FLOW RATE",
        unit="m³/h",
        min=0.0,
        max=300.0,
        data_type=6,
        key=LwzSystemValuesRegisters.VENTILATION_AIR_SET_FLOW_RATE,
    ),
    LwzSystemValuesRegisters.EXTRACT_AIR_ACTUAL_FAN_SPEED: ModbusRegister(
        address=20,
        name="EXTRACT AIR ACTUAL FAN SPEED",
        unit="Hz",
        min=0.0,
        max=100.0,
        data_type=6,
        key=LwzSystemValuesRegisters.EXTRACT_AIR_ACTUAL_FAN_SPEED,
    ),
    LwzSystemValuesRegisters.EXTRACT_AIR_SET_FLOW_RATE: ModbusRegister(
        address=21,
        name="EXTRACT AIR SET FLOW RATE",
        unit="m³/h",
        min=0.0,
        max=300.0,
        data_type=6,
        key=LwzSystemValuesRegisters.EXTRACT_AIR_SET_FLOW_RATE,
    ),
    LwzSystemValuesRegisters.EXTRACT_AIR_HUMIDITY: ModbusRegister(
        address=22,
        name="EXTRACT AIR HUMIDITY",
        unit="%",
        min=0.0,
        max=100.0,
        data_type=6,
        key=LwzSystemValuesRegisters.EXTRACT_AIR_HUMIDITY,
    ),
    LwzSystemValuesRegisters.EXTRACT_AIR_TEMP: ModbusRegister(
        address=23,
        name="EXTRACT AIR TEMP",
        unit="°C",
        min=0.0,
        max=65535.0,
        data_type=2,
        key=LwzSystemValuesRegisters.EXTRACT_AIR_TEMP,
    ),
    LwzSystemValuesRegisters.EXTRACT_AIR_DEW_POINT: ModbusRegister(
        address=24,
        name="EXTRACT AIR DEW POINT",
        unit="°C",
        min=0.0,
        max=65535.0,
        data_type=2,
        key=LwzSystemValuesRegisters.EXTRACT_AIR_DEW_POINT,
    ),
    LwzSystemValuesRegisters.DEW_POINT_TEMP_HC1: ModbusRegister(
        address=25,
        name="DEW POINT TEMP HC1",
        unit="°C",
        min=-40.0,
        max=30.0,
        data_type=2,
        key=LwzSystemValuesRegisters.DEW_POINT_TEMP_HC1,
    ),
    LwzSystemValuesRegisters.DEW_POINT_TEMP_HC2: ModbusRegister(
        address=26,
        name="DEW POINT TEMP HC2",
        unit="°C",
        min=-40.0,
        max=30.0,
        data_type=2,
        key=LwzSystemValuesRegisters.DEW_POINT_TEMP_HC2,
    ),
    LwzSystemValuesRegisters.COLLECTOR_TEMPERATURE: ModbusRegister(
        address=27,
        name="COLLECTOR TEMPERATURE",
        unit="°C",
        min=-60.0,
        max=200.0,
        data_type=2,
        key=LwzSystemValuesRegisters.COLLECTOR_TEMPERATURE,
    ),
    LwzSystemValuesRegisters.HOT_GAS_TEMPERATURE: ModbusRegister(
        address=28,
        name="HOT GAS TEMPERATURE",
        unit="°C",
        min=0.0,
        max=140.0,
        data_type=2,
        key=LwzSystemValuesRegisters.HOT_GAS_TEMPERATURE,
    ),
    LwzSystemValuesRegisters.HIGH_PRESSURE: ModbusRegister(
        address=29,
        name="HIGH PRESSURE",
        unit="bar",
        min=0.0,
        max=50.0,
        data_type=7,
        key=LwzSystemValuesRegisters.HIGH_PRESSURE,
    ),
    LwzSystemValuesRegisters.LOW_PRESSURE: ModbusRegister(
        address=30,
        name="LOW PRESSURE",
        unit="bar",
        min=0.0,
        max=25.0,
        data_type=7,
        key=LwzSystemValuesRegisters.LOW_PRESSURE,
    ),
    LwzSystemValuesRegisters.COMPRESSOR_STARTS: ModbusRegister(
        address=31,
        name="COMPRESSOR STARTS",
        unit="",
        min=0.0,
        max=65535.0,
        data_type=6,
        key=LwzSystemValuesRegisters.COMPRESSOR_STARTS,
    ),
    LwzSystemValuesRegisters.COMPRESSOR_SPEED: ModbusRegister(
        address=32,
        name="COMPRESSOR SPEED",
        unit="Hz",
        min=0.0,
        max=240.0,
        data_type=2,
        key=LwzSystemValuesRegisters.COMPRESSOR_SPEED,
    ),
    LwzSystemValuesRegisters.MIXED_WATER_AMOUNT: ModbusRegister(
        address=33,
        name="MIXED WATER AMOUNT",
        unit="l",
        min=0.0,
        max=65535.0,
        data_type=6,
        key=LwzSystemValuesRegisters.MIXED_WATER_AMOUNT,
    ),
}

LWZ_SYSTEM_PARAMETERS_REGISTERS = {
    LwzSystemParametersRegisters.OPERATING_MODE: ModbusRegister(
        address=1001,
        name="OPERATING MODE",
        unit="",
        min=0.0,
        max=14.0,
        data_type=8,
        key=LwzSystemParametersRegisters.OPERATING_MODE,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK1: ModbusRegister(
        address=1002,
        name="ROOM TEMPERATURE DAY",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK1,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK1: ModbusRegister(
        address=1003,
        name="ROOM TEMPERATURE NIGHT",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK1,
    ),
    LwzSystemParametersRegisters.MANUAL_HC_SET_HK1: ModbusRegister(
        address=1004,
        name="MANUAL HC SET",
        unit="°C",
        min=10.0,
        max=65.0,
        data_type=2,
        key=LwzSystemParametersRegisters.MANUAL_HC_SET_HK1,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK2: ModbusRegister(
        address=1005,
        name="ROOM TEMPERATURE DAY",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK2,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK2: ModbusRegister(
        address=1006,
        name="ROOM TEMPERATURE NIGHT",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK2,
    ),
    LwzSystemParametersRegisters.MANUAL_HC_SET_HK2: ModbusRegister(
        address=1007,
        name="MANUAL HC SET",
        unit="°C",
        min=10.0,
        max=65.0,
        data_type=2,
        key=LwzSystemParametersRegisters.MANUAL_HC_SET_HK2,
    ),
    LwzSystemParametersRegisters.GRADIENT_HK1: ModbusRegister(
        address=1008,
        name="GRADIENT",
        unit="",
        min=0.0,
        max=5.0,
        data_type=7,
        key=LwzSystemParametersRegisters.GRADIENT_HK1,
    ),
    LwzSystemParametersRegisters.LOW_END_HK1: ModbusRegister(
        address=1009,
        name="LOW END",
        unit="°C",
        min=0.0,
        max=20.0,
        data_type=2,
        key=LwzSystemParametersRegisters.LOW_END_HK1,
    ),
    LwzSystemParametersRegisters.GRADIENT_HK2: ModbusRegister(
        address=1010,
        name="GRADIENT",
        unit="",
        min=0.0,
        max=5.0,
        data_type=7,
        key=LwzSystemParametersRegisters.GRADIENT_HK2,
    ),
    LwzSystemParametersRegisters.LOW_END_HK2: ModbusRegister(
        address=1011,
        name="LOW END",
        unit="°C",
        min=0.0,
        max=20.0,
        data_type=2,
        key=LwzSystemParametersRegisters.LOW_END_HK2,
    ),
    LwzSystemParametersRegisters.DHW_SET_DAY: ModbusRegister(
        address=1012,
        name="DHW SET DAY",
        unit="°C",
        min=10.0,
        max=55.0,
        data_type=2,
        key=LwzSystemParametersRegisters.DHW_SET_DAY,
    ),
    LwzSystemParametersRegisters.DHW_SET_NIGHT: ModbusRegister(
        address=1013,
        name="DHW SET NIGHT",
        unit="°C",
        min=10.0,
        max=55.0,
        data_type=2,
        key=LwzSystemParametersRegisters.DHW_SET_NIGHT,
    ),
    LwzSystemParametersRegisters.DHW_SET_MANUAL: ModbusRegister(
        address=1014,
        name="DHW SET MANUAL",
        unit="°C",
        min=10.0,
        max=65.0,
        data_type=2,
        key=LwzSystemParametersRegisters.DHW_SET_MANUAL,
    ),
    LwzSystemParametersRegisters.MWM_SET_DAY: ModbusRegister(
        address=1015,
        name="MWM SET DAY",
        unit="l",
        min=50.0,
        max=288.0,
        data_type=6,
        key=LwzSystemParametersRegisters.MWM_SET_DAY,
    ),
    LwzSystemParametersRegisters.MWM_SET_NIGHT: ModbusRegister(
        address=1016,
        name="MWM SET NIGHT",
        unit="l",
        min=50.0,
        max=288.0,
        data_type=6,
        key=LwzSystemParametersRegisters.MWM_SET_NIGHT,
    ),
    LwzSystemParametersRegisters.MWM_SET_MANUAL: ModbusRegister(
        address=1017,
        name="MWM SET MANUAL",
        unit="l",
        min=50.0,
        max=288.0,
        data_type=6,
        key=LwzSystemParametersRegisters.MWM_SET_MANUAL,
    ),
    LwzSystemParametersRegisters.DAY_STAGE: ModbusRegister(
        address=1018,
        name="DAY STAGE",
        unit="",
        min=0.0,
        max=3.0,
        data_type=6,
        key=LwzSystemParametersRegisters.DAY_STAGE,
    ),
    LwzSystemParametersRegisters.NIGHT_STAGE: ModbusRegister(
        address=1019,
        name="NIGHT STAGE",
        unit="",
        min=0.0,
        max=3.0,
        data_type=6,
        key=LwzSystemParametersRegisters.NIGHT_STAGE,
    ),
    LwzSystemParametersRegisters.PARTY_STAGE: ModbusRegister(
        address=1020,
        name="PARTY STAGE",
        unit="",
        min=0.0,
        max=3.0,
        data_type=6,
        key=LwzSystemParametersRegisters.PARTY_STAGE,
    ),
    LwzSystemParametersRegisters.MANUAL_STAGE: ModbusRegister(
        address=1021,
        name="MANUAL STAGE",
        unit="",
        min=0.0,
        max=3.0,
        data_type=6,
        key=LwzSystemParametersRegisters.MANUAL_STAGE,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK1_COOLING: ModbusRegister(
        address=1022,
        name="ROOM TEMPERATURE DAY",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK1_COOLING,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK1_COOLING: ModbusRegister(
        address=1023,
        name="ROOM TEMPERATURE NIGHT",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK1_COOLING,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK2_COOLING: ModbusRegister(
        address=1024,
        name="ROOM TEMPERATURE DAY",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_DAY_HK2_COOLING,
    ),
    LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK2_COOLING: ModbusRegister(
        address=1025,
        name="ROOM TEMPERATURE NIGHT",
        unit="°C",
        min=10.0,
        max=30.0,
        data_type=2,
        key=LwzSystemParametersRegisters.ROOM_TEMPERATURE_NIGHT_HK2_COOLING,
    ),
    LwzSystemParametersRegisters.RESET: ModbusRegister(
        address=1026,
        name="RESET",
        unit="",
        min=0.0,
        max=1.0,
        data_type=6,
        key=LwzSystemParametersRegisters.RESET,
    ),
    LwzSystemParametersRegisters.RESTART_ISG: ModbusRegister(
        address=1027,
        name="RESTART ISG",
        unit="",
        min=0.0,
        max=2.0,
        data_type=6,
        key=LwzSystemParametersRegisters.RESTART_ISG,
    ),
}


class LwzStiebelEltronAPI(StiebelEltronAPI):
    def __init__(self, host: str, port: int = 502, slave: int = 1) -> None:
        super().__init__(
            [
                ModbusRegisterBlock(
                    base_address=0,
                    count=33,
                    name="System Values",
                    registers=LWZ_SYSTEM_VALUES_REGISTERS,
                    register_type=RegisterType.INPUT_REGISTER,
                ),
                ModbusRegisterBlock(
                    base_address=1000,
                    count=27,
                    name="System Parameters",
                    registers=LWZ_SYSTEM_PARAMETERS_REGISTERS,
                    register_type=RegisterType.HOLDING_REGISTER,
                ),
            ],
            host,
            port,
            slave,
        )
