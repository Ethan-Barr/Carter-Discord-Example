from discord.ext import commands
import discord
import json
import os
import KeepAlive

with open('config.json', 'r') as f:
    config = json.load(f)
token = config['token']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or(">>"), intents=intents)


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency: {round(client.latency * 1000)}ms")


@client.command(aliases=['c', 'purge', 'p'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No Reason Provided"):
    await ctx.send(member.name + " has been from banned the server for " + reason)
    await member.ban(reason=reason)


print(f"Token: {token}")
client.run(token)

# Need to edit the KeepAlive to make the page say when the bot is online
KeepAlive.KeepAlive()
