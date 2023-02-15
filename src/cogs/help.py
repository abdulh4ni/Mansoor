import nextcord
from nextcord.ext import commands
from nextcord import SlashOption
from typing import Optional


TESTING_GUILD_ID = 1071277811681218621  # Replace with your testing guild id


class Help(commands.Cog):
    """Contains help command"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="help",
                            guild_ids=[TESTING_GUILD_ID],
                            description="Sends the help command")
    async def _help(self, interaction: nextcord.Interaction,
                    section: Optional[str] = SlashOption(name="sections",
                                                         choices={"Help",
                                                                  "Regular"})):
        """Sends this help message"""
        if not section:
            em = nextcord.Embed(title="`Sections`",
                                color=nextcord.Color.purple(),
                                description="TIP: Use /help {section} to list commands inside a specific section!")  # noqa: E501
            cogDesc = ''
            for cog in self.bot.cogs:
                if cog == "Help":
                    pass
                else:
                    cogDesc += f'**{cog}** - {self.bot.cogs[cog].__doc__}\n'

            em.add_field(name="Sections", value=cogDesc, inline=False)

        elif section:
            em = nextcord.Embed(title=f"Section: {section} - Commands",
                                description=self.bot.cogs[section].__doc__,
                                color=nextcord.Color.purple())
            for command in self.bot.get_cog(section).application_commands:
                em.add_field(name=f"/{command.name}",
                             value=command.description, inline=False)

        await interaction.response.send_message(embed=em)


def setup(bot):
    bot.add_cog(Help(bot))