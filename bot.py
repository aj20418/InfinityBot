import discord 
import os
import sys
import io
from discord.ext import commands

# This part defines the bot prefix, the description and the owner ID.

bot = commands.Bot(command_prefix="-", description="ApolloBot0.5 is a testing bot. This isn't the final product!", owner_id=362615327441420289)
bot.remove_command('help')

# This part checks the stuff when bot starts


@bot.event
async def on_ready():
    print("Bot Is Online")
    
    
# Help command


@bot.command()
async def help(ctx):
    em = discord.Embed(color=discord.Color(value=0xFBCC16)) 
    em.title = "Bot Commands"
    em.description = "Use -help to display these"
    em.add_field(name="Ping", value="Pong! Isn't it nice?!")
    em.add_field(name="Say", value="Say something as the bot!")
    em.add_field(name="Invite", value="Invite ApolloBot to your great server!")
    await ctx.send(embed=em)

 
 # Ping command
 
@bot.command()
async def ping(ctx):
    em = discord.Embed(color=discord.Color(value=0xFBCC16))
    em.title = "Pong!"
    em.description = await ctx.send("Pong!")
    await ctx.send(embed=em)
       
        
     
# Invite command

@bot.command()
async def invite(ctx):
    em = discord.Embed(color=discord.Color(value=0xFBCC16))
    em.add_field(name="Invite link", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=380080034586820618&scope=bot&permissions=1)")
    await ctx.send(embed=em)
    
    
@bot.command()
async def say(ctx, *, message:str):
    em = discord.Embed(color=discord.Color(value=0xFBCC16))
    em.description = message
    await ctx.send(embed=em)
    

        
if not os.environ.get('TOKEN'):
  print("Could not find token!")
bot.run(os.environ.get('TOKEN').strip('\"'))
