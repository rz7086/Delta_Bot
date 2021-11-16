import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time

class hello(Cog_Extension):
    @commands.Cog.listener()
    async def saysomething(self, msg):
        await msg.channel.send('hello')

def setup(bot):
    bot.add_cog(hello(bot))