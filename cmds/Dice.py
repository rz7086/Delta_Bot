import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time
import random
import re

#骰子類
class Dice(Cog_Extension):

    @commands.command()
    async def dice(self, msg):
        if msg.author != self.bot.user:
            txt = str(msg.message.content)
            #分析正則表達式 \d+ d \d+
            it = re.finditer(r"\d+d\d+", txt)

            #搜尋迭代器（好用）
            for match in it:

                #將xdy分解
                paramater = (match.group().split("d"))
                result = ""


                for i in range(int(paramater[0])):
                    result += str(random.randint(1, int(paramater[1]))) + ", "
                result = result.rstrip(", ")
                
                txt = txt.replace(match.group(), result, 1)

            await msg.reply(txt)

def setup(bot):
    bot.add_cog(Dice(bot))