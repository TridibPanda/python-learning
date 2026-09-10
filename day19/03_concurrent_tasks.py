import asyncio


async def task_one():
    print("Task One: Start")
    await asyncio.sleep(2)
    print("Task One: End")


async def task_two():
    print("Task Two: Start")
    await asyncio.sleep(1)
    print("Task Two: End")


async def main():
    print("Main: Start")

    task1 = asyncio.create_task(task_one())
    task2 = asyncio.create_task(task_two())

    await task1
    await task2

    print("Main: End")


asyncio.run(main())
# Output:
# Main: Start
# Task One: Start
# Task Two: Start
# Task Two: End
# Task One: End
# Main: End
