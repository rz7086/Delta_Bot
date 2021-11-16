import discord
from discord.ext import commands
import json
import os

#'''
with open("setting.json",mode='r',encoding='utf8') as jFile: 
    jdata = json.load(jFile)                        #命名setting
#'''

bot = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
    print("bot is hello world.")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    print('loaded')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    print('unloaded')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    print('reloaded')

for filename in os.listdir('cmds'):       #列出cmds這個資料夾裡的檔案
    print(filename)
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')



if __name__ == "__main__":
    bot.run(jdata["TOKEN"])

