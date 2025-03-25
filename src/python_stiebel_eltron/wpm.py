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
    APPLICATION_LIMIT_HZG = 533
    APPLICATION_LIMIT_WW = 534
    RUNTIME_EHS = 535
    SOURCE_TEMPERATURE = 536
    MIN_SOURCE_TEMPERATURE = 537
    SOURCE_PRESSURE = 538
    HOT_GAS_TEMPERATURE = 539
    HIGH_PRESSURE = 540
    LOW_PRESSURE = 541
    RETURN_TEMPERATURE_HP1 = 542
    FLOW_TEMPERATURE_HP1 = 543
    HOT_GAS_TEMPERATURE_HP1 = 544
    LOW_PRESSURE_HP1 = 545
    MEAN_PRESSURE_HP1 = 546
    HIGH_PRESSURE_HP1 = 547
    WP_WATER_FLOW_RATE_HP1 = 548
    RETURN_TEMPERATURE_HP2 = 549
    FLOW_TEMPERATURE_HP2 = 550
    HOT_GAS_TEMPERATURE_HP2 = 551
    LOW_PRESSURE_HP2 = 552
    MEAN_PRESSURE_HP2 = 553
    HIGH_PRESSURE_HP2 = 554
    WP_WATER_FLOW_RATE_HP2 = 555
    RETURN_TEMPERATURE_HP3 = 556
    FLOW_TEMPERATURE_HP3 = 557
    HOT_GAS_TEMPERATURE_HP3 = 558
    LOW_PRESSURE_HP3 = 559
    MEAN_PRESSURE_HP3 = 560
    HIGH_PRESSURE_HP3 = 561
    WP_WATER_FLOW_RATE_HP3 = 562
    RETURN_TEMPERATURE_HP4 = 563
    FLOW_TEMPERATURE_HP4 = 564
    HOT_GAS_TEMPERATURE_HP4 = 565
    LOW_PRESSURE_HP4 = 566
    MEAN_PRESSURE_HP4 = 567
    HIGH_PRESSURE_HP4 = 568
    WP_WATER_FLOW_RATE_HP4 = 569
    RETURN_TEMPERATURE_HP5 = 570
    FLOW_TEMPERATURE_HP5 = 571
    HOT_GAS_TEMPERATURE_HP5 = 572
    LOW_PRESSURE_HP5 = 573
    MEAN_PRESSURE_HP5 = 574
    HIGH_PRESSURE_HP5 = 575
    WP_WATER_RATE_HP5 = 576
    RETURN_TEMPERATURE_HP6 = 577
    FLOW_TEMPERATURE_HP6 = 578
    HOT_GAS_HP6 = 579
    LOW_PRESSURE_HP6 = 580
    MEAN_PRESSURE_HP6 = 581
    HIGH_PRESSURE_HP6 = 582
    WP_WATER_RATE_HP6 = 583


class WpmEnergySystemInformationRegisters(IsgRegisters):
    SG_READY_OPERATING_STATE = 5001
    CONTROLLER_IDENTIFICATION = 5002


WPM_SYSTEM_VALUES_REGISTERS = {
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FE7: ModbusRegister(
        address=501,
        name="ACTUAL TEMPERATURE FE7",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FE7,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_FE7: ModbusRegister(
        address=502,
        name="SET TEMPERATURE FE7",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_FE7,
    ),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FEK: ModbusRegister(
        address=503,
        name="ACTUAL TEMPERATURE FEK",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FEK,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_FEK: ModbusRegister(
        address=504,
        name="SET TEMPERATURE FEK",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_FEK,
    ),
    WpmSystemValuesRegisters.RELATIVE_HUMIDITY: ModbusRegister(
        address=505,
        name="RELATIVE HUMIDITY",
        unit="%",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.RELATIVE_HUMIDITY,
    ),
    WpmSystemValuesRegisters.DEW_POINT_TEMPERATURE: ModbusRegister(
        address=506,
        name="DEW POINT TEMPERATURE",
        unit="°C",
        min=-40.0,
        max=30.0,
        data_type=2,
        key=WpmSystemValuesRegisters.DEW_POINT_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.OUTSIDE_TEMPERATURE: ModbusRegister(
        address=507,
        name="OUTSIDE TEMPERATURE",
        unit="°C",
        min=-60.0,
        max=80.0,
        data_type=2,
        key=WpmSystemValuesRegisters.OUTSIDE_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_1: ModbusRegister(
        address=508,
        name="ACTUAL TEMPERATURE HK 1",
        unit="°C",
        min=0.0,
        max=40.0,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_1,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1_WPM3I: ModbusRegister(
        address=509,
        name="SET TEMPERATURE HK 1",
        unit="°C",
        min=0.0,
        max=65.0,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1_WPM3I,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1: ModbusRegister(
        address=510,
        name="SET TEMPERATURE HK 1",
        unit="°C",
        min=0.0,
        max=40.0,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_HK_1,
    ),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_2: ModbusRegister(
        address=511,
        name="ACTUAL TEMPERATURE HK 2",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_HK_2,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_HK_2: ModbusRegister(
        address=512,
        name="SET TEMPERATURE HK 2",
        unit="°C",
        min=0.0,
        max=65.0,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_HK_2,
    ),
    WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_WP: ModbusRegister(
        address=513,
        name="ACTUAL FLOW TEMPERATURE WP",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_WP,
    ),
    WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_NHZ: ModbusRegister(
        address=514,
        name="ACTUAL FLOW TEMPERATURE NHZ",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE_NHZ,
    ),
    WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE: ModbusRegister(
        address=515,
        name="ACTUAL FLOW TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_FLOW_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.ACTUAL_RETURN_TEMPERATURE: ModbusRegister(
        address=516,
        name="ACTUAL RETURN TEMPERATURE",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_RETURN_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.SET_FIXED_TEMPERATURE: ModbusRegister(
        address=517,
        name="SET FIXED TEMPERATURE",
        unit="°C",
        min=20.0,
        max=50.0,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_FIXED_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.ACTUAL_BUFFER_TEMPERATURE: ModbusRegister(
        address=518,
        name="ACTUAL BUFFER TEMPERATURE",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_BUFFER_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.SET_BUFFER_TEMPERATURE: ModbusRegister(
        address=519,
        name="SET BUFFER TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_BUFFER_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.HEATING_PRESSURE: ModbusRegister(
        address=520,
        name="HEATING PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.HEATING_PRESSURE,
    ),
    WpmSystemValuesRegisters.FLOW_RATE: ModbusRegister(
        address=521,
        name="FLOW RATE",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.FLOW_RATE,
    ),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_DHW: ModbusRegister(
        address=522,
        name="ACTUAL TEMPERATURE DHW",
        unit="°C",
        min=10.0,
        max=65.0,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_DHW,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_DHW: ModbusRegister(
        address=523,
        name="SET TEMPERATURE DHW",
        unit="°C",
        min=10.0,
        max=65.0,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_DHW,
    ),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FAN: ModbusRegister(
        address=524,
        name="ACTUAL TEMPERATURE FAN",
        unit="K",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_FAN,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_FAN: ModbusRegister(
        address=525,
        name="SET TEMPERATURE FAN",
        unit="K",
        min=7.0,
        max=25.0,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_FAN,
    ),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_AREA: ModbusRegister(
        address=526,
        name="ACTUAL TEMPERATURE AREA",
        unit="K",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_AREA,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_AREA: ModbusRegister(
        address=527,
        name="SET TEMPERATURE AREA",
        unit="K",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_AREA,
    ),
    WpmSystemValuesRegisters.COLLECTOR_TEMPERATURE: ModbusRegister(
        address=528,
        name="COLLECTOR TEMPERATURE",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=WpmSystemValuesRegisters.COLLECTOR_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.CYLINDER_TEMPERATURE: ModbusRegister(
        address=529,
        name="CYLINDER TEMPERATURE",
        unit="°C",
        min=0.0,
        max=90.0,
        data_type=2,
        key=WpmSystemValuesRegisters.CYLINDER_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.RUNTIME: ModbusRegister(
        address=530,
        name="RUNTIME",
        unit="h",
        min=None,
        max=None,
        data_type=6,
        key=WpmSystemValuesRegisters.RUNTIME,
    ),
    WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_EXTERNAL: ModbusRegister(
        address=531,
        name="ACTUAL TEMPERATURE EXTERNAL",
        unit="°C",
        min=10.0,
        max=90.0,
        data_type=2,
        key=WpmSystemValuesRegisters.ACTUAL_TEMPERATURE_EXTERNAL,
    ),
    WpmSystemValuesRegisters.SET_TEMPERATURE_EXTERNAL: ModbusRegister(
        address=532,
        name="SET TEMPERATURE EXTERNAL",
        unit="K",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.SET_TEMPERATURE_EXTERNAL,
    ),
    WpmSystemValuesRegisters.APPLICATION_LIMIT_HZG: ModbusRegister(
        address=533,
        name="APPLICATION LIMIT HZG",
        unit="°C",
        min=-40.0,
        max=40.0,
        data_type=2,
        key=WpmSystemValuesRegisters.APPLICATION_LIMIT_HZG,
    ),
    WpmSystemValuesRegisters.APPLICATION_LIMIT_WW: ModbusRegister(
        address=534,
        name="APPLICATION LIMIT WW",
        unit="°C",
        min=-40.0,
        max=40.0,
        data_type=2,
        key=WpmSystemValuesRegisters.APPLICATION_LIMIT_WW,
    ),
    WpmSystemValuesRegisters.RUNTIME_EHS: ModbusRegister(
        address=535,
        name="RUNTIME",
        unit="h",
        min=None,
        max=None,
        data_type=6,
        key=WpmSystemValuesRegisters.RUNTIME_EHS,
    ),
    WpmSystemValuesRegisters.SOURCE_TEMPERATURE: ModbusRegister(
        address=536,
        name="SOURCE TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.SOURCE_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.MIN_SOURCE_TEMPERATURE: ModbusRegister(
        address=537,
        name="MIN SOURCE TEMPERATURE",
        unit="°C",
        min=-10.0,
        max=10.0,
        data_type=2,
        key=WpmSystemValuesRegisters.MIN_SOURCE_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.SOURCE_PRESSURE: ModbusRegister(
        address=538,
        name="SOURCE PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.SOURCE_PRESSURE,
    ),
    WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE: ModbusRegister(
        address=539,
        name="HOT GAS TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE,
    ),
    WpmSystemValuesRegisters.HIGH_PRESSURE: ModbusRegister(
        address=540,
        name="HIGH PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HIGH_PRESSURE,
    ),
    WpmSystemValuesRegisters.LOW_PRESSURE: ModbusRegister(
        address=541,
        name="LOW PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.LOW_PRESSURE,
    ),
    WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP1: ModbusRegister(
        address=542,
        name="RETURN TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP1,
    ),
    WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP1: ModbusRegister(
        address=543,
        name="FLOW TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP1,
    ),
    WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP1: ModbusRegister(
        address=544,
        name="HOT GAS TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP1,
    ),
    WpmSystemValuesRegisters.LOW_PRESSURE_HP1: ModbusRegister(
        address=545,
        name="LOW PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.LOW_PRESSURE_HP1,
    ),
    WpmSystemValuesRegisters.MEAN_PRESSURE_HP1: ModbusRegister(
        address=546,
        name="MEAN PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.MEAN_PRESSURE_HP1,
    ),
    WpmSystemValuesRegisters.HIGH_PRESSURE_HP1: ModbusRegister(
        address=547,
        name="HIGH PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.HIGH_PRESSURE_HP1,
    ),
    WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP1: ModbusRegister(
        address=548,
        name="WP WATER FLOW RATE",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP1,
    ),
    WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP2: ModbusRegister(
        address=549,
        name="RETURN TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP2,
    ),
    WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP2: ModbusRegister(
        address=550,
        name="FLOW TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP2,
    ),
    WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP2: ModbusRegister(
        address=551,
        name="HOT GAS TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP2,
    ),
    WpmSystemValuesRegisters.LOW_PRESSURE_HP2: ModbusRegister(
        address=552,
        name="LOW PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.LOW_PRESSURE_HP2,
    ),
    WpmSystemValuesRegisters.MEAN_PRESSURE_HP2: ModbusRegister(
        address=553,
        name="MEAN PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.MEAN_PRESSURE_HP2,
    ),
    WpmSystemValuesRegisters.HIGH_PRESSURE_HP2: ModbusRegister(
        address=554,
        name="HIGH PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.HIGH_PRESSURE_HP2,
    ),
    WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP2: ModbusRegister(
        address=555,
        name="WP WATER FLOW RATE",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP2,
    ),
    WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP3: ModbusRegister(
        address=556,
        name="RETURN TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP3,
    ),
    WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP3: ModbusRegister(
        address=557,
        name="FLOW TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP3,
    ),
    WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP3: ModbusRegister(
        address=558,
        name="HOT GAS TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP3,
    ),
    WpmSystemValuesRegisters.LOW_PRESSURE_HP3: ModbusRegister(
        address=559,
        name="LOW PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.LOW_PRESSURE_HP3,
    ),
    WpmSystemValuesRegisters.MEAN_PRESSURE_HP3: ModbusRegister(
        address=560,
        name="MEAN PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.MEAN_PRESSURE_HP3,
    ),
    WpmSystemValuesRegisters.HIGH_PRESSURE_HP3: ModbusRegister(
        address=561,
        name="HIGH PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.HIGH_PRESSURE_HP3,
    ),
    WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP3: ModbusRegister(
        address=562,
        name="WP WATER FLOW RATE",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP3,
    ),
    WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP4: ModbusRegister(
        address=563,
        name="RETURN TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP4,
    ),
    WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP4: ModbusRegister(
        address=564,
        name="FLOW TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP4,
    ),
    WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP4: ModbusRegister(
        address=565,
        name="HOT GAS TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP4,
    ),
    WpmSystemValuesRegisters.LOW_PRESSURE_HP4: ModbusRegister(
        address=566,
        name="LOW PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.LOW_PRESSURE_HP4,
    ),
    WpmSystemValuesRegisters.MEAN_PRESSURE_HP4: ModbusRegister(
        address=567,
        name="MEAN PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.MEAN_PRESSURE_HP4,
    ),
    WpmSystemValuesRegisters.HIGH_PRESSURE_HP4: ModbusRegister(
        address=568,
        name="HIGH PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.HIGH_PRESSURE_HP4,
    ),
    WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP4: ModbusRegister(
        address=569,
        name="WP WATER FLOW RATE",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.WP_WATER_FLOW_RATE_HP4,
    ),
    WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP5: ModbusRegister(
        address=570,
        name="RETURN TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP5,
    ),
    WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP5: ModbusRegister(
        address=571,
        name="FLOW TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP5,
    ),
    WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP5: ModbusRegister(
        address=572,
        name="HOT GAS TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HOT_GAS_TEMPERATURE_HP5,
    ),
    WpmSystemValuesRegisters.LOW_PRESSURE_HP5: ModbusRegister(
        address=573,
        name="LOW PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.LOW_PRESSURE_HP5,
    ),
    WpmSystemValuesRegisters.MEAN_PRESSURE_HP5: ModbusRegister(
        address=574,
        name="MEAN PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.MEAN_PRESSURE_HP5,
    ),
    WpmSystemValuesRegisters.HIGH_PRESSURE_HP5: ModbusRegister(
        address=575,
        name="HIGH PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.HIGH_PRESSURE_HP5,
    ),
    WpmSystemValuesRegisters.WP_WATER_RATE_HP5: ModbusRegister(
        address=576,
        name="WP WATER RATE",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.WP_WATER_RATE_HP5,
    ),
    WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP6: ModbusRegister(
        address=577,
        name="RETURN TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.RETURN_TEMPERATURE_HP6,
    ),
    WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP6: ModbusRegister(
        address=578,
        name="FLOW TEMPERATURE",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.FLOW_TEMPERATURE_HP6,
    ),
    WpmSystemValuesRegisters.HOT_GAS_HP6: ModbusRegister(
        address=579,
        name="HOT GAS",
        unit="°C",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.HOT_GAS_HP6,
    ),
    WpmSystemValuesRegisters.LOW_PRESSURE_HP6: ModbusRegister(
        address=580,
        name="LOW PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.LOW_PRESSURE_HP6,
    ),
    WpmSystemValuesRegisters.MEAN_PRESSURE_HP6: ModbusRegister(
        address=581,
        name="MEAN PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.MEAN_PRESSURE_HP6,
    ),
    WpmSystemValuesRegisters.HIGH_PRESSURE_HP6: ModbusRegister(
        address=582,
        name="HIGH PRESSURE",
        unit="bar",
        min=None,
        max=None,
        data_type=7,
        key=WpmSystemValuesRegisters.HIGH_PRESSURE_HP6,
    ),
    WpmSystemValuesRegisters.WP_WATER_RATE_HP6: ModbusRegister(
        address=583,
        name="WP WATER RATE",
        unit="l/min",
        min=None,
        max=None,
        data_type=2,
        key=WpmSystemValuesRegisters.WP_WATER_RATE_HP6,
    ),
}

WPM_ENERGY_SYSTEM_INFORMATION_REGISTERS = {
    WpmEnergySystemInformationRegisters.SG_READY_OPERATING_STATE: ModbusRegister(
        address=5001,
        name="SG READY OPERATING STATE",
        unit="",
        min=1.0,
        max=4.0,
        data_type=6,
        key=WpmEnergySystemInformationRegisters.SG_READY_OPERATING_STATE,
    ),
    WpmEnergySystemInformationRegisters.CONTROLLER_IDENTIFICATION: ModbusRegister(
        address=5002,
        name="CONTROLLER IDENTIFICATION",
        unit="",
        min=None,
        max=None,
        data_type=6,
        key=WpmEnergySystemInformationRegisters.CONTROLLER_IDENTIFICATION,
    ),
}


class WpmStiebelEltronAPI(StiebelEltronAPI):
    def __init__(self, host: str, port: int = 502, slave: int = 1) -> None:
        super().__init__(
            [
                ModbusRegisterBlock(
                    base_address=500,
                    count=83,
                    name="System Values",
                    registers=WPM_SYSTEM_VALUES_REGISTERS,
                ),
                ModbusRegisterBlock(
                    base_address=5000,
                    count=2,
                    name="Energy System Information",
                    registers=WPM_ENERGY_SYSTEM_INFORMATION_REGISTERS,
                ),
            ],
            host,
            port,
            slave,
        )
