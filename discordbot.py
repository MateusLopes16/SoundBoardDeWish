import discord
from discord.ext import commands
import asyncio
import os

connected = False

current_dir = os.path.dirname(os.path.abspath(__file__))

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def greg(ctx, repeat=1):
    await play(ctx, 'greg.mp3', repeat)

@client.command()
async def spies(ctx, repeat=1):
    await play(ctx, 'spies.mp3', repeat)

@client.command()
async def gadjet(ctx, repeat=1):
    await play(ctx, 'gadjet.mp3', repeat)

@client.command()
async def flop(ctx, repeat=1):
    await play(ctx, 'flop.mp3', repeat)

@client.command()
async def beter(ctx, repeat=1):
    await play(ctx, 'beter.mp3', repeat)

@client.command()
async def bzez(ctx, repeat=1):
    await play(ctx, 'bzez.mp3', repeat)

@client.command()
async def cha(ctx, repeat=1):
    await play(ctx, 'cha.mp3', repeat)

#client command erase that erase all the existing messages in the channel
@client.command()
async def erase(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

async def toomuch(ctx):
    await play(ctx, 'toomuch.mp3', 1)
    
async def play(ctx, mp3_file, repeat):
    global connected
    if repeat > 10:
        if connected:
            await ctx.message.delete()
            await ctx.send("Ton grand pere qui a fait la guerre ta cru a vie c'était un artchaut, tu t'est prit pour eminem a vouloir débiter autant !")
            return
        await toomuch(ctx)
        return
    channel = ctx.message.author.voice.channel
    file_path = os.path.join(current_dir, 'files', mp3_file)
    if not connected:
        voice_channel = await channel.connect()
        connected = True
        for i in range(repeat):
            voice_channel.play(discord.FFmpegPCMAudio(file_path), after=lambda e: print('Player error: %s' % e) if e else None)
            while voice_channel.is_playing():
                await asyncio.sleep(1)

        await voice_channel.disconnect()
        connected = False
    else:
        await ctx.message.delete()
        await ctx.send("Ton grand daron avec ses tresses de mexicain calme ta joie, j'suis occupé la !")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        await ctx.send("alors deja que ta pas eu ton bac, en plus tu connais pas le nom des commandes ?!")
    else:
        raise error

client.run('MTEwNzY3OTU0MzU3NTE4NzUxNg.GkkglV.f-oT8CyiOk48r3tMG4-lHb6VhkN9D93panOoH8')
