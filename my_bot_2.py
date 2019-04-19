import random

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "$")
TOKEN = "ULTRA SECRET TOKEN"

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}!!!""")

@client.command(name='8ball', 
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                ctx)
async def eight_ball():
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Nah fam not even close',
    ]
    await client.say(random.choice(possible_responses))

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="sipping boba"))
    print ("Logged in as" + client.user.name)

@client.event
async def on_message(message):
    id = client.get_guild(464209055485919242)

    if message.content.find("?hello") != -1:
        await message.channel.send("Hi!")
    elif message.content == "?users":
        await message.channel.send(f"""# number of Members: {id.member_count} """)

client.run(TOKEN)
