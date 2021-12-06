# -- Welcome to The Land of the Shitty code ™ -- #

# -- IMPORTS -- #
import nextcord
from time import sleep as wait # lol don't ask
import sqlite3
from config import config as config
import sessionService

# -- GLOBALS -- #
global playerarray
playerarray = []

# -- MISC -- #
client = nextcord.Client()
con = sqlite3.connect('reportdb.db')
cur = con.cursor()

# -- Thus the code begins -- #

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    await message.channel.send('Hello')
    

async def p1(authorid, channelid):
    client.get_channel(int(channelid)).send("What is the name of **Minecraft Name** used to scam you?")




@client.event
async def on_ready():
    print('[LOG] Bot has started!')
    try:
        await sessionService.create_database()
    except:
        print('Table already created')



client.run(config.getToken())