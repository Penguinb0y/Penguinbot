from discord.ext import commands
import random


bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('ZAZAZAZAZAZAZAZA')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.event
async def change_presence(ctx):
    game = discord.game("sipping boba")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print("Logged in as" + bot.user.name)


bot.run(TOKEN)
