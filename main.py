# -- Welcome to The Land of the Shitty code ™ -- # python3 -m pip install -U nextcord-ext-menus

# -- IMPORTS -- #
import nextcord
from time import sleep as wait # lol don't ask
import sqlite3
from config import config as config
import sessionService
from nextcord.ext import menus
from nextcord.ext import commands

# -- GLOBALS -- #
global playerarray
playerarray = []

# -- MISC -- #
client = nextcord.Client()
con = sqlite3.connect('reportdb.db')
cur = con.cursor()
bot = commands.Bot(command_prefix='-')

class colors():
  def __init__(self, blue, red, green):
    self.blue = blue
    self.red = red
    self.green = green
  
  blue, grey, gray, green, red = 1,2,2,3,4





# -- Thus the code begins -- #

async def menuGen(message, pg):
  print('Generating menu', pg)

class ReportUserMenu(menus.ButtonMenu):
    def __init__(self):
        super().__init__(disable_buttons_after=True)

    
    @nextcord.ui.button (style = colors.red, label="Report User")
    async def on_report_user(self, button, interaction):
        await interaction.response.send_message(content= 'Are you sure you would like to report a user?', ephemeral=True)
        

    @nextcord.ui.button (style = colors.blue, label="Lookup User")
    async def on_lookup_user(self, button, interaction):
        return


@client.event
async def on_ready():
    
    print('[LOG] Bot has started!')
    try:
        await sessionService.create_database()
    except:
        print('Table already created')

    channel = client.get_channel(int(config.getReportChannel()))
    await channel.purge()
    await channel.send('**Minecraft Account Scam Database**\n\nPress **Report User** or **Lookup User** to get started!', view=ReportUserMenu())
    


client.run(config.getToken())


