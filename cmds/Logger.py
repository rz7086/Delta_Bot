import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time
import logging
logging.basicConfig(filename="log.txt",level=logging.DEBUG)

class Logger(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        logging.info(f"{msg.author} {time} {msg.content}")

        if msg.author != self.bot.user:
            await msg.channel.send('hello')

def setup(bot):
    bot.add_cog(Logger(bot))