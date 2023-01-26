import asyncio


async def main_async_await():
    """
        Using Async Await keyword
    """
    print("Start of Async Await Explore!!")
    await proccess_data("My Async func")
    print("Data Processing Completed..")


async def main_async_task():
    """
        Using Async with task for non-blocking or parallel execution
    """
    print("Start of Async Await Explore!!")
    task = asyncio.create_task(proccess_data("My Async func"))
    # execute the task using await keyword
    await task
    print("Data Processing Completed..")


async def main_async_task_sleep():
    """
        Using Async with task for non-blocking or parallel execution
    """
    print("Start of Async Await Explore!!")
    task = asyncio.create_task(proccess_data("My Async func"))
    await asyncio.sleep(1)
    print("Data Processing Completed..")


async def proccess_data(data):
    print(f"Processing Data: {data}")
    await asyncio.sleep(5)
    print("Finializing Data")

asyncio.run(main_async_task_sleep())
