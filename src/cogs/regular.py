import nextcord
from nextcord.ext import commands



TESTING_GUILD_ID = 1071277811681218621  # Replace with your testing guild id


class Regular(commands.Cog):
    """Contains all the regular commands that come with a bot"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="ping",
                            description="Test your ping!",
                            guild_ids=[TESTING_GUILD_ID])
    async def _ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Pong! {0}".format(round(self.bot.latency, 1)))

    @nextcord.slash_command(name="say",
                            description="Make the bot say something!",
                            guild_ids=[TESTING_GUILD_ID])
    async def _say(self, interaction: nextcord.Interaction, message):
        await interaction.send(message)            
        


def setup(bot):
    bot.add_cog(Regular(bot))
