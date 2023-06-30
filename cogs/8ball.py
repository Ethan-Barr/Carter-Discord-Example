import asyncio
import json
import os
import requests
import random

import nextcord
from nextcord.ext import commands

class _8Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, query=None):

        if query == None:
            embed = discord.Embed(
                title = "Magic 8Ball",
                description = "You have to ask a question!",
                color = discord.Color.red()
            )
            embed.set_footer(text="© sotus network co founder djmachette PROJECT AUTISM 2023")

            await ctx.send(embed=embed)

        else:
            responses = [
                "Yes.",
                "No.",
                "Maybe.",
                "Probably.",
                "It is uncertain.",
                "Ask another time.",
                "I rather not get too political.",
                "What are you, gay?."
            ]

            index = random.randint(0, len(responses))

            embed = discord.Embed(
                title = "Magic 8Ball",
                description = responses[index],
                color = discord.Color.green()
            )
            embed.set_footer(text="© sotus network co founder djmachette PROJECT AUTISM 2023")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(_8Ball(client))
