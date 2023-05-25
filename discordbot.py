import discord
from discord.ext import commands
import asyncio
import os
import random

connected = False

current_dir = os.path.dirname(os.path.abspath(__file__))

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

commands_names = ["squeezie", "wesh", "cringe", "reuf", "spies", "cha", "kouisine", "spiderman", "libulule", "cerceuil", "donut", "greg", "arab","discours","chant", "monkey", "prout", "ah", "rage"]

for command_name in commands_names:
    @client.command(name=command_name)
    async def play_command(ctx, repeat=1, name=command_name):
        await ctx.message.delete()
        print(name)
        await play(ctx, name + '.mp3', repeat)
    
@client.command()
async def all(ctx):
    await ctx.message.delete()
    await ctx.send("""
**LISTE DE TOUTES LES COMMANDES** 
\n
 - 📞 !greg, *(oue c'est greg)*
 - 🤪 !wesh, *(weeeeesssshhhhhh)*
 - 🥱 !cringe, *(fin frerot, tu es cringe)*
 - 😡 !reuf, *(quoi, comment ca mon reuf ?)*
 - 👀 !spies, *(tu tu tu,   tu tu tu)*
 - 🤩 !cha, *(cha cha cha cha cha cha)*
 - 🙍 !kouisine, *(la place de la femme c'est a la cuisine)*
 - 🕸️ !spiderman, *(chui spiderman fdp)*
 - 🍺 !libulule, *(je pete ma biere ma libulule)*
 - ⚰️ !cerceuil, *(musique du confinement)*
 - 🤷‍♂️ !squeezie, *(est ce que c'est bon pour vous)*
 - 🥯 !donut, *(donut sucré au sucre)*
 - !insulte, *(un bot qui insulte random)*
 - !audio, *(plus qu'a cliquer sur l'emoji)*

*On peut ajouter un chiffre apres la commande pour repeter l'audio plusieurs fois (max 3)*
*Exemple: !wesh 2*
""")

#client command erase that erase all the existing messages in the channel
@client.command()
async def erase(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

async def toomuch(ctx):
    await play(ctx, 'toomuch.mp3', 1)

@client.command()
async def insulte(ctx):
    await ctx.message.delete()
    n = random.randint(1, 5)
    print(n)
    file = 'insulte/insulte' + str(n) + '.mp3'
    await play(ctx, file, 1)
    
async def play(ctx, mp3_file, repeat):
    global connected
    if repeat > 3:
        if connected:
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
        await ctx.send("Ton grand daron avec ses tresses de mexicain calme ta joie, j'suis occupé la !")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        await ctx.send("alors deja que ta pas eu ton bac, en plus tu connais pas le nom des commandes ?!")
    else:
        raise error
    

@client.command()
async def audio(ctx):
    await ctx.message.delete()
    message = await ctx.send("Choose a song to play:")
    await message.add_reaction("📞")
    await message.add_reaction("🤪")
    await message.add_reaction("🥱")
    await message.add_reaction("😡")
    await message.add_reaction("👀")
    await message.add_reaction("🤩")
    await message.add_reaction("🙍")
    await message.add_reaction("🕸️")
    await message.add_reaction("🍺")
    await message.add_reaction("⚰️")
    await message.add_reaction("🤷‍♂️")
    await message.add_reaction("🥯")
    
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0)
    except TimeoutError:
        await ctx.send("trop tard fdp")
        return

    await message.delete()
    if str(reaction.emoji) == "📞":
        await play(ctx, 'greg.mp3', 1)
    elif str(reaction.emoji) == "🤪":
        await play(ctx, 'wesh.mp3', 1)
    elif str(reaction.emoji) == "🥱":
        await play(ctx, 'cringe.mp3', 1)
    elif str(reaction.emoji) == "😡":
        await play(ctx, 'reuf.mp3', 1)
    elif str(reaction.emoji) == "👀":
        await play(ctx, 'spies.mp3', 1)
    elif str(reaction.emoji) == "🤩":
        await play(ctx, 'cha.mp3', 1)
    elif str(reaction.emoji) == "🙍":
        await play(ctx, 'kouisine.mp3', 1)
    elif str(reaction.emoji) == "🕸️":
        await play(ctx, 'spiderman.mp3', 1)
    elif str(reaction.emoji) == "🍺":
        await play(ctx, 'libulule.mp3', 1)
    elif str(reaction.emoji) == "⚰️":
        await play(ctx, 'cerceuil.mp3', 1)
    elif str(reaction.emoji) == "🤷‍♂️":
        await play(ctx, 'squeezie.mp3', 1)
    elif str(reaction.emoji) == "🥯":
        await play(ctx, 'donut.mp3', 1)
    
    
client.run('MTEwNzY3OTU0MzU3NTE4NzUxNg.GkkglV.f-oT8CyiOk48r3tMG4-lHb6VhkN9D93panOoH8')
