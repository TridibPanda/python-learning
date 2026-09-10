import asyncio


async def fetch_user():
    print("Fetching user...")
    await asyncio.sleep(2)
    return "User data"


async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(1)
    return "Order data"


async def main():
    print("Start")

    user, orders = await asyncio.gather(fetch_user(), fetch_orders())

    print("User:", user)
    print("Orders:", orders)
    print("End")


asyncio.run(main())
# Output:
# Start
# Fetching user...
# Fetching orders...
# User: User data
# Orders: Order data
# End
