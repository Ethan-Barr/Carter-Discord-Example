from contextlib import contextmanager
import requests
import logging
import json
import time
import sys
import os

import nextcord
from nextcord.ext import commands

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import config

logging.basicConfig(filename="watchdog.log", level=logging.INFO)


# The Actual main file for Jarvis
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

    @bot.listen() # Start up
    async def on_ready():
        assert bot.user is not None
        print(f"{bot.user.name} has connected to Discord!")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            response = requests.post("https://api.carterlabs.ai/chat", headers={
                "content-Type": "application/json"
            },data=json.dumps({
                "text": ctx.message.content,
                "key": config.carterKey,
                "playerId": str(ctx.author.id)
            }))
            output_text = response.json()["output"]["text"]
            await ctx.send(output_text)
            print("Used Carter")
        else:
            raise error


    # Run Discord bot
    bot.run(config.token)



@contextmanager
def observe_file_changes(log_file_path):
    event_handler = FileModifiedHandler(log_file_path)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        yield
        while True:
            time.sleep(1)
            if event_handler.is_log_file_modified():
                logging.info(f"Detected modification in log file {log_file_path}. Ignoring...")
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# Restarting Bot on code update
class FileModifiedHandler(FileSystemEventHandler):
    def __init__(self, log_file_path):
        super().__init__()
        self.log_file_path = log_file_path
        self.log_file_modified_at = os.stat(log_file_path).st_mtime

    def on_modified(self, event):
        if event.src_path == self.log_file_path:
            # If the log file was modified, update the last modified time
            self.log_file_modified_at = os.stat(self.log_file_path).st_mtime
            logging.info(f"Detected modification in log file {event.src_path}. Ignoring...")
        else:
            logging.info(f"Detected modification in {event.src_path}. Restarting bot...")
            time.sleep(1)
            os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    with observe_file_changes("log.txt"):
        main()