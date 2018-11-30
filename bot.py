import os, discord, random
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)

# this is an event which is triggered when something happens in Discord 
# in this case on_ready() is called when the bot logs on
#you can checkthe Discord API Documentaion for more event Functions 
# here: https://discordapp.com/developers

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    
# below this line you can put custom Functions
@client.command()
async def roasts(ctx):
    choices = [
     "You have some egg head shape",
     "The top of your head is a dome",
     "You need to fix that head shape of yours",
     "Your unseasoned",
     "You have the Rthro head shape",
     "Your lips are drier then the sahara",
     "Your knees are ashier then the skin of kfc chicken",
     "What is "+ctx.message.author.name+", that name is so unoriginal",
     "When i saw your head ,I realised a new 3d polygon had been discovered",
     "When someone tried to replicate your head in blender an error came up: triangle limit exceded ",
     "Dead trim, nuff said",
     "I can see my self in that glistening forehead",
     "It's a waste of time trying to cuss something so irrelevant",
     "Nooooob"
    ]
    await ctx.send(random.choice(choices))

    
@client.command()
async def version(ctx):
    await ctx.send("Elemental Soul Bot v.01 by >Fire.Exe")


@client.command()
async def add(ctx, left : int, right : int):
    await ctx.send(left + right)


@client.command()
async def divide(ctx, left : int, right : int):
    await ctx.send(left / right)


@client.command()
async def multiply(ctx, left : int, right : int):
    await ctx.send(left * right)


@client.command()
async def subtract(ctx, left: int, right: int):
        await ctx.send(left - right)


@client.command()
async def square(ctx, num : int):
    await ctx.send(num*num)
    
    
@client.command(pass_content=True)
async def assign(ctx, left: str):
        user = ctx.message.author
        server = ctx.message.guild
        role = discord.utils.get(server.roles, name=left)
        if left  == "Nopartnerpings":
          await ctx.send("You will no longer receive partner pings " + str( user.name))
          await user.add_roles(role)
            
     
@client.command(pass_content=True)
async def unassign(ctx, left: str):
        user = ctx.message.author
        server = ctx.message.guild
        role = discord.utils.get(server.roles, name=left)
        if left  == "Nopartnerpings":
          await ctx.send("You will now recieve partner pings " + str( user.name))
          await user.remove_roles(role)
         
        
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    role = discord.utils.get(member.guild.roles, name="Nopartnerpings")
    await channel.send("Welcome "+str(member.mention))
    await member.add_roles(role)

client.run(TOKEN)
