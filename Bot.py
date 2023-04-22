from termcolor import colored
import requests
import time
import json
import os

import nextcord
from nextcord.ext import commands


with open('config.json', 'r') as f:
    data = json.load(f)


intents = nextcord.Intents.default()
intents.message_content = True

activity = nextcord.Activity(
    type=nextcord.ActivityType.listening, name=f">>help"
)

client = commands.Bot(
    intents=intents,
    activity=activity,
    command_prefix='?'  # set the command prefix here
)


# Load all cogs in the "cogs" directory
for folder in os.listdir("cogs"):
    if folder.endswith(".py"):
        client.load_extension(f"cogs.{folder[:-3]}")
        print('loaded')


@client.listen() # Start up
async def on_ready():
    print(f"{client.user.name} has connected to Discord!    \n")

@client.event
async def on_message(message):
    if 'jarvis' in message.content.lower():
        response = requests.post("https://api.carterlabs.ai/chat", headers={
            "Content-Type": "application/json"
        }, data=json.dumps({
            "text": message.content,
            "key": data["carterKey"],
            "playerId": message.author.id
        }))
        response_data = response.json()['output']['text']
        print(response_data)
        await message.channel.send(response_data)

        pass

    @client.command()
    async def yest(ctx):
        await ctx.send("Hello, world!")

# Run the bot
client.run(data["token"])
