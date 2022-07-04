import discord
from discord.ext import commands

import asyncio


class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def developers(self, ctx):
        owner = self.client.get_user(798280308071596063)
        nody = self.client.get_user(836815485445603369)
        staff = discord.Embed(
            title="The Development Team",
            description=f"{owner} : Founder/Primary Coder\n{nody} : Co-owner/Secondary Coder",
        )
        await ctx.send(embed=staff)

    @commands.command()
    async def brem(self, ctx):
        embed = discord.Embed(
            title="Bot Invitation!",
            description="[Ready for duty!](https://discord.com/api/oauth2/authorize?client_id=901389809283629067&permissions=8&scope=bot)",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(title="Vote for brem!", color=0x00C4B8)
        embed.add_field(
            name=f"here you go {ctx.author}",
            value=f"https://top.gg/bot/901389809283629067/vote or just press on [me](https://top.gg/bot/901389809283629067/vote)",
            inline=False,
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["quit"])
    @commands.is_owner()
    async def shut(self, ctx, down=None):
        owner = self.client.get_user(798280308071596063)
        if down != "down":
            return
        await ctx.send("Executing shut down protocol...")
        embed = discord.Embed(description="**Shutting Down**", color=0x000000)
        await owner.send(embed=embed)
        await asyncio.sleep(2)
        await self.client.close()

    @commands.command()
    @commands.is_owner()
    async def coding(self, ctx):
        await ctx.channel.purge(limit=1)
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send(f"({ctx.author.name}) sending you a dm...", delete_after=5.0)
        await ctx.author.send("https://replit.com/join/ujycybfjfr-warsbro")
        await ctx.send("link sent in dms!", delete_after=7.0)

    @commands.command()
    @commands.is_owner()
    async def botty(self, ctx):
        activeservers = self.client.guilds
        for guild in activeservers:
            await ctx.send(guild.name)


def setup(client):
    client.add_cog(admin(client))
