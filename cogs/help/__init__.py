import nextcord
from nextcord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = nextcord.Embed(
            title='Help',
            description='List of available commands',
            color=nextcord.Color.blue()
        )

        cog_names = []
        for cog in self.bot.cogs:
            cog_names.append(cog)

        for cog_name in cog_names:
            cog = self.bot.get_cog(cog_name)
            if cog:
                command_list = cog.get_commands()
                if command_list:
                    command_str = ''
                    for command in command_list:
                        command_str += f'**{command.name}**: {command.help}\n'
                    embed.add_field(
                        name=cog_name,
                        value=command_str,
                        inline=False
                    )

        embed.set_footer(text=f"Use {self.bot.command_prefix}help command_name for more info on a command")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
