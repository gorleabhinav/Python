# Running async functions on separate thread
----------------------------------------------------
In this example, we are starting event loop inside separate thread and submitting coroutines to given loop using function `asyncio.run_coroutine_threadsafe(coro, loop)` from main thread.

To run `python3 running_coroutines_on_seperate_thread.py`

In output all coroutines and main functions are running concurrently