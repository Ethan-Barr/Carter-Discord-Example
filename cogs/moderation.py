import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ban command
    @nextcord.slash_command()
    async def ban(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Ban a member from the server"""
        if interaction.user.guild_permissions.ban_members:
            try:
                await member.ban()
                await interaction.response.send_message(f'{member} has been banned.')
            except:
                await interaction.response.send_message('Please mention a valid member.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")
    
    # Kick command
    @nextcord.slash_command()
    async def kick(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Kick a member from the server"""
        if interaction.user.guild_permissions.kick_members:
            try:
                await member.kick()
                await interaction.response.send_message(f'{member} has been kicked.')
            except:
                await interaction.response.send_message('Please mention a valid member.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")
    
    # Mute command
    @nextcord.slash_command()
    async def mute(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Mute a member for set time"""
        if interaction.user.guild_permissions.manage_roles:
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
    @nextcord.slash_command()
    async def unmute(self, interaction: nextcord.Interaction, member: nextcord.Member):
        """Unmute a member that has been muted"""
        if interaction.user.guild_permissions.manage_roles:
            try:
                # Replace "Muted" with the actual role name for muting
                role = nextcord.utils.get(interaction.guild.roles, name="Muted")
                await member.remove_roles(role)
                await interaction.response.send_message(f'{member} has been unmuted.')
            except:
                await interaction.response.send_message('Please mention a valid member.')
        else:
            await interaction.response.send_message("You don't have the permission to use this command.")


    # delete messages
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