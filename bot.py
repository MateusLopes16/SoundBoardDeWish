import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.command()
async def btn(ctx):
    channel = ctx.author.voice.channel
    message = await ctx.send("Choose a song to play:")
    await message.add_reaction("🎵")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == "🎵"

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
    except TimeoutError:
        await ctx.send("No song selected within 30 seconds.")
        return

    if str(reaction.emoji) == "🎵":
        await ctx.send(f"Now playing the song you selected in {channel.name}")


bot.run('MTEwNzY3OTU0MzU3NTE4NzUxNg.GkkglV.f-oT8CyiOk48r3tMG4-lHb6VhkN9D93panOoH8')
