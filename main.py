# -- Welcome to The Land of the Shitty code ™ -- #

# -- IMPORTS -- #
import nextcord
from time import sleep as wait # lol don't ask
import sqlite3

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
    

async def start_session(dcid, mode, step, data):
    playerarray.append([dcid, mode, step, data])
    print(f'Args = {dcid, mode, step, data}')

    print(f'playerarray = {playerarray}')


async def find_session_data(dcid):
    print(f"in-context player array = {playerarray}")
    for i,k in enumerate(playerarray):
        if str(k[0]) == str(dcid): #k[0] should be the dcid (discord id)
            return k
    return False


async def p1(authorid, channelid):
    client.get_channel(int(channelid)).send("What is the name of **Minecraft Name** used to scam you?")


async def create_database():
    cur.execute('''CREATE TABLE users
                (minecraftname text, discordid text, reporterid text, reportreason text, proof text)''')

async def add_user(minecraftname, discordid, reporterid, reportreason, proof):
    cur.execute(f"INSERT INTO users VALUES ('{minecraftname}','{discordid}','{reporterid}','{reportreason}','{proof}')")
    con.commit()
    con.close()   


@client.event
async def on_ready():
    print('[LOG] Bot has started!')
    try:
        await create_database()
    except:
        print('Table already created')


client.run('ODU2NzEwNjM4NzAwOTg2Mzc5.YNE_9Q.lbu6ObaKOkXNd1PmITqJqBXxI9M')