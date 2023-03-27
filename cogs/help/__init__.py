import nextcord
from nextcord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        # Create an embed
        embed = nextcord.Embed(title="Command Help", description="Here's a list of all the available commands:", color=0x00ff00)

        # Add fields for each command and its description
        for cog in self.bot.cogs:
            # Only show commands for the "Moderation" cog if the user has the "Moderator" role
            if cog == "Moderation" and not nextcord.utils.get(ctx.author.roles, name="The TVA"):
                continue

            # Add a title for each subject of commands
            embed.add_field(name=f"**{cog} Commands**", value="\u200b", inline=False)

            for command in self.bot.get_cog(cog).get_commands():
                if not command.hidden:
                    # Add each command and its description
                    embed.add_field(name=f"{command.name}", value=command.help, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
