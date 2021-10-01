import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)
import discord,asyncio
from discord.ext import commands
import discord,asyncio
import datetime
import random
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get



client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online) #온라인
  #await client.change_presence(status=discord.Status.idle) #자리비움
  #await client.change_presence(status=discord.Status.dnd) #다른용무
  #await client.change_presence(status=discord.Status.offline) #오프라인

  await client.change_presence(activity=discord.Game(name="흑우의 디스코드 봇"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))

@client.command()
async def hello(ctx):
    await ctx.send('안녕하세요')


@client.command()
async def 만만이(ctx):
    await ctx.send('```검열됨```')



@client.command()
async def roll(ctx, dice):
    lenth = len(dice)
    a=0
    b=0
    pp = list()
    i=0
    dice2 = list()
    dice3 = list()
    ak = 0
    while a<lenth :
        if dice[a:a+1] == "+" :
             a=lenth
             ak=2
        a=a+1
    embed = discord.Embed(title = "주사위",
    description = dice, color = 0x62c1cc)
    embed.set_footer(text = f"{ctx.message.author.name}", icon_url = ctx.message.author.avatar_url)
    if ak != 2 :
     dice2 = list()
     dice2 = dice.split('d')
     
     k = int(dice2[0])
     j = int(dice2[1])
     i=0
     while i<k :
        pp.insert(i+1, random.randrange(1, j))
        i=i+1
     i=0
     sum = 0

     while i<k :
        sum = sum + pp[i]  
        i=i+1

     pp.insert(0, "```[")
     pp.insert(k+1, "]```")   

     for o in range(len(pp)):
      pp[o] = str(pp[o])

     pa= ' ' .join(pp)
    
     
     embed.add_field(name = "Roll", value = pa,  inline=True)
     embed.add_field(name = "Result", value = sum, inline=True)
     
     
    else :
      dice2 = dice.split('d')
      lenth = len(dice)
      i=0
      z=1
      k=0
      j=0
      pa = ""
      while i<lenth:
	         if dice[i] =="+":
		          z=z+1
	         i=i+1

      i=0
      dice2=dice.split('+') 
      Allsum = 0
      while i<z :
         pp = list()
         dice3 = list()
         dice3 = dice2[i].split('d')
         k = int(dice3[0])
         j = int(dice3[1])
         m=0
         while m<k :
          pp.insert(m+1, random.randrange(1, j))
          m=m+1
         
         m=0
         sum = 0 
         while m<k :
          sum = sum + pp[m]  
          m=m+1
         Allsum = Allsum + sum 
         pp.insert(0, "``[")
         pp.insert(k+1, "]``")  

         for o in range(len(pp)):
          pp[o] = str(pp[o]) 

         pa= ' ' .join(pp)

         embed.add_field(name = "Roll", value = pa,  inline=False)
         embed.add_field(name = "Result", value = sum, inline=False)
         i=i+1
      embed.add_field(name = "All Result", value = Allsum, inline=False)
    await ctx.send(embed = embed)
     

@client.command()
async def Allrole(ctx):
    embed = discord.Embed(title = "역할들",
    description = "역할 id, 명칭", color = 0x62c1cc)
    for i in range(len(ctx.guild.roles)):
        embed.add_field(name = ctx.guild.roles[i].name, value = ctx.guild.roles[i].id,  inline=False)
    await ctx.send(embed = embed)

@client.command()
async def RRR(ctx, RRR):
    member = ctx.message.author
    
    if RRR == "로보토미" :
        await member.add_roles(get(ctx.guild.roles, name="롭토 R-18"))
        embed = discord.Embed(title = "로보토미 R-18 지급",
        description = "", color = 0x62c1cc)
        embed.set_footer(text = f"{ctx.message.author.name}", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif RRR == "원신" :
        await member.add_roles(get(ctx.guild.roles, name="원신 R-18"))
        embed = discord.Embed(title = "원신 R-18 지급",
        description = "", color = 0x62c1cc)
        embed.set_footer(text = f"{ctx.message.author.name}", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif  RRR == "로보토미해제" :
        await member.remove_roles(get(ctx.guild.roles, name='롭토 R-18'))
        embed = discord.Embed(title = "로보토미 R-18 해제",
        description = "", color = 0x62c1cc)
        embed.set_footer(text = f"{ctx.message.author.name}", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif RRR == "원신해제" :
        await member.remove_roles(get(ctx.guild.roles, name='원신 R-18'))
        embed = discord.Embed(title = "원신 R-18 해제",
        description = "", color = 0x62c1cc)
        embed.set_footer(text = f"{ctx.message.author.name}", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)







client.run(os.environ['token'])