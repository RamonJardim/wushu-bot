import discord
import os

import music
import functions

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot = commands.Bot(command_prefix='!')
token = os.getenv("DISCORD_BOT_SECRET")

music.setup(bot)
functions.setup(bot)
    
@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    servers = list(bot.guilds)
    await bot.change_presence(game=discord.Game(name='LoL as Zoe'))
    print('Servers: ')
    printServers(servers)

def printServers(servers):
  for i in range(len(servers)):
    print(servers[i].name)
    
    
print(discord.version_info)
bot.run(token)