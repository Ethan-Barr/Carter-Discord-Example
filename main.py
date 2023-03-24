import os
import json
import nextcord
from nextcord.ext import commands

import config


def main():
    intents = nextcord.Intents.default()
    intents.message_content = True

    activity = nextcord.Activity(
        type=nextcord.ActivityType.listening, name=f"{config.prefix}help"
    )

    bot = commands.Bot(
        commands.when_mentioned_or(config.prefix),
        intents=intents,
        activity=activity,
    )

    # Get the modules of all cogs whose directory structure is ./cogs/<module_name>
    for folder in os.listdir("cogs"):
        bot.load_extension(f"cogs.{folder}")

    @bot.listen()
    async def on_ready():
        assert bot.user is not None
        print(f"{bot.user.name} has connected to Discord!")

    # Run Discord bot
    bot.run(config.token)


if __name__ == "__main__":
    main()