import requests
import json
import os

import nextcord
from nextcord.ext import commands

import Utils

intents = nextcord.Intents.default()

intents.message_content = True
activity = nextcord.Activity(
    type=nextcord.ActivityType.listening, name=f"{Utils.prefix}help"
)

bot = commands.Bot(
    commands.when_mentioned_or(Utils.prefix),
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
            "key": Utils.carterKey,
            "playerId": str(ctx.author.id)
        }))
        output_text = response.json()["output"]["text"]
        await ctx.send(output_text)
        print("Used Carter")
    else:
        raise 
    

# Run Discord bot
bot.run(Utils.token)