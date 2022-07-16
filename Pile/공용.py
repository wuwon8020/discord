import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
import random
import dice




class Core(commands.Cog, name="공용"):
 
    def __init__(self, app):
        self.app = app

    @commands.command(name="help", help = "명령어 리스트를 출력합니다", usage = "@help")
    async def help_command(self, ctx, func=None):
      
        if func is None:
            embed = discord.Embed(title="디스코드 봇", description="접두사는 `$` 입니다.") #Embed 생성
            cog_list = ["공용"] # Cog 리스트 추가
            for x in cog_list: # cog_list에 대한 반복문
                 cog_data = self.app.get_cog(x) # x에 대해 Cog 데이터를 구하기
                 command_list = cog_data.get_commands() # cog_data에서 명령어 리스트 구하기
                 embed.add_field(name=x, value=" ".join([c.name for c in command_list]), inline=False) # 필드 추가
                 
            cog_list = ["놀이터"] # Cog 리스트 추가
            for x in cog_list: # cog_list에 대한 반복문
                 cog_data = self.app.get_cog(x) # x에 대해 Cog 데이터를 구하기
                 command_list = cog_data.get_commands() # cog_data에서 명령어 리스트 구하기
                 embed.add_field(name=x, value=" ".join([c.name for c in command_list]), inline=False) # 필드 추가
            
        else: # func가 None이 아니면
         command_notfound = True # 이걸 어떻게 쓸지 생각해보세요!
         for _title, cog in self.app.cogs.items(): # title, cog로 item을 돌려주는데 title은 필요가 없습니다.
          if not command_notfound: # False면
            break # 반복문 나가기

          else: # 아니면
            for title in cog.get_commands(): # 명령어를 아까처럼 구하고 title에 순차적으로 넣습니다.
                if title.name == func: # title.name이 func와 같으면
                    cmd = self.app.get_command(title.name) # title의 명령어 데이터를 구합니다.

                
                    embed = discord.Embed(title=f"명령어 : {cmd}", description=cmd.help, inline=False) # Embed 만들기
        
                    break # 반복문 나가기
                else:
                    command_notfound = True

            
        await ctx.send(embed=embed) # 보내기




    @commands.command(name="roll", help = "주사위를 돌립니다. (M면체 주사위를 N번 돌립니다)", usage = "$roll NdM")
    async def roll(self, ctx, dice):
       await ctx.send(embed = dice(ctx, dice))

    @commands.command(name = "입장")
    async def start_command(ctx):
        embed = discord.Embed(title="SHOP BOT",description="SHOP 아이템 목록. 쇼핑을 합시다", color=0x00aaaa)
        embed.add_field(name="STEP🦶", value="빠르게 이동한다", inline=False)
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("🦶") #step
        
    
    @commands.event
    async def on_reaction_add(reaction, user):
    

        if str(reaction.emoji) == "🦶":
            await user.add_roles(get(user.guild.roles, name="마크"))
    



def setup(app):
    app.add_cog(Core(app))
