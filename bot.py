import discord 
import os
import sys
import io
from discord.ext import commands
import textwrap
import traceback
from contextlib import redirect_stdout
import json

# This part defines the bot prefix, the description and the owner ID.

bot = commands.Bot(command_prefix="-", description="InfinityBot is an amazing discord bot!", owner_id=362615327441420289)
bot.remove_command('help')

# This part checks the stuff when bot starts

developers = [
    362615327441420289,
    292690616285134850
]


def dev_check(id):
    with open('data/devs.json') as f:
        devs = json.load(f)
    if id in devs:
        return True
    else:
        return False



def cleanup_code(content):
    '''Automatically removes code blocks from the code.'''
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])
 
    return content.strip('` \n')


@bot.event
async def on_ready():
    print("Bot Is Online")
    
    
# Help command


@bot.command()
async def help(ctx):
    em = discord.Embed(color=discord.Color(value=0xFBCC16)) 
    em.title = "Bot Commands"
    em.description = "A bot being developed by Apollo, Free TNT and Affinix. Hop into the development server [here](https://discord.gg/vXwFVdy)"
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
    

@bot.command(hidden=True, name='eval')
async def _eval(ctx, *, body: str):

    if not dev_check(ctx.author.id):
        return

    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        try:
            await ctx.message.add_reaction('\u2705')
        except:
            pass

        if ret is None:
            if value:
                await ctx.send(f'```py\n{value}\n```')
        else:
            await ctx.send(f'```py\n{value}{ret}\n```')    
    
    
if not os.environ.get('TOKEN'):
  print("Could not find token!")
bot.run(os.environ.get('TOKEN').strip('\"'))
