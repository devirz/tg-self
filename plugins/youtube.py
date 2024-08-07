import json
from telethon import functions, types
from telethon.events import NewMessage
from yt_dlp import YoutubeDL

youtube_url_pattern = r'(http(s)?:\/\/)?(www\.)?youtu(be\.com|\.be)\/.+'

async def init(bot):
    @bot.on(NewMessage(pattern=r'yt (http(s)?:\/\/)?(www\.)?youtu(be\.com|\.be)\/.+', outgoing=True))
    async def youtube_downloader(event):
        await event.edit('**wait...**')
        url = event.message.text[3:]
        print(url)
        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            data = { 'id': info['id'], 'title': info['title'], 'thumb': info['thumbnails'][-2]['url'], 'duration': info['duration_string'], 'uploader': info['uploader'], 'date': info['upload_date'] }
            await event.delete()
            caption = f"**ID:** `{data['id']}`\n**Title:** `{data['title']}`\n**Duration:** `{data['duration']}`\n**Date:** `{data['date']}`\n**Uploader:** `{data['uploader']}`"
            await bot.send_file(event.message.chat.id, data['thumb'], caption=caption)
            s = await event.reply("**Waiting For Download...**")
            ydl_opts = {
                'writethumbnail': True,
                'format': 'mp3/bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320'
                },
                {'key': 'EmbedThumbnail'}]
            }
            with YoutubeDL(ydl_opts) as yt:
                res = yt.download(url)
                if not res:
                    await s.edit("**Download Finished.\nWait For Upload...**")
                    await bot.send_file(event.message.chat.id, f"{data['title']} [{data['id']}].mp3")
                    await s.delete()
            #await bot.send_file(event.message.chat.id, data[''])
            '''
            result = await bot(functions.channels.EditPhotoRequest(
        channel=event.message.chat.id,
        photo=await bot.upload_file(data['thumb'])
    ))
    '''
    
