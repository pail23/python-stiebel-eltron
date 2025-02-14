import asyncio

from python_stiebel_eltron.wpm import WpmStiebelEltronAPI


async def main():
    api = WpmStiebelEltronAPI("192.168.1.209", 502)
    await api.connect()

    await api.async_update()
    for k, v in api._data.items():
        if v is not None:
            print(f"{k.name} ({k.value}): {v}")

    await api.close()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(main())
