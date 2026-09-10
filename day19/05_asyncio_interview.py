import asyncio


async def successful_task():
    await asyncio.sleep(1)
    return "Success"


async def failing_task():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong")


async def main():
    try:
        # results = await asyncio.gather(successful_task(), failing_task()) # Output:  Caught: Something went wrong

        results = await asyncio.gather(
            successful_task(), failing_task(), return_exceptions=True
        )
        print("Results:", results)

    except ValueError as error:
        print("Caught:", error)


asyncio.run(main())
# Output:
# Results: ['Success', ValueError('Something went wrong')]
