from telethon import events

async def init(bot):
    @bot.on(events.NewMessage(pattern=r'[Pp][Rr] (.+)', outgoing=True))
    async def private_download(event):
        username = event.message.text[3:]
        print(username)
        await event.edit("**wait...**")
        async for message in reversed(bot.iter_messages(username)):
            if message.media:
                await bot.download_media(message)
        await event.edit("**Downloaded!**")
