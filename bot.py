import os, discord, random, datetime, time, asyncio
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")
# this is an event which is triggered when something happens in Discord 
# in this case on_ready() is called when the bot logs on
#you can checkthe Discord API Documentaion for more event Functions 
# here: https://discordapp.com/developers
QOTD = "None"

async def status_task():
    while True:
        now = datetime.datetime.now()
        await asyncio.sleep(10)
        if now.hour == 11 and now.minute == 45:
         global QOTD 
         if QOTD != "None":  
          server = discord.utils.get(client.guilds, name='Elemental Soul')
          role = discord.utils.get(server.roles, name="QOTDping")
          channel = discord.utils.get(server.channels, name="qotd")
          await channel.send(str(role.mention)+QOTD)
          QOTD = "None"
        

@client.event
async def on_ready():
    activity = discord.Game(name="Elemental Soul | /help")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(status_task())
    
    
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
        elif left  == "QOTDping":
          await ctx.send("You will now receive QOTD pings " + str( user.name))
          await user.add_roles(role)
            
     
@client.command(pass_content=True)
async def unassign(ctx, left: str):
        user = ctx.message.author
        server = ctx.message.guild
        role = discord.utils.get(server.roles, name=left)
        if left  == "Nopartnerpings":
          await ctx.send("You will now recieve partner pings " + str( user.name))
          await user.remove_roles(role)
        elif left  == "QOTDping":
          await ctx.send("You will no longer receive QOTD pings " + str( user.name))
          await user.remove_roles(role)
      
    
@client.command(name="kick",
                description="'Kick a member'    'Usage:/kick[member]'     'Example:/kick dJnokia'",
                brief="'Usage:/kick[member]'",
                pass_content=True)
async def kick(ctx, user: discord.Member):
        if ctx.message.author.guild_permissions.kick_members:
         await ctx.send(str(user.name)+" has been kicked")
         await user.kick()
            
@client.command(pass_content=True)      
async def qotd(ctx, *, qotd):
        if ctx.message.author.guild_permissions.ban_members:
         user = ctx.message.author
         await ctx.send(str(user.name)+" has set the qotd to "+qotd)
         global QOTD 
         QOTD = qotd
        
@client.command(pass_content=True)
async def ban(ctx, user: discord.Member):
        if ctx.message.author.guild_permissions.ban_members:
         await ctx.send(str(user.name)+" has been banned")
         await user.ban()
        
        
@client.command(pass_content=True)
async def help(ctx):
 embed = discord.Embed(
        colour = discord.Colour.orange()
 )
  
 embed.set_author(name="Help")
 embed.add_field(name="/help", value="Shows this message",inline=False)
 embed.add_field(name="/roasts", value="Get roasted",inline=False)
 embed.add_field(name="/version", value="Checks my version",inline=False)
 embed.add_field(name="/assign", value="Give yourself a role",inline=False)
 embed.add_field(name="Example:", value="/assign QOTDping",inline=True)
 embed.add_field(name="/unassign", value="Remove a role from yourself",inline=True)
 embed.add_field(name="Example:", value="/unassign QOTDping",inline=False)
 embed.add_field(name="/membercount", value="Shows the amount of people in the server",inline=True)
 embed.add_field(name="/kick", value="Kick a user",inline=False)
 embed.add_field(name="Example:", value="/kick YourDad",inline=False)
 embed.add_field(name="/ban", value="Ban a user",inline=False)
 embed.add_field(name="Example:", value="/ban YourDad",inline=False)
 await ctx.send("Here's all the commands and their uses:", embed=embed)
        
    
@client.command(pass_content=True)
async def membercount(ctx):
 embed = discord.Embed(
        colour = discord.Colour.orange()
 )
 x = ctx.guild.members
 num = 0
 for member in x:
    num = num + 1
 embed.set_author(name=" ")
 embed.add_field(name="Users: ", value=num,inline=False)
 await ctx.send(" ", embed=embed)
    
        
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    role = discord.utils.get(member.guild.roles, name="QOTDping")
    await channel.send("Welcome to Elemental Soul "+str(member.mention)+" Make sure to read rules, faqs if you have any questions and important-links for the group")
    await member.add_roles(role)
    
   
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send("Bye "+str(member.name)+" We hope to see you back at Elemental Soul soon!")
    

client.run(TOKEN)



    
