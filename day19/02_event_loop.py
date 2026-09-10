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

    await task_one()
    await task_two()

    print("Main: End")


asyncio.run(main())
# Output:
# Main: Start
# Task One: Start
# Task One: End
# Task Two: Start
# Task Two: End
# Main: End
