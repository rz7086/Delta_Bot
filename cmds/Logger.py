import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time

class Logger(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        
        await msg.channel.send('hello')

def setup(bot):
    bot.add_cog(Logger(bot))