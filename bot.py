import  random
import discord
from discord.ext.commands import Bot
BOT_PREFIX = "/"
client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def roasts():
    choices = [
     "You have some egg head shape",
     "The top of your head is a dome",
     "You need to fix that head shape of yours",
     "Your unseasoned",
     "You have the default ghanaian head shape",
     "Your lips are drier then the sahara",
     "Your knees are ashier then the skin of kfc chicken",
     "What is {0.author.mention}, that name is so unoriginal",
     "When i saw your head ,I realised a new 3d polygon had been discovered",
     "When someone tried to replicate your head in blender an error came up: triangle limit exceded ",
     "Dead trim, nuff said",
     "I can see my self in that glistening forehead",
     "It's a waste of time trying to cuss something so irrelevant",
     "Nooooob"
    ]
    await client.say(random.choice(choices))


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))


@client.command()
async def version():
    await client.say("Elemental Soul Bot v.01 by >Fire.Exe")


@client.command()
async def add(left : int, right : int):
    await client.say(left + right)


@client.command()
async def divide(left : int, right : int):
    await client.say(left / right)


@client.command()
async def multiply(left : int, right : int):
    await client.say(left * right)


@client.command()
async def subtract(left: int, right: int):
        await client.say(left - right)


@client.command()
async def square(num : int):
    await client.say(num*num)

client.run(TOKEN)
