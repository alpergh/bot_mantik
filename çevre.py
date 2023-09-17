import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def deniz(ctx):
    with open('images2/mem1.jpg', 'rb') as f:
        
        picture = discord.File(f)
   
    await ctx.send(file=picture) 

@bot.command()
async def dunya(ctx):
        with open('images2/mem2.jpg', 'rb') as f:
        
            picture = discord.File(f)
   
        await ctx.send(file=picture)

@bot.command()
async def işik(ctx):
        with open('images2/mem3.jpg', 'rb') as f:
        
            picture = discord.File(f)
   
        await ctx.send(file=picture)

@bot.command()
async def ses(ctx):
    with open('images2/mem4.jpg', 'rb') as f:
          
        picture = discord.File(f)
        
    await ctx.send(file=picture)
           
@bot.command()
async def helps(ctx):
    with open('images2/mem5.jpg', 'rb') as f:
          
        picture = discord.File(f)
          
    await ctx.send(file=picture)        

bot.run("")
