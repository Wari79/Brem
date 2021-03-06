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
translator = Translator(service_urls=["translate.googleapis.com"])

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

class cmd5(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def quote(self, ctx):
        quote = get_quote()
        embed = discord.Embed(
            title=f"{ctx.author.name}'s quote!", description=(quote), color=0x00C4B8
        )
        await ctx.reply(embed=embed)

#--------------------------------------------------------------------------------------

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        response = requests.get("https://meme-api.herokuapp.com/gimme/dankmemes")
        embed = discord.Embed(title=f"{ctx.author}'s meme")
        embed.set_image(url=response.json().get("url"))
        await ctx.send(embed=embed)

#--------------------------------------------------------------------------------------

    @commands.command(aliases=["Countdown", "COUNTDOWN", "count-down", "cd"])
    async def countdown(self, ctx, timeInput=None):
        if timeInput == None:
            await ctx.reply("you need to set a number to be timed off dummy!")
            return
        else:
            try:
                try:
                    time = int(timeInput)
                except:
                    convertTimeList = {
                        "s": 1,
                        "m": 60,
                        "h": 3600,
                        "d": 86400,
                        "S": 1,
                        "M": 60,
                        "H": 3600,
                        "D": 86400,
                    }
                    time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
                if time > 86400:
                    await ctx.reply("I can't do timers over a day long")
                    return
                if time <= 0:
                    await ctx.reply("Timers don't go into negatives :/")
                    return
                if time >= 3600:
                    message = await ctx.send(
                        f"Timer has been set succesfully :white_check_mark: ```Remaining time: {time//3600} hours {time%3600//60} minutes {time%60} seconds``` **{ctx.author.mention} I will mention you when it ends!**"
                    )
                elif time >= 60:
                    message = await ctx.send(
                        f"Timer has been set succesfully :white_check_mark: ```Remaining time: {time//60} minutes {time%60} seconds``` **{ctx.author.mention} I will mention you when it ends!**"
                    )
                elif time < 60:
                    message = await ctx.send(
                        f"Timer has been set succesfully :white_check_mark: ```Remaining time: {time} seconds``` **{ctx.author.mention} I will mention you when it ends!**"
                    )
                while True:
                    try:
                        await asyncio.sleep(5)
                        time -= 5
                        if time >= 3600:
                            await message.edit(
                                content=f" ```Remaing time: {time//3600} hours {time %3600//60} minutes {time%60} seconds```"
                            )
                        elif time >= 60:
                            await message.edit(
                                content=f" ```Remaining time: {time//60} minutes {time%60} seconds```"
                            )
                        elif time < 60:
                            await message.edit(
                                content=f" ```Remaining time: {time} seconds```"
                            )
                        if time <= 0:
                            await message.edit(content="Ended!")
                            await ctx.send(
                                f"{ctx.author.mention} Your countdown has ended!"
                            )
                            break
                    except:
                        break
            except:
                await ctx.send(
                    f"Alright, first you gotta let me know how I'm gonna time **{timeInput}**...."
                )

#-------------------------------------------------------------------------------------

    @commands.command(aliases=["remind"])
    async def reminder(self, ctx, timeInput, *, message=None):
        if timeInput == None:
            await ctx.reply(
                "you need to set a number to be timed off, for example ``*remind 4h get the dog for a walk``"
            )
            return
        else:
            try:
                try:
                    time = int(timeInput)
                except:
                    convertTimeList = {
                        "s": 1,
                        "m": 60,
                        "h": 3600,
                        "d": 86400,
                        "S": 1,
                        "M": 60,
                        "H": 3600,
                        "D": 86400,
                    }
                    time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
                if time > 86400:
                    await ctx.reply("I can't do timers over a day long")
                    return
                if time <= 0:
                    await ctx.reply("Timers don't go into negatives :/")
                    return
                if time >= 3600:
                    await ctx.send(
                        f"Alright {ctx.author.mention}, in ``{time//3600} hours, {time%3600//60} minutes, and {time%60} seconds`` I will remind you of **{message}**"
                    )
                elif time >= 60:
                    await ctx.send(
                        f"Alright {ctx.author.mention}, in ``{time//60} minutes and {time%60} seconds``, I will remind you of **{message}**"
                    )
                elif time < 60:
                    await ctx.send(
                        f"Alright {ctx.author.mention}, in ``{time} seconds`` I will remind you of **{message}**"
                    )
                while True:
                    try:
                        await asyncio.sleep(5)
                        time -= 5
                        if time <= 0:
                            await ctx.author.send(
                                f"{ctx.author.mention}, Your reminder ended, ``{message}``"
                            )
                            break
                    except:
                        break
            except:
                await ctx.send(
                    f"Alright, first you gotta let me know how I'm gonna time **{timeInput}**..."
                )

#-------------------------------------------------------------------------------------

    @commands.command()
    async def define(self, ctx, word):
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
        )
        if response.status_code == 404:
            await ctx.reply(f"Word not found {ctx.author.name}")
            return
        else:
            wordx = response.json()
            the_dictionary = wordx[0]
            meanings = the_dictionary["meanings"]
            definitions = meanings[0]
            definition = definitions["definitions"]
            meaningg = definition[0]
            meaning = meaningg["definition"]
            example = meaningg.get("example", ["None"])
            synonymslist = meaningg.get("synonyms", ["None"])

            if isinstance(synonymslist, str):
                synonymslist = [synonymslist]
            synonyms = ", ".join(synonymslist)

            embed = discord.Embed(title=f"`{word.lower()}`", color=0x00C4B8)
            embed.add_field(name="Definition", value=f"{meaning}", inline=False)
            embed.add_field(name="Example", value=f"*{example}*", inline=False)
            embed.add_field(name="Synonyms", value=f"``{synonyms}``", inline=False)
            await ctx.reply(embed=embed)

#--------------------------------------------------------------------------------------

    @commands.command()
    async def translate(self, ctx, language, *, message):
        translator = Translator()
        translation = translator.translate(message, dest=language)

        embed = discord.Embed(description=f"Translation  ??????  ``{translation.text}``")
        embed.add_field(
            name="Language Triggered:", value=f"``{language}``", inline=False
        )
        embed.add_field(name="Sentence Used:", value=f"``{message}``", inline=False)
        embed.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

#--------------------------------------------------------------------------------------

    @commands.command()
    async def say(self, ctx, *, message=None):
        if message == None:
            await ctx.reply(
                f"pssst {ctx.author.name}, you need to put a message for me to say dude..."
            )
            return
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(message)

#--------------------------------------------------------------------------------------

    @commands.command()
    async def asking(self, ctx, help=None):
      guild = ctx.guild
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
      if help == None:
        await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``asking help`` ?"
        )
        return
      if help != "help":
        return
      myembed = discord.Embed(
        title="Asking", description=f"```{prefix}ask [question]```", color=0x00C4B8
    )
      await ctx.send(embed=myembed)  

#---------------------------------------------------------------------------------------------

    @commands.command()
    async def calculations(ctx, help=None):
      guild = ctx.guild
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
      if help == None:
        await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``calculations help`` ?"
        )
        return
      if help != "help":
        return
      embed = discord.Embed(
        title="Calculations",
        description=f"You can use ``+  , - , * , /`` and the **correct** example would be ```{prefix}calculate 1+1``` or ```{prefix}calculate 1-1``` or ```{prefix}calculate 1*1``` or ```{prefix}calculate 1/1```",
        color=0x00C4B8,
    )
      await ctx.reply(embed=embed)      

def setup(client):
  client.add_cog(cmd5(client))