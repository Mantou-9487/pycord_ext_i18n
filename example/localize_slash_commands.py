from discord import ApplicationContext
from discord.ext import commands

from pycord_ext_i18n import I18n

i18n = I18n()

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @i18n.localize_slash_command()
    async def test(self, ctx: ApplicationContext):
        await ctx.response.send_message(content=f"My command name is {ctx.command.name}!")

def setup(bot):
    bot.add_cog(ExampleCog(bot))