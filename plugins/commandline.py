import subprocess
from telethon import events


def run_command(command: str) -> str:
    """Utility function to run commands."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode("utf-8")


async def init(bot):
    @bot.on(events.NewMessage(pattern=r'[Rr][Uu][Nn] (.+)'))
    async def command_runner(event):
        text = event.message.text[4:]
        output = run_command(text)
        await event.edit("**Output:**\n`{}`".format(output))
