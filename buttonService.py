token = 'ODU2NzEwNjM4NzAwOTg2Mzc5.YNE_9Q.lbu6ObaKOkXNd1PmITqJqBXxI9M'
import nextcord
from time import sleep as wait # lol don't ask
from nextcord.ext import menus
from nextcord.ext import commands


bot = commands.Bot(command_prefix='-')
client = nextcord.Client()


class ReportUserMenu(menus.ButtonMenu):
    def __init__(self):
        super().__init__(disable_buttons_after=True)

    async def send_initial_message(self, ctx, channel):
        return await channel.send(f'Hello {ctx.author}', view=self)

    @nextcord.ui.button(emoji="\N{THUMBS UP SIGN}")
    async def on_thumbs_up(self, button, interaction):
        await self.message.edit(content=f"Thanks {interaction.user}!")


@bot.event
async def on_ready():
    channel = bot.get_channel(857361620601929748) # channel where I want to ticket-creation message to auto send
    await channel.send('"**Minecraft Account Scam Database**\n\nPress **Report User** or **Lookup User** to get started!"', view=ReportUserMenu())


bot.run(token)