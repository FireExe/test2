import os, discord, random, datetime, time, asyncio, json
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")
spam = []

@client.event
async def on_ready():
    activity = discord.Game(name="B-tech ES Bot")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


    
@client.event
async def on_message(message):
    print(message.content)
    await client.process_commands(message)
    global spam
    user = message.author
    server = message.guild
    if not str(user.id) + "-" + str(server.id) in spam:
     spam[str(user.id) + "-" + str(server.id)][int(1)] = 1
     spam[str(user.id) + "-" + str(server.id)][2] = message.content
     spam[str(user.id) + "-" + str(server.id)][3] = "Empty"
     spam[str(user.id) + "-" + str(server.id)][4] = "Empty"
    else:
      spam[str(user.id) + "-" + str(server.id)] = spam[str(user.id) + "-" + str(server.id)] + 1 
      if spam[str(user.id) + "-" + str(server.id)][3] == "Empty" and message.content == spam[str(user.id) + "-" + str(server.id)][2]:
          spam[str(user.id) + "-" + str(server.id)][3] = message.content
      elif spam[str(user.id) + "-" + str(server.id)][4] == "Empty" and message.content == spam[str(user.id) + "-" + str(server.id)][2]:
          spam[str(user.id) + "-" + str(server.id)][4] = message.content 
      elif spam[str(user.id) + "-" + str(server.id)][4] != "Empty":
        await message.channel.send("Test")          
    if message.content.startswith("https://discord.gg/"):
        if message.author.guild_permissions.kick_members:
            print("Working")
        else:
            await message.delete()
             




client.run(TOKEN)



    
