import discord
from discord.ext import commands

import time


class general(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        start_time = time.time()
        message = await ctx.send(
            f"Pong! 🏓\nWs Latency: **{round(self.client.latency * 1000)}ms**"
        )
        end_time = time.time()

        await message.edit(
            content=f"Pong! 🏓 \nWS Latency: **{round(self.client.latency * 1000)}ms** \nAPI Latency: **{round((end_time - start_time) * 1000)}ms**"
        )


def setup(client):
    client.add_cog(general(client))
