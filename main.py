# -- Welcome to The Land of the Shitty code ™ -- #

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

# -- Thus the code begins -- #


class ReportUserMenu(menus.ButtonMenu):
    def __init__(self):
        super().__init__(disable_buttons_after=True)

    async def send_initial_message(self, ctx, channel):
        return await channel.send(f'Hello {ctx.author}', view=self)

    @nextcord.ui.button(emoji="\N{THUMBS UP SIGN}")
    async def on_thumbs_up(self, button, interaction):
        await self.message.edit(content=f"Thanks {interaction.user}!")




@client.event
async def on_ready():
    
    print('[LOG] Bot has started!')
    try:
        await sessionService.create_database()
    except:
        print('Table already created')

    channel = client.get_channel(int(config.getReportChannel()))
    await channel.send('**Minecraft Account Scam Database**\n\nPress **Report User** or **Lookup User** to get started!', view=ReportUserMenu())
    


client.run(config.getToken())


