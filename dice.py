import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
import random

def dice(ctx, dice) :
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
       return embed

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
       return embed