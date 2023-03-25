from nextcord.ext import commands


class utils(commands.Cog, name="Ping"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        print("Received ping")
        
        latency = round(self.bot.latency * 1000)
        message = f'Pong! Latency: {latency}ms'
        
        await ctx.send(message)

def setup(bot: commands.Bot):
    bot.add_cog(utils(bot))