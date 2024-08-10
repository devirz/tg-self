import os
import sys
import asyncio
from telethon.sync import TelegramClient, events
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

if (not API_ID or not API_HASH):
  raise ValueError("Please set api id and api hash in .env file!")

try:
  # Standalone script assistant.py with folder plugins/
  import plugins
except ImportError:
  try:
    # Running as a module with `python -m assistant` and structure:
    #
    #     assistant/
    #         __main__.py (this file)
    #         plugins/    (cloned)
    from . import plugins
  except ImportError:
    print('could not load the plugins module, does the directory exist '
          'in the correct location?', file=sys.stderr)

    exit(1)

bot = TelegramClient("devirz_backup", API_ID, API_HASH)


async def main():
  await plugins.init(bot)
  await bot.start()
  await bot.run_until_disconnected()

if __name__ == '__main__':
  asyncio.run(main())