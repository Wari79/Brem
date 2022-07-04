import discord
from discord.ext import commands

import asyncio


class test(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.counter = 0

    @commands.command()
    @commands.is_owner()
    async def temp_give(self, ctx, member: discord.Member, role: discord.Role, time):
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        temprole = int(time[0]) * time_convert[time[-1]]
        await ctx.send(f"Giving {member} ``{role}``...")
        async with ctx.typing():
            await asyncio.sleep(2)
        await member.add_roles(role)
        await ctx.send(f"Gave {member} the role ``{role}``")
        await asyncio.sleep(temprole)
        await member.remove_roles(role)


def setup(client):
    client.add_cog(test(client))
