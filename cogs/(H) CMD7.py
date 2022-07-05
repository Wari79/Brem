import discord
from discord.ext import commands
import json



class cmd6(commands.Cog):
    def __init__(self, client):
        self.client = client


    def determine_prefix(bot, msg):
      DEFAULT_PREFIX = "*"
      guild = msg.guild
      base = [DEFAULT_PREFIX]

      with open("prefix.json", "r", encoding="utf-8") as fp:
          custom_prefixes = json.load(fp)

      if guild:
        try:
            prefix = custom_prefixes[f"{guild.id}"]
            return prefix
        except KeyError:
            return base
            return prefix

      return base

    @commands.command(aliases=["Change_prefix", "cp"])
    @commands.has_permissions(manage_guild=True)
    async def change(self, ctx, prefix, prefixes: str = None):
      if prefix == None:
        await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``change prefix`` ?"
        )
        return
      if prefix != "prefix":
        return
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)  # load the JSON file

      try:
        custom_prefixes[f"{ctx.guild.id}"] = prefixes  # If the guild is in the JSON
      except KeyError:  # If no entry for the guild exists
        new = {ctx.guild.name: prefixes}
        custom_prefixes.update(new)  # Add the new prefix for the guild

      await ctx.send(f"Prefix is now `{prefixes}` on the server.")
      await ctx.guild.me.edit(nick=f"({prefixes})Brem")

      with open("prefix.json", "w", encoding="utf-8") as fpp:
        json.dump(custom_prefixes, fpp, indent=2)

#-----------------------------------------------------------------------------------------------

    @commands.command()
    async def brem(self, ctx):
        embed = discord.Embed(
            title="Bot Invitation!",
            description="[Ready for duty!](https://discord.com/api/oauth2/authorize?client_id=901389809283629067&permissions=8&scope=bot)",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)

#-----------------------------------------------------------------------------------------------

    @commands.command()
    async def developers(self, ctx):
        owner = self.client.get_user(798280308071596063)
        staff = discord.Embed(
            title="The Development Team",
            description=f"{owner} : Founder/Primary Coder",
        )
        await ctx.send(embed=staff)

#-----------------------------------------------------------------------------------------------

    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(title="Vote for brem!", color=0x00C4B8)
        embed.add_field(
            name=f"here you go {ctx.author}",
            value=f"https://top.gg/bot/901389809283629067/vote or just press on [me](https://top.gg/bot/901389809283629067/vote)",
            inline=False,
        )
        await ctx.send(embed=embed)

#-----------------------------------------------------------------------------------------------

    @commands.command(aliases=["os", "Open_source"])
    async def open_source(self, ctx, source=None):
        source = discord.Embed(
            description=f"[Open Source Link](https://replit.com/@Warsbro/Brem-1#main.py)",
            color=0x00C4B8,
        )
        await ctx.reply(embed=source)

def setup(client):
  client.add_cog(cmd6(client))