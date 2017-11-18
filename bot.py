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
    em.title = "Invite"
    em.add_field(name="invite link", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=380080034586820618&scope=bot&permissions=1)")
    await ctx.send(embed=em)
                 

        
if not os.environ.get('TOKEN'):
  print("Could not find token!")
bot.run(os.environ.get('TOKEN').strip('\"'))
