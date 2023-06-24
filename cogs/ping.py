import nextcord
from nextcord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @nextcord.slash_command()
    async def ping(self, interaction: nextcord.Interaction):
        """Simple command that responds with Pong!"""
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Ping(bot))