import discord
from discord.ext import commands
import imagegetter
import os
from dotenv import load_dotenv

# bot_prefix: ska
client = commands.Bot(command_prefix = 'ska ', intents=discord.Intents.all())

load_dotenv()

# ready event
@client.event
async def on_ready():
    print('Ready now!')
    
# wait for message  
@client.event
async def on_message(mes): 
    channel = mes.channel
    content = mes.content
    if content == 'hello':
        # await channel.send('skahere')
        await mes.delete()
    await client.process_commands(mes)
    
@client.command()
async def top(ctx):
    file = discord.File('download/image.jpg')
    # embed = discord.Embed(title = "", description= '', color=0x077ff7)
    # embed.set_image(url = 'download/imagag')
    msg = await ctx.send(file = file)
        
@client.event
async def on_message(mes):
    channel = mes.channel
    content = mes.content
    inputed = str(content).split(" ")
    tag = ""
    if (inputed[0] == 'find' and inputed[1] != 'daily') :
        imagegetter.delete()
        for input in inputed[1:]:
            tag = tag + input + " "
        tag = tag.strip()
        imagegetter.search(tag)
        for i in range(3):
            file = discord.File('download/' + str(i) + 'image.jpg')
            msg = await channel.send(file = file)
    if (inputed[0] == 'find' and inputed[1] == 'daily'):
        imagegetter.delete()
        imagegetter.daily()
        for i in range(5):
            file = discord.File('download/' + str(i) + 'image.jpg')
            msg = await channel.send(file = file)
        
@client.event
async def on_message(mes):
    channel = mes.channel
    content = mes.content
    if (content == 'DDD'):
        imagegetter.delete()
        imagegetter.risu()
        file = discord.File('download/' + str(0)     + 'image.jpg')
        msg = await channel.send(file = file)
        

       
client.run(os.getenv('TOKEN'))