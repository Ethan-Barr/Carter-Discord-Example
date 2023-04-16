import requests
import time
import json
import os

import nextcord
from nextcord.ext import commands

from Utils.secret import prefix, token, carterAPI, name
from Utils.Carter import CarterSend


intents = nextcord.Intents.default()

intents.message_content = True
activity = nextcord.Activity(
    type=nextcord.ActivityType.listening, name=f"{prefix} help"
)

bot = commands.Bot(
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
    print(f"{bot.user.name} has connected to Discord!    \n")

@bot.event
async def on_message(message):
    user = message.author
    sentence = str(message.content)
    sentence = sentence.lower()

    if name in sentence:
        CarterSend(sentence, user.id)
        with open('CarterResponse.txt') as f:
            ResponseOutput = f.read()
    
        print(message.content)
        await message.channel.send(f"{ResponseOutput}")
        print(ResponseOutput)
        os.remove("CarterResponse.txt")
    
    else:
        pass



# Run Discord bot
bot.run(token)