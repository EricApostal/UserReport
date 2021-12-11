# -- Welcome to The Land of the Shitty code ™ -- # 
# todo: interaction.response.??? member maybe?

# -- IMPORTS -- #
import nextcord
from time import sleep as wait # lol don't ask
import sqlite3
from config import config as config
import sessionService
from nextcord.ext import menus
from nextcord.ext import commands

# -- GLOBALS -- #


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

# async def menuGen(interaction, pg):
#   print('Generating menu', pg)
#   intmessage = await interaction.response.send_message(content= 'Are you sure you would like to report a user?', ephemeral=True, view=)


#-- MENU LIBRARIES (sorta) --#
# -- GENERIC CANCEL BUTTON --#
class cancelbutton(menus.ButtonMenu):
  @nextcord.ui.button (style = colors.green, label="Cancel")
  async def on_cancel(self, button, interaction):
      print('operation canceled')
      return 
      

#-- MENU ONE --#
class reportConfirm(menus.ButtonMenu): # just the first button menu
  def __init__(self):
      super().__init__(disable_buttons_after=True)

  @nextcord.ui.button (style = colors.green, label="Yes!")
  async def on_confirm_create_ticket(self, button, interaction):
    await interaction.response.send_message(content= 'What is the **Minecraft Name** of the user you would like to report?', ephemeral=True, view=typeMinecraftName()) #HERE
    user_data = sessionService.cdata('none', 'none','none')
    print(interaction.user.id)

    await sessionService.start_session(str(interaction.user.id), 'report', '1', user_data)
      
      # channel = await interaction.create_text_channel('cool-channel') 
      # await channel.edit(name=interaction.response.author.id)

  @nextcord.ui.button (style = colors.red, label="Oops!, nvm")
  async def on_deny_create_ticket(self, button, interaction):
      return   

#-- MENU TWO --#
class typeMinecraftName(menus.ButtonMenu): # just the first button menu
  def __init__(self):
      super().__init__(disable_buttons_after=True)

  @nextcord.ui.button (style = colors.red, label="Cancel")
  async def on_cancel(self, button, interaction):
      print(interaction)
      return # THIS NEEDS TO DO SOMETHING THANKS


class ReportUserMenu(menus.ButtonMenu):
    def __init__(self):
        super().__init__(disable_buttons_after=True)

    @nextcord.ui.button (style = colors.red, label="Report User")
    async def on_report_user(self, button, interaction):
      await interaction.response.send_message(content= 'Are you sure you would like to report a user?', ephemeral=True, view=reportConfirm())


    @nextcord.ui.button (style = colors.blue, label="Lookup User")
    async def on_lookup_user(self, button, interaction):
        return

@client.event
async def on_message(message):
  print('message sent')
  if message.author == client.user:
    return

  if await sessionService.getsessiondata(str(message.author.id)):
    userdata = await sessionService.getsessiondata(str(message.author.id))
    print(f'User found: {userdata}')
  else:
    print('Message found from user not in array')

@client.event
async def on_ready():
    
    print('[BOT] Bot has started!')
    try:
        await sessionService.create_database()
    except:
        print('[SQL] Table already created')

    channel = client.get_channel(int(config.getReportChannel()))
    await channel.purge()
    await channel.send('**Minecraft Account Scam Database**\n\nPress **Report User** or **Lookup User** to get started!', view=ReportUserMenu())
    


client.run(config.getToken())


