import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Ban Commang
    @commands.command()
    async def ban(self, ctx, member: nextcord.Member):
        if ctx.author.guild_permissions.ban_members:
            try:
                await member.ban()
                await ctx.send(f'{member} has been banned.')
            except:
                await ctx.send('Please mention a valid member.')
        else:
            await ctx.send("You don't have the permission to use this command.")

    @nextcord.slash_command()
    async def ban(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Ban a member from the server"""
        if interaction.author.guild_permissions.ban_members:
            try:
                await member.ban()
                await interaction.response.send_message(f'{member} has been banned.')
            except:
                await interaction.response.send_message('Please mention a valid member.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")


    # Kick command
    @commands.command()
    async def kick(self, ctx, member: nextcord.Member):
        if ctx.author.guild_permissions.kick_members:
            try:
                await member.kick()
                await ctx.send(f'{member} has been kicked.')
            except:
                await ctx.send('Please mention a valid member.')
        else:
            await ctx.send("You don't have the permission to use this command.")

    @nextcord.slash_command()
    async def kick(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Kick a member from the server"""
        if interaction.author.guild_permissions.kick_members:
            try:
                await member.kick()
                await interaction.response.send_message(f'{member} has been kicked.')
            except:
                await interaction.response.send_message('Please mention a valid member.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")


    # Mute command
    @commands.command()
    async def mute(self, ctx, member: nextcord.Member):
        if ctx.author.guild_permissions.manage_roles:
            try:
                # Replace "Muted" with the actual role name for muting
                role = nextcord.utils.get(ctx.guild.roles, name="Muted")
                await member.add_roles(role)
                await ctx.send(f'{member} has been muted.')
            except:
                await ctx.send('Please mention a valid member.')
        else:
            await ctx.send("You don't have the permission to use this command.")

    @nextcord.slash_command()
    async def mute(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Mute a member for set time"""
        if interaction.author.guild_permissions.manage_roles:
            try:
                # Replace "Muted" with the actual role name for muting
                role = nextcord.utils.get(interaction.guild.roles, name="Muted")
                await member.add_roles(role)
                await interaction.response.send_message(f'{member} has been muted.')
            except:
                await interaction.response.send_message('Please mention a valid member.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")


    # Unmute command
    @commands.command()
    async def unmute(self, ctx, member: nextcord.Member):
        if ctx.author.guild_permissions.manage_roles:
            try:
                # Replace "Muted" with the actual role name for muting
                role = nextcord.utils.get(ctx.guild.roles, name="Muted")
                await member.remove_roles(role)
                await ctx.send(f'{member} has been unmuted.')
            except:
                await ctx.send('Please mention a valid member.')
        else:
            await ctx.send("You don't have the permission to use this command.")

    @nextcord.slash_command()
    async def unmute(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Unmute a member that has been muted"""
        if interaction.author.guild_permissions.manage_roles:
            try:
                # Replace "Muted" with the actual role name for muting
                role = nextcord.utils.get(interaction.guild.roles, name="Muted")
                await member.remove_roles(role)
                await interaction.response.send_message(f'{member} has been unmuted.')
            except:
                await interaction.response.send_message('Please mention a valid member.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")


    # delete message
    @commands.command()
    async def clear(self, ctx, limit: int):
        if ctx.author.guild_permissions.manage_messages:
            try:
                # Limit the number of messages to delete
                await ctx.channel.purge(limit=limit + 1)
                await ctx.send(f'{limit} messages have been deleted.')
            except:
                await ctx.send('An error occurred while deleting messages.')
        else:
            await ctx.send("You don't have the permission to use this command.")

    @nextcord.slash_command()
    async def clear(self, interaction: nextcord.Interaction, limit: int):
        """Clear a number of messages from channel"""
        if interaction.user.guild_permissions.manage_messages:
            try:
                # Limit the number of messages to delete
                await interaction.channel.purge(limit=limit + 1)
                await interaction.response.send_message(f'{limit} messages have been deleted.')
            except:
                await interaction.response.send_message('An error occurred while deleting messages.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")

def setup(bot):
    bot.add_cog(Moderation(bot))