import discord
from discord.ext import commands


UNAVAILABLE = "Unavailable"
AVAILABLE = "Available"


class Schedule(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["away"])
    async def unavailable(self, ctx):
        user = ctx.message.author
        user_roles = [role.name for role in user.roles]

        await ctx.send(f"{user.name} can't play now")

        if AVAILABLE in user_roles:
            await user.remove_roles(discord.utils.get(user.guild.roles, name=AVAILABLE))
        if UNAVAILABLE not in user_roles:
            await user.add_roles(discord.utils.get(user.guild.roles, name=UNAVAILABLE))

    @commands.command(aliases=["here"])
    async def available(self, ctx):
        user = ctx.message.author
        user_roles = [role.name for role in user.roles]

        await ctx.send(f"{user.name} can play now")
        if UNAVAILABLE in user_roles:
            await user.remove_roles(discord.utils.get(user.guild.roles, name=UNAVAILABLE))
        if AVAILABLE not in user_roles:
            await user.add_roles(discord.utils.get(user.guild.roles, name=AVAILABLE))


def setup(client):
    client.add_cog(Schedule(client))
