import nextcord
from nextcord.ext import commands

import os

from config import *
from carter import *

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix=Prefix, intents=intents)


# On startup
@client.event
async def on_ready():
    print(f"{UIName} | Operational")


@client.event
async def on_message(message: nextcord.Message):
    if message.author == client.user:
        return

    # Remove these 2 lines if you dont want this function - This function will mute a user/bot on discord by changing the userID in ""
    if message.author.id == 1087420744809582692:
        return

    sentence = message.content.lower()
    User = message.author
    WakeWord = UIName[1:]


    if Prefix in sentence:
        sentence = sentence.replace(Prefix, "")

        # Handles Ban command - Member need Ban permission on there role
        if "ban" in sentence:
            if message.author.guild_permissions.ban_members:
                try:
                    member = message.mentions[0]
                    await member.ban()
                    await message.channel.send(f'{member} has been banned.')
                except:
                    await message.channel.send('Please mention a valid member.')

        # Handles Kick command - Member need Kick members permission on there role
        elif "kick" in sentence:
            if message.author.guild_permissions.kick_members:
                try:
                    member = message.mentions[0]
                    await member.kick()
                    await message.channel.send(f'{member} has been kicked.')
                except:
                    await message.channel.send('Please mention a valid member.')

        # Handles mute command - Member need manage roles permission on there role
        elif "mute" in sentence:
            if message.author.guild_permissions.manage_roles:
                try:
                    member = message.mentions[0]
                    role = nextcord.utils.get(
                        message.guild.roles, name="Muted")
                    await member.add_roles(role)
                    await message.channel.send(f'{member} has been muted.')
                except:
                    await message.channel.send('Please mention a valid member.')

        # Handles unmute command - Member need manage roles permission on there role
        elif "unmute" in sentence:
            if message.author.guild_permissions.manage_roles:
                try:
                    member = message.mentions[0]
                    role = nextcord.utils.get(
                        message.guild.roles, name="Muted")
                    await member.remove_roles(role)
                    await message.channel.send(f'{member} has been unmuted.')
                except:
                    await message.channel.send('Please mention a valid member.')

        # Handles clear command - Member need manage messages permission on there role
        elif "clear" in sentence:
            if message.author.guild_permissions.manage_messages:
                amount = sentence.replace("clear ", "")
                messageamount = int(amount)
                channel = message.channel
                messages = []
                await channel.purge(limit=messageamount)
                ResponseOutput = (
                    f"{messageamount} messages deleted. I was authorised to do so by {User} in channel {channel}")
                await channel.send(ResponseOutput)

    # CarterAPI if commands is not found
    # Use this code if you want to add some form of chatbot interface.
    elif WakeWord in sentence:
        await message.channel.trigger_typing()
        SendToCarter(sentence, User, APIkey)
        with open('ResponseOutput.txt') as f:
            ResponseOutput = f.read()
        await message.channel.send(f"{ResponseOutput}")
        # print(message.content)
        # print(ResponseOutput)
        os.remove("ResponseOutput.txt")
    else:
        pass

# run bot
client.run(DiscordAPI)
