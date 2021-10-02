import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get

class 놀이터(commands.Cog, name = "놀이터"):

    def __init__(self, app):
        self.app = app
    
    
    @commands.command(name = "RRR", help = "놀이터 R-18 권한을 갖거나 해제할수 있습니다", usage = "$RRR 로보토미 OR 원신, $RRR 로보토미해제 OR 원신해제")
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
     
    @commands.command(name="만만이", help = "만만이", usage = "만만이") #수정
    async def 만만이(self, ctx): #수정
        await ctx.send("```검열됨```")

def setup(app):
    app.add_cog(놀이터(app))