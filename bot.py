from discord.client import Client
from discord.errors import ClientException
from discord.ext import commands
import discord,asyncio
import datetime
import random
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
import os


client = commands.Bot(command_prefix='$')




@client.event
async def on_ready():
  client.remove_command("help")
  for filename in os.listdir("Pile"):
    if filename.endswith(".py"):
        client.load_extension(f"Pile.{filename[:-3]}")

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임 하는중"))




@client.command()
async def hello(ctx):
    await ctx.send('안녕하세요')

@client.command(name="리로드") #1
async def reload_commands(ctx, extension=None): #2
    if extension is None: #3
         for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                client.unload_extension(f"Cogs.{filename[:-3]}")
                client.load_extension(f"Cogs.{filename[:-3]}")
                await ctx.send(":white_check_mark: 모든 명령어를 다시 불러왔습니다!")
    else: #4
        client.unload_extension(f"Cogs.{extension}") #5
        client.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 다시 불러왔습니다!")
        

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title = "명령어 오류!",
        description = "올바른 명령어가 아닙니다. 명령어에 대해 알아볼려면 $help를 입력해주세요.", color = 0x62c1cc)
        await ctx.send(embed=embed)
        return


client.run(os.environ['token'])