import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
import random

class Core(commands.Cog, name="공용"):
 
    def __init__(self, app):
        self.app = app

    @commands.command(name="help", help = "명령어 리스트를 출력합니다", usage = "@help")
    async def help_command(self, ctx, func=None):
      
        if func is None:
            embed = discord.Embed(title="흑우의 디스코드 봇", description="접두사는 `$` 입니다.") #Embed 생성
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
                    if func == "RRR" or "만만이" :
                      embed.add_field(name="주의!", value="이 명령어는 놀이터에서만 기동됩니다.") # 사용법 추가
                      
                    embed.add_field(name="사용법", value=cmd.usage, inline=False) # 사용법 추가
                    command_notfound = False
                    break # 반복문 나가기
                else:
                    command_notfound = True

            
        await ctx.send(embed=embed) # 보내기




@commands.command(name="roll", help = "주사위를 돌립니다. (M면체 주사위를 N번 돌립니다)", usage = "$roll NdM")
async def roll(self, ctx, dice):
      lenth = len(dice)
      
      a=0
      b=0
      pp = list()
      i=0
      dice2 = list()
      dice22= list()
      dice3 = list()
      sum = list()
      ak = 0
      
      while a<lenth :
        if dice[a:a+1] == "+" or dice[a:a+1] == "-" or dice[a:a+1] == "*" or dice[a:a+1] == "/":
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
       embed.add_field(name = "Roll", value = pa,  inline=False)
       embed.add_field(name = "Result", value = sum, inline=False)
       await ctx.send(embed = embed)

      else :
  
       lenth = len(dice)
       i=0
       sum = 0 
       z=0
       k=0
       j=0
       pu = list()
       count=list()
       pa = ""
       pu=list()
       ch=list()
       while i<lenth :
        if dice[i] == "+" :
             pu.insert(z, '+')
             z=z+1
        elif dice[i] == "-":
             pu.insert(z, '-')
             z=z+1
        elif dice[i] == "*":
             pu.insert(z, '*')
             z=z+1
        elif dice[i] == "/":
             pu.insert(z, '/')
             z=z+1
        i=i+1   
       
              
       i=0
       #11d20+3d10*2d10
       Allsum = 0
       check = 0
         
       while i<z:
         sum = 0 
         if pu[i] == "+" :
            if check == 0 :
             dice2=dice.split('+',1)
             check=check+1
            else :
             dice22=dice2[1]
             dice2=dice22.split('+',1) 
         elif pu[i] == "-" :
            if check == 0 : 
             dice2=dice.split('-',1)
             check=check+1
            else :
             dice22=dice2[1]
             dice2=dice22.split('-',1) 
         elif pu[i] == "*" :
            if check == 0 : 
             dice2=dice.split('*',1)
             check=check+1
            else :
             dice22=dice2[1]
             dice2=dice22.split('*',1) 
         elif pu[i] == "/" :
            if check == 0 : 
             dice2=dice.split('/') 
             check=check+1  
            else :
                dice22=dice2[1]
                dice2=dice22.split('/')       
         j=0    
         pp = list()
         dice3 = list()
         dice3 = dice2[0].split('d')
         k = int(dice3[0])
         j = int(dice3[1])
         m=0
         while m<k :
          pp.insert(m+1, random.randrange(1, j))
          m=m+1
        
         m=0
         
         while m<k :
          sum = sum + pp[m]  
          m=m+1
     
         
         pp.insert(0, "``[")
         pp.insert(k+1, "]``")  

         for o in range(len(pp)):
          pp[o] = str(pp[o]) 

         pa= ' ' .join(pp)
        
         count.insert(i*2, sum)
         count.insert(i*2+1, pu[i])
   

         embed.add_field(name = "Roll", value = pa,  inline=False)
         embed.add_field(name = "Result", value = sum, inline=False)
        
         i=i+1
       sum = 0
       pp = list()
       dice3 = list()  
      

       dice3 = dice2[1].split('d')
 
       k = int(dice3[0])
       j = int(dice3[1])
     
       m=0
       while m<k :
        pp.insert(m+1, random.randrange(1, j))
        m=m+1
       StrA = ""  
       m=0
    
       while m<k :
        sum = sum + pp[m] 
        m=m+1
      
       pp.insert(0, "``[")
       pp.insert(k+1, "]``")  
      
       for o in range(len(pp)):
        pp[o] = str(pp[o]) 
     
       pa= ' ' .join(pp)
       
       count.insert(i*2, sum)
        
       embed.add_field(name = "Roll", value = pa,  inline=False)
       embed.add_field(name = "Result", value = sum, inline=False)
       for o in range(len(count)):
          count[o] = str(count[o]) 
       StrA = "".join(count) 
       i=0
       j=0
       Allsum = eval(StrA) 
         

       
        
       embed.add_field(name = "All Result", value = Allsum, inline=False)
       await ctx.send(embed = embed)


    



def setup(app):
    app.add_cog(Core(app))
