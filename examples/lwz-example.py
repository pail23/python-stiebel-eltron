#!/usr/bin/env python3
"""Example that uses the optional tmodbus backend with an LWZ heat pump.

For the development environment, initialize and sync with uv:
``uv sync --all-extras``.
"""

import argparse
import asyncio

from modbus_connection import ModbusTcpParams
from modbus_connection.tmodbus import ModbusConnection

from pystiebeleltron.lwz import LwzStiebelEltronAPI

host_port = 502
device_id = 1


async def main(host_ip: str) -> None:
    connection = ModbusConnection(ModbusTcpParams(host=host_ip, port=host_port))
    api = LwzStiebelEltronAPI(connection.for_unit(device_id))

    await api.async_update()

    room_temp = api.get_current_temp()
    target_temp = api.get_target_temp()
    outside_temp = api.system_values.outside_temperature
    operation = api.get_operation().name

    print(f"The current room temperature is {room_temp} °C")
    print(f"The target room temperature is {target_temp} °C")
    print(f"The current outside temperature is {outside_temp} °C")
    print(f"The current operating mode is {operation}")
    await connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read values from an LWZ heat pump.")
    parser.add_argument("host_ip", help="IP address of the ISG gateway")
    args = parser.parse_args()
    asyncio.run(main(args.host_ip))
