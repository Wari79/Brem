import discord
from discord.ext import commands
from replit import db
import requests
import random
import json
import asyncio
from keep_alive import keep_alive
import os
from discord.utils import find
import datetime
from datetime import datetime
from discord.ext import tasks
from googletrans import Translator
import traceback
import sys
import time

def restart_bot():
    os.execv(sys.executable, ["python"] + sys.argv)

class owner(commands.Cog):
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

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.send("Executing the restart protocol...")
        restart_bot()  

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
    client.add_cog(owner(client))
