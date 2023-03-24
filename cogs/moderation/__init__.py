import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.log_file = open('moderation.log', 'a')


    # Kick user
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        """Kick a member from the server"""
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked from the server.")

    # Purge messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Clears a specified amount of messages from the chat."""
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages have been cleared.")

    # Ban User
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        """Bans the specified member from the server."""
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')
    def cog_unload(self):
        self.log_file.close()




def setup(client):
    client.add_cog(Moderation(client))