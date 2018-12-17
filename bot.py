import os, discord, random, datetime, time, asyncio, json
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
os.chdir = (r"C:\Users\Toshiba pc\PycharmProjects\bots")

async def update_data(users, user, server):
    if not str(user.id) + "-" + str(server.id) in users:
        users[str(user.id) + "-" + str(server.id)] = {}
        users[str(user.id) + "-" + str(server.id)]["money"] = 100
        users[str(user.id) + "-" + str(server.id)]["strikes"] = 0
        users[str(user.id) + "-" + str(server.id)]["Lastrob"] = 0


async def add_experience(users, user, exp, server):
        now = datetime.datetime.now()
        users[str(user.id) + "-" + str(server.id)]["money"] += exp
        users[str(user.id) + "-" + str(server.id)]["Lastrob"] = now.minute


@client.command()
async def rob(ctx):
    now = datetime.datetime.now()
    with open("users.json", "r") as f:
        users = json.load(f)
        user = ctx.message.author
        server = ctx.message.guild
        if  int(users[str(user.id) + "-" + str(server.id)]["Lastrob"]) != now.minute:
         number = random.randint(20, 100)
         await ctx.send("You rob a bank and earn £"+str(number))
         await update_data(users, ctx.message.author, ctx.message.guild)
         await add_experience(users, ctx.message.author, int(number), ctx.message.guild)
         with open("users.json", "w") as f:
          json.dump(users, f)
        else:
          await ctx.send("You have 1 minute until you can rob again")
    
@client.command()
async def bal(ctx):
   with open("users.json", "r") as f:
    users = json.load(f)
    user = ctx.message.author
    server = ctx.message.guild
    await update_data(users, ctx.message.author, ctx.message.guild)
    await ctx.send(str(users[str(user.id) + "-" + str(server.id)]["money"]))






client.run(TOKEN)



    
