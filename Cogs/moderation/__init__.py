import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    #Kick user
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        """Kick a member from the server"""
        try:
            await member.kick(reason=reason)
        except nextcord.errors.Forbidden:
            embed = nextcord.Embed(
                title="Missing Permissions",
                description="You do not have the `kick_members` permission to use this command.",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)
        except nextcord.errors.HTTPException:
            embed = nextcord.Embed(
                title="Failed to kick member",
                description="An error occurred while trying to kick the member. Please try again later.",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            muted_role = nextcord.utils.get(ctx.guild.roles, name="Muted")
            if muted_role in member.roles:
                await member.remove_roles(muted_role)
                await ctx.send(f"{member.mention} was also unmuted.")

            embed = nextcord.Embed(
                title="Kicked user",
                description=f"{member.mention} has been kicked for reason: {reason}",
                color=nextcord.Color.dark_green()
            )
            await ctx.send(embed=embed)


    # Purge messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Clears a specified amount of messages from the chat."""
        try:
            await ctx.channel.purge(limit=amount + 1)
            embed = nextcord.Embed(
                title="Cleared messages",
                description=f"You have cleared {amount} messages",
                color=nextcord.Color.dark_green()
            )
            await ctx.send(embed=embed)
        except nextcord.errors.Forbidden:
            embed = nextcord.Embed(
                title="Missing Permissions",
                description="You do not have the `manage_messages` permission to use this command.",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)

    # Ban User
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        """Bans the specified member from the server."""
        try:
            await member.ban(reason=reason)
            embed = nextcord.Embed(
                title="Banned User",
                description=f"{member.mention} has been banned for reason: {reason}",
                color=nextcord.Color.dark_green()
            )
            await ctx.send(embed=embed)
        except nextcord.errors.Forbidden:
            embed = nextcord.Embed(
                title="Missing Permissions",
                description="You do not have the `ban_members` permission to use this command.",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)
    
    # Unban User
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
    
        for ban_entry in banned_users:
            user = ban_entry.user
    
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                try:
                    await ctx.guild.unban(user)
                    embed = nextcord.Embed(
                        title="Unbanned User",
                        description=f"{user.mention} has been unbanned.",
                        color=nextcord.Color.dark_green()
                    )
                    await ctx.send(embed=embed)
                except nextcord.errors.Forbidden:
                    embed = nextcord.Embed(
                        title="Missing Permissions",
                        description="You do not have the `ban_members` permission to use this command.",
                        color=nextcord.Color.red()
                    )
                    await ctx.send(embed=embed)
                return
        embed = nextcord.Embed(
            title="Invalid User",
            description="The user could not be found in the ban list.",
            color=nextcord.Color.red()
        )
        await ctx.send(embed=embed)
    



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

        try:
            await member.add_roles(mute_role, reason=reason)
            await ctx.send(f"{member.mention} has been muted.")
        except nextcord.errors.Forbidden:
            embed = nextcord.Embed(
                title="Missing Permissions",
                description="I do not have the `manage_roles` permission to use this command.",
                color=nextcord.Color.red(),
            )
            await ctx.send(embed=embed)

    #Unmute User
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: nextcord.Member):
        """Unmutes a muted member."""
        mute_role = nextcord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            embed = nextcord.Embed(
                title="Mute Role Not Found",
                description="The `Muted` role was not found. No members are currently muted.",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        if mute_role not in member.roles:
            embed = nextcord.Embed(
                title="Member Not Muted",
                description=f"{member.mention} is not currently muted.",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))