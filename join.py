import discord
from discord.ext import commands


class JoinCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="joined")
    async def joined(self, ctx: commands.Context, member: discord.Member):
        """Says when a member joined."""
        # Joined at can be None in very bizarre cases so just handle that as well
        if member.joined_at is None:
            await ctx.send(f"{member} has no join date.")
        else:
            await ctx.send(f"{member} joined {discord.utils.format_dt(member.joined_at)}")
