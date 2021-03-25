import discord
from lib import ping
from lib import badapple

PREFIX = "[]"

class myClient(discord.Client):
    async def on_ready(self): print("SUCCESSFUL LOGIN")
    async def on_message(self, message):
        if message.content.startswith(PREFIX + "ping"): await ping.ping(self,message)
        if message.content.startswith(PREFIX + "badApple"): await badapple.badapple(self,message)
