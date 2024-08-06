import asyncio
from telethon import events

async def init(bot):
    @bot.on(events.NewMessage(pattern=r'[Dd][Ll]', outgoing=True))
    async def upload_file(event):
        if event.is_reply:
            #print(event.message.reply_to_msg)
            replied = await event.get_reply_message()
            print("replied: ", replied.stringify())
            if not replied.media:
                await event.edit("**please reply into any media message not text!**")
            else:
                async def callback(current, total):
                    await event.edit("🚀**Downloading:** `{:.2%}`".format(current / total))
                    await asyncio.sleep(1)
                await event.edit("**wait...**")
                file = await bot.download_media(replied, progress_callback=callback)
                await event.edit(f"**Downloaded!**\n**⛱File:** `{file}`")
                Path(file).rename(f"./downloads/{file}")
