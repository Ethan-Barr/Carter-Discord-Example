from nextcord.ext import commands
import nextcord

from carterpy import Carter
from CarterOffline import *

import requests
import dotenv
import json
import os


# Setup
dotenv.load_dotenv()

prefix = os.getenv("BOT_PREFIX")
token = os.getenv("DISCORD_TOKEN")
CarterAPI = os.getenv("CARTER_TOKEN")

UIName = 'jarvis'    # You can change this to anything you want

# Bot config
intents = nextcord.Intents.all()
# Change this to anything you want to display on your bots Activity
activity = nextcord.Activity(type=nextcord.ActivityType.watching, name="Iron Man movies")
client = commands.Bot(command_prefix=prefix, intents=intents, activity=activity)

client.remove_command("help")

intents_file_path = "intents.json"

# Carter-py setup

carterpy = Carter(CarterAPI)
carter = CarterOffline(intents_file_path, CarterAPI)

# On startup
@client.event
async def on_ready():
    print(f"{UIName} | Operational")


# Cog setup
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'`cogs.{extension}` was loaded.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'`cogs.{extension}` was unloaded. You can no longer use it until it is reloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel
    sentence = str(message.content)
    User = str(message.author)


    if message.author != client.user and not sentence.lower().startswith(prefix) and UIName in sentence.lower():
        try:
            async with channel.typing():
                try:
                    response = carter.SendToCarter(CarterAPI, sentence, User)
                except:
                    response = carterpy.say(sentence, User)
                await message.reply(response)

        except Exception as err:
            await message.reply(f"There was an Error: {err}")
            print(err)

    if message.reference:
        replied_to = await message.channel.fetch_message(message.reference.message_id)
        if replied_to.author == client.user:
            async with channel.typing():
                try:
                    response = carter.SendToCarter(CarterAPI, sentence, User)
                except:
                    response = carterpy.say(sentence, User)
                await message.reply(response)

    # Only temporary!
    if isinstance(channel, nextcord.DMChannel) and message.author != client.user and not message.content.startswith(prefix):
        try:
            async with channel.typing():
                try:
                    response = carter.SendToCarter(CarterAPI, sentence, User)
                except:
                    response = carterpy.say(sentence, User)
                await message.reply(response)

        except Exception as err:
            await message.reply(f"There was an Error: {err}")

    await client.process_commands(message)


@client.slash_command()
async def github(ctx: nextcord.Interaction):
    """Displays the link to the Nextcord source code"""
    embed = nextcord.Embed(
        title="Github Repo",
        description="""Here is the github repo with the source code as a template!:
        https://github.com/Ethan-Barr/Carter-Discord-Example
            """,
        url="https://github.com/Ethan-Barr/Carter-Discord-Example",
        color=nextcord.Color.red()
    )
    embed.set_image(
        url="https://logos-world.net/wp-content/uploads/2020/11/GitHub-Logo.png")
    await ctx.send(embed=embed)


client.run(token)
