import asyncio


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data received")
    return "Hello from server"


async def main():
    print("Start")

    result = await fetch_data()

    print(f"Result: {result}")
    print("End")


asyncio.run(main())
# Output:
# Start
# Fetching data...
# Data received
# Result: Hello from server
# End
