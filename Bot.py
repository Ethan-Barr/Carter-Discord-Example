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


@client.event
async def on_message(message):
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

    await client.process_commands(message)


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency, 1)}ms")


@client.slash_command()
async def ping(interaction: nextcord.Interaction):
    """Simple command that responds with Pong!"""
    await interaction.response.send_message(f"Pong! {round(client.latency, 1)}ms")


@client.slash_command(
    name="github",
    description="Displays the link to the Nextcord source code"
)
async def github(ctx: nextcord.Interaction):
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
