import os
from random import choice
from telethon import events

async def init(bot):
    @bot.on(events.NewMessage(pattern=r'plugins', outgoing=True))
    async def get_plugins_list(e):
        emojies = ["😁","😄","🙄","😀","😋","😎"]
        plugins = ["{} [`{}`]".format(choice(emojies), file.split(".")[0]) for file in os.listdir(os.path.dirname(__file__)) if file[0].isalpha() and file.endswith('.py')]
        modules = {m.split('.')[-1]: f"__{m}__" for m in plugins}
        print("plugins: ", plugins)
        await e.edit("**🚀Plugins:**\n{}".format("\n".join(plugins)))
