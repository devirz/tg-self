#import asyncio
import time

from telethon import events


async def init(bot):
    @bot.on(events.NewMessage(pattern=r'[Pp][Ii][Nn][Gg]', outgoing=True))
    async def handler(event, s=time.time()):
        d = time.time() - s
        await event.edit(f'🚀Pong! __({d:.2f}ms)__')
        #await asyncio.sleep(5)
        #await asyncio.gather(event.delete(), message.delete())
