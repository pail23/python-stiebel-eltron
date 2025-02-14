"""Modbus api for stiebel eltron heat pumps. This file is generated. Do not modify it manually."""
from . import ModbusRegister, ModbusRegisterBlock, StiebelEltronAPI, IsgRegisters


class WpmSystemValuesRegisters(IsgRegisters):

    ACTUAL_TEMPERATURE_FE7 = 501
    SET_TEMPERATURE_FE7 = 502
    ACTUAL_TEMPERATURE_FEK = 503
    SET_TEMPERATURE_FEK = 504
    RELATIVE_HUMIDITY = 505
    DEW_POINT_TEMPERATURE = 506
    OUTSIDE_TEMPERATURE = 507
    ACTUAL_TEMPERATURE_HK_1 = 508
    SET_TEMPERATURE_HK_1_WPM3I = 509
    SET_TEMPERATURE_HK_1 = 510
    ACTUAL_TEMPERATURE_HK_2 = 511
    SET_TEMPERATURE_HK_2 = 512
    ACTUAL_FLOW_TEMPERATURE_WP = 513
    ACTUAL_FLOW_TEMPERATURE_NHZ = 514
    ACTUAL_FLOW_TEMPERATURE = 515
    ACTUAL_RETURN_TEMPERATURE = 516
    SET_FIXED_TEMPERATURE = 517
    ACTUAL_BUFFER_TEMPERATURE = 518
    SET_BUFFER_TEMPERATURE = 519
    HEATING_PRESSURE = 520
    FLOW_RATE = 521
    ACTUAL_TEMPERATURE_DHW = 522
    SET_TEMPERATURE_DHW = 523
    ACTUAL_TEMPERATURE_FAN = 524
    SET_TEMPERATURE_FAN = 525
    ACTUAL_TEMPERATURE_AREA = 526
    SET_TEMPERATURE_AREA = 527
    COLLECTOR_TEMPERATURE = 528
    CYLINDER_TEMPERATURE = 529
    RUNTIME = 530
    ACTUAL_TEMPERATURE_EXTERNAL = 531
    SET_TEMPERATURE_EXTERNAL = 532

class WpmEnergySystemInformationRegisters(IsgRegisters):

    SG_READY_OPERATING_STATE = 5001
    CONTROLLER_IDENTIFICATION = 5002





WPM_SYSTEM_VALUES_REGISTERS = {

    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FE7: ModbusRegister(address=501, name="ACTUAL TEMPERATURE FE7", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FE7),
    WpmSystemValuesRegisters.SET_TEMPERATURE_FE7: ModbusRegister(address=502, name="SET TEMPERATURE FE7", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_FE7),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FEK: ModbusRegister(address=503, name="ACTUAL TEMPERATURE FEK", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FEK),
    WpmSystemValuesRegisters.SET_TEMPERATURE_FEK: ModbusRegister(address=504, name="SET TEMPERATURE FEK", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_FEK),
    WpmSystemValuesRegisters.RELATIVE_HUMIDITY: ModbusRegister(address=505, name="RELATIVE HUMIDITY", unit="%", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.RELATIVE_HUMIDITY),
    WpmSystemValuesRegisters.DEW_POINT_TEMPERATURE: ModbusRegister(address=506, name="DEW POINT TEMPERATURE", unit="°C", min=-40.0, max=30.0, data_type=2, key=WpmSystemValuesRegisters.DEW_POINT_TEMPERATURE),
    WpmSystemValuesRegisters.OUTSIDE_TEMPERATURE: ModbusRegister(address=507, name="OUTSIDE TEMPERATURE", unit="°C", min=-60.0, max=80.0, data_type=2, key=WpmSystemValuesRegisters.OUTSIDE_TEMPERATURE),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_1: ModbusRegister(address=508, name="ACTUAL TEMPERATURE HK 1", unit="°C", min=0.0, max=40.0, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_1),
    WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1_WPM3I: ModbusRegister(address=509, name="SET TEMPERATURE HK 1 WPM3I", unit="°C", min=0.0, max=65.0, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1_WPM3I),
    WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1: ModbusRegister(address=510, name="SET TEMPERATURE HK 1", unit="°C", min=0.0, max=40.0, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_2: ModbusRegister(address=511, name="ACTUAL TEMPERATURE HK 2", unit="°C", min=0.0, max=90.0, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_2),
    WpmSystemValuesRegisters.SET_TEMPERATURE_HK_2: ModbusRegister(address=512, name="SET TEMPERATURE HK 2", unit="°C", min=0.0, max=65.0, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_HK_2),
    WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_WP: ModbusRegister(address=513, name="ACTUAL FLOW TEMPERATURE WP", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_WP),
    WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_NHZ: ModbusRegister(address=514, name="ACTUAL FLOW TEMPERATURE NHZ", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_NHZ),
    WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE: ModbusRegister(address=515, name="ACTUAL FLOW TEMPERATURE", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE),
    WpmSystemValuesRegisters.ACTUAL_RETURN_TEMPERATURE: ModbusRegister(address=516, name="ACTUAL RETURN TEMPERATURE", unit="°C", min=0.0, max=90.0, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_RETURN_TEMPERATURE),
    WpmSystemValuesRegisters.SET_FIXED_TEMPERATURE: ModbusRegister(address=517, name="SET FIXED TEMPERATURE", unit="°C", min=20.0, max=50.0, data_type=2, key=WpmSystemValuesRegisters.SET_FIXED_TEMPERATURE),
    WpmSystemValuesRegisters.ACTUAL_BUFFER_TEMPERATURE: ModbusRegister(address=518, name="ACTUAL BUFFER TEMPERATURE", unit="°C", min=0.0, max=90.0, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_BUFFER_TEMPERATURE),
    WpmSystemValuesRegisters.SET_BUFFER_TEMPERATURE: ModbusRegister(address=519, name="SET BUFFER TEMPERATURE", unit="°C", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.SET_BUFFER_TEMPERATURE),
    WpmSystemValuesRegisters.HEATING_PRESSURE: ModbusRegister(address=520, name="HEATING PRESSURE", unit="bar", min=None, max=None, data_type=7, key=WpmSystemValuesRegisters.HEATING_PRESSURE),
    WpmSystemValuesRegisters.FLOW_RATE: ModbusRegister(address=521, name="FLOW RATE", unit="l/min", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.FLOW_RATE),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_DHW: ModbusRegister(address=522, name="ACTUAL TEMPERATURE DHW", unit="°C", min=10.0, max=65.0, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_DHW),
    WpmSystemValuesRegisters.SET_TEMPERATURE_DHW: ModbusRegister(address=523, name="SET TEMPERATURE DHW", unit="°C", min=10.0, max=65.0, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_DHW),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FAN: ModbusRegister(address=524, name="ACTUAL TEMPERATURE FAN", unit="K", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FAN),
    WpmSystemValuesRegisters.SET_TEMPERATURE_FAN: ModbusRegister(address=525, name="SET TEMPERATURE FAN", unit="K", min=7.0, max=25.0, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_FAN),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_AREA: ModbusRegister(address=526, name="ACTUAL TEMPERATURE AREA", unit="K", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_AREA),
    WpmSystemValuesRegisters.SET_TEMPERATURE_AREA: ModbusRegister(address=527, name="SET TEMPERATURE AREA", unit="K", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_AREA),
    WpmSystemValuesRegisters.COLLECTOR_TEMPERATURE: ModbusRegister(address=528, name="COLLECTOR TEMPERATURE", unit="°C", min=0.0, max=90.0, data_type=2, key=WpmSystemValuesRegisters.COLLECTOR_TEMPERATURE),
    WpmSystemValuesRegisters.CYLINDER_TEMPERATURE: ModbusRegister(address=529, name="CYLINDER TEMPERATURE", unit="°C", min=0.0, max=90.0, data_type=2, key=WpmSystemValuesRegisters.CYLINDER_TEMPERATURE),
    WpmSystemValuesRegisters.RUNTIME: ModbusRegister(address=530, name="RUNTIME", unit="h", min=None, max=None, data_type=6, key=WpmSystemValuesRegisters.RUNTIME),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_EXTERNAL: ModbusRegister(address=531, name="ACTUAL TEMPERATURE EXTERNAL", unit="°C", min=10.0, max=90.0, data_type=2, key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_EXTERNAL),
    WpmSystemValuesRegisters.SET_TEMPERATURE_EXTERNAL: ModbusRegister(address=532, name="SET TEMPERATURE EXTERNAL", unit="K", min=None, max=None, data_type=2, key=WpmSystemValuesRegisters.SET_TEMPERATURE_EXTERNAL),
}

WPM_ENERGY_SYSTEM_INFORMATION_REGISTERS = {

    WpmEnergySystemInformationRegisters.SG_READY_OPERATING_STATE: ModbusRegister(address=5001, name="SG READY OPERATING STATE", unit="", min=1.0, max=4.0, data_type=6, key=WpmEnergySystemInformationRegisters.SG_READY_OPERATING_STATE),
    WpmEnergySystemInformationRegisters.CONTROLLER_IDENTIFICATION: ModbusRegister(address=5002, name="CONTROLLER IDENTIFICATION", unit="", min=None, max=None, data_type=6, key=WpmEnergySystemInformationRegisters.CONTROLLER_IDENTIFICATION),
}



class WpmStiebelEltronAPI(StiebelEltronAPI):

    def __init__(self, host: str, port: int = 502, slave: int = 1) -> None:
        super().__init__([
            
                ModbusRegisterBlock(base_address=500, count=32, name="System Values", registers=WPM_SYSTEM_VALUES_REGISTERS),
                ModbusRegisterBlock(base_address=5000, count=2, name="Energy System Information", registers=WPM_ENERGY_SYSTEM_INFORMATION_REGISTERS),
            ],
            host, port, slave)