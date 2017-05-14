import asyncio

async def hello():
    print("Hello world")
    r=await asyncio.sleep(3)
    print("Hello again!")


loop_event=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop_event.run_until_complete(asyncio.wait(tasks))
loop_event.close()