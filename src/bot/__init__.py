from nextcord.ext.commands import Bot
from nextcord import Intents
from dotenv import load_dotenv
import os

TESTING_GUILD_ID = 1071277811681218621

class DiscordBot(Bot):
    def __init__(self):
        super().__init__(command_prefix = "$", case_insensitive = True, intents=Intents.all())

    def run(self):
        load_dotenv("token.env")
        super().run(token = os.getenv("TOKEN"))
        
    async def on_ready(self):
        self.NAME = "Mansoor"
                    
        print(f"Logged in as {self.user.name}#{self.user.discriminator}")
        print(f"ID: {self.user.id}")
        print(f"Servers: {str(len(self.guilds))}")

bot = DiscordBot()
