import discord
from discord.ext import commands

import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import asyncio
import random
from core.stuff import get_quote
from core.stuff import Passwords, email, words, ip, nick, status, insults



class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hack(self, ctx, *, member: discord.Member = None):
        await ctx.reply(
            "You sure you want to perform this **DEADLY** command? **yes/no**"
        )
        msg = await self.client.wait_for(
            "message",
            check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,
        )

        if msg.content.lower() == "yes":
            message = await ctx.reply(
                f"Alright then {ctx.author.name}, let's hack this weeby called {member.name}"
            )

            async with ctx.typing():
                await asyncio.sleep(3)
            await message.edit(content=f"Hackin {member.name}.")

            async with ctx.typing():
                await asyncio.sleep(1)
            await message.edit(content=f"Hackin {member.name}..")

            async with ctx.typing():
                await asyncio.sleep(1)
            await message.edit(content=f"Hackin {member.name}...")

            async with ctx.typing():
                await asyncio.sleep(1)
            await message.edit(content=f"Done! their email: {random.choice(email)}")

            async with ctx.typing():
                await asyncio.sleep(2)
            await message.edit(content=f"password: {random.choice(Passwords)}")

            async with ctx.typing():
                await asyncio.sleep(2)
            await message.edit(content=f"Commonly used word: {random.choice(words)}")

            async with ctx.typing():
                await asyncio.sleep(2)
            await message.edit(
                content=f"Btw {member.name} is a {random.choice(insults)}"
            )

            async with ctx.typing():
                await asyncio.sleep(2)
                await message.edit(content=f"Their status: **{random.choice(status)}**")

            async with ctx.typing():
                await asyncio.sleep(2)
            await message.edit(
                content=f"Changing their nickname to **{random.choice(nick)}**"
            )

            async with ctx.typing():
                await asyncio.sleep(2)
            await message.edit(content=f"I.P address: **{random.choice(ip)}**")

            async with ctx.typing():
                await asyncio.sleep(3)
            await message.edit(
                content="They now have a *trojan* horse virus on their device HAHA"
            )
            return

        else:
            await ctx.reply("Cancelling this deadly command then...")


def setup(client):
    client.add_cog(fun(client))
