import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()
    await nc.connect("nats://127.0.0.1:4222")

    # Group1 subscriber
    async def g1_handler(msg):
        print(f"[Group1] got: {msg.data.decode()}")
    await nc.subscribe("group1.events", cb=g1_handler)

    # Group2 subscriber
    async def g2_handler(msg):
        print(f"[Group2] got: {msg.data.decode()}")
    await nc.subscribe("group2.events", cb=g2_handler)

    # Publish into group1
    await nc.publish("group1.events", b"hello from group1 publisher")

    # Publish into group2
    await nc.publish("group2.events", b"hello from group2 publisher")

    await asyncio.sleep(1)
    await nc.drain()

asyncio.run(run())