#!/usr/bin/env python3

import asyncio
import threading
from time import sleep
import async_funtions

# create new EL and set it as CEL if there is no CLE in OS thread
loop = asyncio.get_event_loop()

# running event loop forver in thread
threading.Thread(target=loop.run_forever, daemon=True).start()
asyncio.run_coroutine_threadsafe(async_funtions.data_request(),loop)
asyncio.run_coroutine_threadsafe(async_funtions.read_file_content(),loop)
asyncio.run_coroutine_threadsafe(async_funtions.dummy(),loop)

def main():
    while True:
        # doing non-interrupt work
        print("doing non interrupting work")
        sleep(10)

if __name__ == "__main__":
    main()    