import os
from bot import bot
from utils import db


if __name__ == "__main__":
    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{cog[:-3]}")
                print("Loaded " + cog)
            except Exception as e:
                print("COG Error: " + e)
    db.build()
    bot.run()