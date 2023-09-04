import asyncio

async def fetch_products():
    print("Fetching Products...")
    await asyncio.sleep(2)
    print("Obtained Products....")
    return {"name": "Jim Can Supplies", "code": 12922, "price": 13.23}

async def main():
    # create task
    task1 = asyncio.create_task(fetch_products())
    product = await task1
    print(product)

asyncio.run(main())
