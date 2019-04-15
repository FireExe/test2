import os, discord, random, datetime, time, asyncio, json
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")
spam = []
# this is an event which is triggered when something happens in Discord 
# in this case on_ready() is called when the bot logs on
#you can checkthe Discord API Documentaion for more event Functions 
# here: https://discordapp.com/developers
os.chdir = (r"C:\Users\Toshiba pc\PycharmProjects\bots")
async def status_task():
 while True:
  now = datetime.datetime.now()
  await asyncio.sleep(1)
  server = discord.utils.get(client.guilds, name='Bot making')
  x = server.members
  with open("users.json", "r+") as f:
   users = json.load(f)
   for member in x:
        await update_data(users, member, server)
        if  int(users[str(member.id) + "-" + str(server.id)]["Lastrob"]) !=  int(1) and int(users[str(member.id) + "-" + str(server.id)]["Lastrob"]) != 60:
         users[str(member.id) + "-" + str(server.id)]["Lastrob"] += 1
         with open("users.json", "r+") as f:
          json.dump(users, f)
        elif int(users[str(member.id) + "-" + str(server.id)]["Lastrob"]) ==  int(60):
           users[str(member.id) + "-" + str(server.id)]["Lastrob"] = 1
           with open("users.json", "r+") as f:
            json.dump(users, f)

@client.event
async def on_ready():
    activity = discord.Game(name="B-tech ES Bot")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(status_task())


async def update_data(users, user, server):
    if not str(user.id) + "-" + str(server.id) in users:
        users[str(user.id) + "-" + str(server.id)] = {}
        users[str(user.id) + "-" + str(server.id)]["money"] = 100
        users[str(user.id) + "-" + str(server.id)]["strikes"] = 0
        users[str(user.id) + "-" + str(server.id)]["Lastrob"] = 1
        users[str(user.id) + "-" + str(server.id)]["experience"] = 0
        users[str(user.id) + "-" + str(server.id)]["level"] = 1


async def add_money(users, user, exp, server):
        now = datetime.datetime.now()
        users[str(user.id) + "-" + str(server.id)]["money"] += exp
        users[str(user.id) + "-" + str(server.id)]["Lastrob"] = 2




@client.command()
async def write(ctx):        
   with open("Users","a") as file:
     file.write("some text")
     file.close()
     print("done")
          
@client.command()
async def read(ctx):        
   with open("Users","r") as file:
     print(file.read())
        
@client.command()
async def bal(ctx):
   with open("users.json", "r") as f:
    users = json.load(f)
    user = ctx.message.author
    server = ctx.message.guild
    await update_data(users, ctx.message.author, ctx.message.guild)
    await ctx.send(str(users[str(user.id) + "-" + str(server.id)]["money"]))
    for line in f:
     print(line)
  

            
async def add_experience(users, user, exp, server):
    users[str(user.id) + "-" + str(server.id)]["experience"] += exp

async def level_up(users, user, channel, server):
    experience = users[str(user.id) + "-" + str(server.id)]["experience"]
    lvl_start = users[str(user.id) + "-" + str(server.id)]["level"]
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await channel.send(f":tada: Congrats {user.mention}, you levelled up to level {lvl_end}!")
        users[str(user.id) + "-" + str(server.id)]["level"] = lvl_end


@client.event
async def on_message(message):
    with open("users.json", "r+") as f:
        users = json.load(f)
        if message.author.id == client.user.id:
            return
        else:
            await update_data(users, message.author,message.guild)
            number = random.randint(5,10)
            await add_experience(users, message.author, number, message.guild)
            await level_up(users, message.author, message.channel, message.guild)
            with open("users.json", "r+") as f:
             json.dump(users, f)
    await client.process_commands(message)
    
@client.event
async def on_message(message):
    print(message.content)
    await client.process_commands(message)
    global spam
    if not str(user.id) + "-" + str(server.id) in spam:
     spam[str(user.id) + "-" + str(server.id)]["Spam"] = 1
     spam[str(user.id) + "-" + str(server.id)]["Spam1"] = message.content
     spam[str(user.id) + "-" + str(server.id)]["Spam2"] = "Empty"
     spam[str(user.id) + "-" + str(server.id)]["Spam3"] = "Empty"
    else:
      spam[str(user.id) + "-" + str(server.id)] = spam[str(user.id) + "-" + str(server.id)] + 1 
      if spam[str(user.id) + "-" + str(server.id)]["Spam2"] == "Empty" and message.content == spam[str(user.id) + "-" + str(server.id)]["Spam1"]:
          spam[str(user.id) + "-" + str(server.id)]["Spam2"] = message.content
      elseif spam[str(user.id) + "-" + str(server.id)]["Spam3"] == "Empty" and message.content == spam[str(user.id) + "-" + str(server.id)]["Spam1"]:
          spam[str(user.id) + "-" + str(server.id)]["Spam3"] = message.content 
      elsif spam[str(user.id) + "-" + str(server.id)]["Spam3"] != "Empty":
        await message.channel.send("Test")          

    if message.content.startswith("https://discord.gg/"):
        if message.author.guild_permissions.kick_members:
            print("Working")
        else:
            await message.delete()
             




client.run(TOKEN)



    
