import nextcord
from nextcord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        # Calculate the bot's latency
        latency = round(self.bot.latency * 1000, 2)
        # Send the response
        await ctx.send(f'Pong! Latency: {latency} ms')

def setup(bot):
    bot.add_cog(PingCog(bot))
