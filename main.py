import os
import sys
import json
import time
import nextcord
from nextcord.ext import commands

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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
        help_command=None
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


class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Detected modification in {event.src_path}. Restarting bot...")
        time.sleep(1)
        os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == "__main__":
    event_handler = FileModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        main()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()