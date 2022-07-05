import discord
from discord.ext import commands

import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import asyncio
import random
from core.stuff import get_quote
from core.stuff import Passwords, email, words, ip, nick, status, insults
import json


def audio_len(path):
    global MP3
    audio = MP3(path)
    return audio.info.length


class cmd6(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def dm(self, ctx, user: discord.User, *, message=None):
        await ctx.channel.purge(limit=1)
        await ctx.send(
            "Do you want me to tell the user that you are the one who sent this message?**yes/no**?",
            delete_after=10.0,
        )

        msg2 = await self.client.wait_for(
            "message",
            check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,
        )

        if msg2.content.lower() == "yes":
            userowner = self.client.get_user(798280308071596063)
            await msg2.add_reaction("✅")
            reply = discord.Embed(title="<a:warning:978727506569994291>Incoming DM!<a:warning:978727506569994291>", description=f"<a:Right2:969689928717983815>``{message}``", color=0x00c4b8)
            await user.send(embed=reply)
            await user.send(f"**This message had been sent by**  -  {ctx.author}")
            await ctx.author.send("DM Sent successfully :white_check_mark:")
            await userowner.send(
                f"{ctx.author.name} to {user.name} message = {message}"
            )
            return
        try:
            userowner = self.client.get_user(798280308071596063)
            await msg2.add_reaction("✅")
            reply2 = discord.Embed(title="<a:warning:978727506569994291>Incoming DM<a:warning:978727506569994291>", description=f"<a:Right2:969689928717983815> ``{message}``", color=0x00c4b8)
            await user.send(embed=reply2)
            await user.send(
                f"**This message is sent by an anonymous user** :shushing_face:"
            )
            await ctx.author.send(
                "DM Sent succefully :white_check_mark: (I've hid your name too :wink:)",
            )
            await userowner.send(
                f"{ctx.author.name} to {user.name} message = ``{message}``"
            )

        except discord.Forbidden:
            embed = discord.Embed(
                description="Sorry, but I couldn't send this user the reason via dm. Dm failures occur when you excute the command on bots, or when members have disabled incoming dms",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

#-----------------------------------------------------------------------------------------------

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            pass

        else:
            with open("reactrole.js") as react_file:
                data = json.load(react_file)
                for x in data:
                    if (
                        x["emoji"] == payload.emoji.name
                        and x["message_id"] == payload.message_id
                    ):
                        role = discord.utils.get(
                            self.client.get_guild(payload.guild_id).roles,
                            id=x["role_id"],
                        )
                        await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        with open("reactrole.js") as react_file:
            data = json.load(react_file)
            for x in data:
                if (
                    x["emoji"] == payload.emoji.name
                    and x["message_id"] == payload.message_id
                ):
                    role = discord.utils.get(
                        self.client.get_guild(payload.guild_id).roles, id=x["role_id"]
                    )
                    await self.client.get_guild(payload.guild_id).get_member(
                        payload.user_id
                    ).remove_roles(role)

    @commands.command(aliases=["React_role"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 25, commands.BucketType.user)
    async def reactrole(self, ctx, emoji, role: discord.Role, *, message):
        myembed = discord.Embed(description=message)
        msg = await ctx.channel.send(embed=myembed)
        await msg.add_reaction(emoji)

        with open("reactrole.js") as json_file:
            data = json.load(json_file)

        new_react_role = {
            "role_name": role.name,
            "role_id": role.id,
            "emoji": emoji,
            "message_id": msg.id,
        }
        data.append(new_react_role)

        with open("reactrole.js", "w") as j:
            json.dump(data, j, indent=4)

#----------------------------------------------------------------------------------------------

    @commands.command(aliases=["calc", "Calculate", "calcu"])
    async def calculate(self, ctx, operation: str = None):
        if operation == None:
            await ctx.reply(
                "What should i calculate then? **correct** format would be ``ex. *calc 4+5``"
            )
            return
        else:
            await ctx.reply(eval(operation))

#----------------------------------------------------------------------------------------------

    @commands.command(aliases=["8ball"])
    async def ask(self, ctx, *, question):
        answer = [
            "Sure, why not?",
            "Yes, definitely.",
            "Without a doubt.",
            "Most likely.",
            "I'm not quite sure.",
            "Truly a hard question, but the answer is no.",
            "I doubt it.",
            "I'd say, no.",
            "I guess... yeah?",
            "Sorry, an error occured. Can you ask again?",
            "I can't say for sure about that one.",
            "why?",
            "maybe",
            "idk",
            "yes",
            "what do you mean?",
            "sure",
        ]
        if question == None:
            await ctx.reply(
                "Well you need to put a question for this command to work..."
            )
            return
        if not question.endswith("?"):
            await ctx.reply(
                f"{ctx.author.name}, I don't think that's a question. Please add a question mark after your question!"
            )
            return

        else:
            async with ctx.typing():
                await asyncio.sleep(2)
            await ctx.reply(f"```Q: {question}```\nA: **{random.choice(answer)}**")

#----------------------------------------------------------------------------------------------

    @commands.command()
    async def hello(self, ctx, member, user: discord.User = None):
        if member != "member":
            return
        if user == None:
            await ctx.reply(
                "You need to Mention A Member; in order to complete the greeting operation!"
            )
            return

        else:
            await ctx.channel.purge(limit=1)
            await user.send(
                f"Hello {user.mention}, {ctx.author.name} :wave: Has Greeted You at {ctx.guild.name} :D"
            )

            async with ctx.typing():
                await asyncio.sleep(2)
            await user.send(
                f"listen out {user.mention} if you want to greet back a member just use the command greet back! ``` greet back [@member/id]```"
            )

            async with ctx.typing():
                await asyncio.sleep(3)
            await ctx.send(
                "Member has been greeted succesfully wait for a greet back!",
                delete_after=20.0,
            )
          
    @commands.command()
    async def greet(self, ctx, back, user: discord.User = None):
            if back != "back":
                return
            else:
                await ctx.channel.purge(limit=1)
                async with ctx.typing():
                    await asyncio.sleep(3)
                await user.send(
                    f"hey {user.mention}, {ctx.author.name} is greeting you back at {ctx.guild.name}; how cool is that huh? :sparkles:"
                )
                await ctx.send("Greeted back!", delete_after=21.0)
#----------------------------------------------------------------------------------------------

    @commands.command(aliases=["e", "E"])
    async def embed(self, ctx, *, message=None):
        colors = [
            0xFFE4E1,
            0x00FF7F,
            0xD8BFD8,
            0xDC143C,
            0xFF4500,
            0xDEB887,
            0xADFF2F,
            0x800000,
            0x4682B4,
            0x006400,
            0x808080,
            0xA0522D,
            0xF08080,
            0xC71585,
            0xFFB6C1,
            0x00CED1,
        ]

        await ctx.reply(
            "What color do you want the embed to be? [green, red, black, default, brem, random]"
        )
        msg = await self.client.wait_for(
            "message",
            check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,
        )
        if msg.content.lower() == "green":
            Saying = discord.Embed(
                title=f"{ctx.guild.name}", description=message, color=0x24C41A
            )
            await ctx.send(embed=Saying)
            return

        if msg.content.lower() == "red":
            Saying = discord.Embed(
                title=f"{ctx.guild.name}", description=message, color=0xC41A1A
            )
            await ctx.send(embed=Saying)
            return

        if msg.content.lower() == "brem":
            Saying = discord.Embed(
                title=f"{ctx.guild.name}", description=message, color=0x00C4B8
            )
            await ctx.send(embed=Saying)
            return

        if msg.content.lower() == "default":
            Saying = discord.Embed(
                title=f"{ctx.guild.name}", description=message, color=0x838383
            )
            await ctx.send(embed=Saying)
            return

        if msg.content.lower() == "black":
            Saying = discord.Embed(
                title=f"{ctx.guild.name}", description=message, color=0x000000
            )
            await ctx.send(embed=Saying)
            return

        if msg.content.lower() == "random":
            Saying = discord.Embed(
                title=f"{ctx.guild.name}",
                description=message,
                color=random.choice(colors),
            )
            await ctx.send(embed=Saying)
            return
        else:
            await ctx.send(
                "Sorry, i couldn't define this color, make sure it has no any capital letters in the beginning!"
            )

#----------------------------------------------------------------------------------------------

    @commands.command()
    async def tts(self, ctx, *, text):
        global gTTS
        speech = gTTS(text=text, lang="en", tld="co.uk")
        speech.save("tts.mp3")
        image = discord.File("tts.mp3")
        await ctx.send(file=image)

#----------------------------------------------------------------------------------------------





def setup(client):
  client.add_cog(cmd6(client))