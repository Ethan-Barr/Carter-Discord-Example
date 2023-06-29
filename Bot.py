from nextcord.ext import commands
import nextcord

import requests
import dotenv
import json
import os

dotenv.load_dotenv()

prefix = os.getenv("BOT_PREFIX")
token = os.getenv("DISCORD_TOKEN")
CarterAPI = os.getenv("CARTER_TOKEN")

UIName = "Jarvis"  # You can change this to anything you want

intents = nextcord.Intents.all()
# Change this to anything you want to display on your bots Activity
activity = nextcord.Activity(type=nextcord.ActivityType.watching, name="Iron Man movies")
client = commands.Bot(command_prefix=prefix, intents=intents, activity=activity)

client.remove_command("help")

# On startup
@client.event
async def on_ready():
    print(f"{UIName} | Operational")


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
    if message.author != client.user and not message.content.lower().startswith(prefix) and "jarvis" in message.content.lower():
        try:
            async with channel.typing():
                response = requests.post(
                    "https://api.carterlabs.ai/api/chat",
                    headers={
                        "Content-Type": "application/json"
                    },
                    data=json.dumps({
                        "text": message.content,
                        "key": CarterAPI,
                        "user_id": message.author.id
                    })
                )

                response_data = response.json()
                response_text = response_data['output']['text']
                await message.reply(response_text, mention_author=False)

        except Exception as err:
            await channel.send(f"There was an Error: {err}")


    # Only temporary!
    if isinstance(channel, nextcord.DMChannel) and message.author != client.user and not message.content.startswith(prefix):
        try:
            async with channel.typing():
                response = requests.post(
                    "https://api.carterlabs.ai/api/chat",
                    headers={
                        "Content-Type": "application/json"
                    },
                    data=json.dumps({
                        "text": message.content,
                        "key": CarterAPI,
                        "user_id": message.author.id
                    })
                )

                response_data = response.json()
                response_text = response_data['output']['text']
                await message.reply(response_text, mention_author=False)

        except Exception as err:
            await channel.send(f"There was an Error: {err}")

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