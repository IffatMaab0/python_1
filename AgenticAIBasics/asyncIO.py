import asyncio


async def func1():
    print("hello")
    await asyncio.sleep(5)
    print("Hello after 5 sec")
async def func2():
    print("leo")
    await asyncio.sleep(3)
    print("Leo after 3 sec")   
async def main():
    await asyncio.gather(func1(),func2())
asyncio.run(main())      