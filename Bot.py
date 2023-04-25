import nextcord
from nextcord.ext import commands

import os

from config import *
from carter import *

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix=Prefix, intents=intents)

# handle ban command
@client.command()
async def ban(ctx, member: nextcord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned.')

# handle kick command
@client.command()
async def kick(ctx, member: nextcord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been kicked.')

# handle mute command
@client.command()
async def mute(ctx, member: nextcord.Member):
    role = nextcord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f'{member} has been muted.')

# handle unmute command
@client.command()
async def unmute(ctx, member: nextcord.Member):
    role = nextcord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f'{member} has been unmuted.')

# handle on_message event
@client.event
async def on_message(message: nextcord.Message):

    if message.author == client.user:
        return

    sentence = message.content.lower()
    User = message.author
    WakeWord = UIName[1:]

    if Prefix in sentence:

        sentence = sentence.replace(Prefix, "")
        # handle ban command
        if "ban" in sentence:
            if message.author.guild_permissions.administrator:
                try:
                    member = message.mentions[0]
                    await member.ban()
                    await message.channel.send(f'{member} has been banned.')
                except:
                    await message.channel.send('Please mention a valid member.')

                    # handle kick command
        elif "kick" in sentence:
            if message.author.guild_permissions.administrator:
                try:
                    member = message.mentions[0]
                    await member.kick()
                    await message.channel.send(f'{member} has been kicked.')
                except:
                    await message.channel.send('Please mention a valid member.')

                    # handle mute command
        elif "mute" in sentence:
            if message.author.guild_permissions.administrator:
                try:
                    member = message.mentions[0]
                    role = nextcord.utils.get(message.guild.roles, name="Muted")
                    await member.add_roles(role)
                    await message.channel.send(f'{member} has been muted.')
                except:
                    await message.channel.send('Please mention a valid member.')

        # handle unmute command
        elif "unmute" in sentence:
            if message.author.guild_permissions.administrator:
                try:
                    member = message.mentions[0]
                    role = nextcord.utils.get(message.guild.roles, name="Muted")
                    await member.remove_roles(role)
                    await message.channel.send(f'{member} has been unmuted.')
                except:
                    await message.channel.send('Please mention a valid member.')

        elif "clear" in sentence:
            if message.author.guild_permissions.administrator:
                amount = sentence.replace("clear ", "")
                messageamount = int(amount)
                channel = message.channel
                messages = []
                await channel.purge(limit=messageamount)
                ResponseOutput = (f"{messageamount} messages deleted. I was authorised to do so by {User}.")
                await channel.send(ResponseOutput)

    elif WakeWord in sentence: # Use this code if you want to add some form of chatbot interface.
            SendToCarter(sentence, User, APIkey)
            with open('ResponseOutput.txt') as f:
                ResponseOutput = f.read()

            print(message.content)
            await message.channel.send(f"{ResponseOutput}")
            print(ResponseOutput)
            os.remove("ResponseOutput.txt")

    else:
        pass

# run bot
client.run(DiscordAPI)