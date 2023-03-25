import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


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

    

    # Unban User
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')




    # Mute User
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: nextcord.Member, *, reason=None):
        """Mutes the specified member in the server."""
        mute_role = nextcord.utils.get(ctx.guild.roles, name="Muted")

        if not mute_role:
            # Create the mute role if it doesn't exist
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, send_messages=False)

        await member.add_roles(mute_role, reason=reason)
        await ctx.send(f'{member.mention} has been muted.')

    #Unmute User
    @commands.command()
    async def unmute(self, ctx, member: nextcord.Member):
        """Unmutes a muted member."""
        role = nextcord.utils.get(ctx.guild.roles, name="Muted")
        if role not in member.roles:
            await ctx.send(f"{member.mention} is not muted.")
            return
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} has been unmuted.")


def setup(client):
    client.add_cog(Moderation(client))