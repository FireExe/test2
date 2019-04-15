import os, discord, random, datetime, time, asyncio, json
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")
spam = {}

async def status_task():
 while True:
  await asyncio.sleep(3)
  global spam
  server = discord.utils.get(client.guilds, name='Bot making')
  x = server.members
  for user in x:
   if not str(user.id) + "-" + str(server.id) in spam:
     spam[str(user.id) + "-" + str(server.id)] = {}
     spam[str(user.id) + "-" + str(server.id)]["Spam"] = []
     spam[str(user.id) + "-" + str(server.id)]["SpamLvl"] = 0
   else:
     spam[str(user.id) + "-" + str(server.id)]["SpamLvl"] = 0
     spam[str(user.id) + "-" + str(server.id)]["Spam"] = []

  

@client.event
async def on_ready():
    activity = discord.Game(name="B-tech ES Bot")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(status_task())


    
@client.event
async def on_message(message):
   print(message.content)
   await client.process_commands(message)
   if message.author.id != client.user.id:
    global spam
    user = message.author
    server = message.guild
    if not str(user.id) + "-" + str(server.id) in spam:
     spam[str(user.id) + "-" + str(server.id)] = {}
     spam[str(user.id) + "-" + str(server.id)]["Spam"] = []
     spam[str(user.id) + "-" + str(server.id)]["Spam"].append(message.content)
     spam[str(user.id) + "-" + str(server.id)]["SpamLvl"] = 0
    else:
      #spam[str(user.id) + "-" + str(server.id)]["Spam"] = spam[str(user.id) + "-" + str(server.id)]["Spam"] + 1 
      for spam in spam[str(user.id) + "-" + str(server.id)]["Spam"]:
       if spam == message.content:
        spam[str(user.id) + "-" + str(server.id)]["SpamLvl"] = spam[str(user.id) + "-" + str(server.id)]["SpamLvl"] + 1
        spam[str(user.id) + "-" + str(server.id)]["Spam"].append(message.content)
      if spam[str(user.id) + "-" + str(server.id)]["SpamLvl"] < 3:
         await message.channel.send("Stop the spam")
         mgs = []
         channel = message.channel
         async for x in bot.logs_from((channel), limit = int(3)):
          if x.author == message.author:
            mgs.append(x)
         await delete_messages(mgs)
    if message.content.startswith("https://discord.gg/"):
        if message.author.guild_permissions.kick_members:
            print("Working")
        else:
            await message.delete()
             




client.run(TOKEN)



    
