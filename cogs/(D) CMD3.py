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


class cmd3(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["c", "Purge", "p", "purge"])
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)
        await ctx.send(
            f"Deleted {amount} messages succesfully :white_check_mark:, `this message will be deleted in 5 seconds`",
            delete_after=5.0,
        )

#--------------------------------------------------------------------------------------------------------------
    @commands.command(aliases=["m"])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            creation = discord.Embed(
                description="Creating Muted role...", color=0x00C4B8
            )
            await ctx.reply(embed=creation)
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(
                    mutedRole,
                    speak=False,
                    send_messages=False,
                    read_message_history=True,
                    read_messages=False,
                )
                creation = discord.Embed(
                    title="Created Role Successfully :white_check_mark:"
                )
                await ctx.send(embed=creation)

        embed = discord.Embed(
            description=f"{member.mention} has been muted!\n**Responsible Moderator:** {ctx.author}",
            color=0x00C4B8,
        )
        embed.add_field(name="reason:", value=reason, inline=False)
        await member.add_roles(mutedRole)
        await ctx.send(embed=embed)
        await member.send(
            f"You have been muted from: **{guild.name}**, reason: **{reason}**, By the moderator: **{ctx.author}**"
        )

#------------------------------------------------------------------------------------  
  
    @commands.command(aliases=["tm"])
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member: discord.Member, time, *, reason=None):
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        tempmute = int(time[0]) * time_convert[time[-1]]

        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            creation = discord.Embed(
                description="Creating Muted role...", color=0x00C4B8
            )
            await ctx.reply(embed=creation)
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(
                    mutedRole,
                    speak=False,
                    send_messages=False,
                    read_message_history=True,
                    read_messages=False,
                )
                creation = discord.Embed(
                    title="Created Role Successfully :white_check_mark:"
                )
                await ctx.send(embed=creation)

        embed = discord.Embed(
            description=f"{member.mention} has been temp-muted!\n**Responsible Moderator:** {ctx.author}\n**Time:** {time}",
            color=0x00C4B8,
        )
        embed.add_field(name="reason:", value=reason, inline=False)
        await member.add_roles(mutedRole)
        await ctx.send(embed=embed)
        await member.send(
            f"You have been muted from: **{guild.name}**, reason: **{reason}**, for: **{time}**, By the moderator: **{ctx.author}**"
        )

        await asyncio.sleep(tempmute)
        await member.remove_roles(mutedRole)
        await member.send(
            f"You have been unmuted from **{guild.name}** automatically because you're temp-mute time is over!, responsible moderator was **{ctx.author}**"
        )

#-------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f"you have been unmuted from: - {ctx.guild.name}")

        embed = discord.Embed(
            description=f"{member.mention} is now unmuted!\n**Responsible Moderator:** {ctx.author}",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------

    @commands.command(aliases=["k", "Kick"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.send(
            f"You have been kicked from **{ctx.guild.name}** by **{ctx.message.author}** reason: **{reason}**"
        )
        await ctx.channel.purge(limit=1)
        await member.kick(reason=reason)
        embed = discord.Embed(
            description=f"**{member}** has been kicked out from {ctx.guild.name}\n**Responsible Moderator:** {ctx.message.author}\n **Reason:** {reason}",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------
  
    @commands.command(aliases=["mk"])
    @commands.has_permissions(administrator=True)
    async def mass_kick(self, ctx, *, ids: str):
        list_of_ids = ids.split(" ")
        list_of_idsx = list(map(int, list_of_ids))
        success = 0

        for id in list_of_idsx:
            user = await self.client.fetch_user(id)
            await ctx.guild.kick(user)
            success += 1

        embed = discord.Embed(
            description=f"**{str(success)}** members have been mass-kicked by **{ctx.message.author}**",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)      

#-------------------------------------------------------------------------------------

    @commands.command(aliases=["b"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.send(
            f"You have been banned from **{ctx.guild.name}** by **{ctx.message.author}** reason: **{reason}**"
        )
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)

        embed = discord.Embed(
            description=f"**{member}** has been banned from {ctx.guild.name}\n**Responsible Moderator:** {ctx.message.author}\n**Reason:** {reason}",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)

#------------------------------------------------------------------------------------      
    @commands.command(aliases=["mb"])
    @commands.has_permissions(administrator=True)
    async def mass_ban(self, ctx, *, ids: str = None):
        list_of_ids = ids.split(" ")
        list_of_idsx = list(map(list, list_of_ids))
        success = 0

        for id in list_of_idsx:
            user = await self.client.fetch_user(id)
            await ctx.guild.ban(user, delete_message_days=0)
            success += 1

        embed = discord.Embed(
            description=f"**{str(success)}** members have been mass-banned by **{ctx.message.author}**",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)

#------------------------------------------------------------------------------------

    @commands.command(aliases=["ub"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int = None):
        if user_id == None:
            await ctx.reply(
                "If you don't consider placing an ID, then how we unbanning them?"
            )
            return

            user = await self.client.fetch_user(user_id)
            await ctx.guild.unban(user)

            embed = discord.Embed(
                description=f"{user.mention} ({user.id}) is now unbanned from {ctx.guild.name}\n**Responsible Moderator:** {ctx.message.author}",
                color=0x00C4B8,
            )
            await ctx.send(embed=embed)

#------------------------------------------------------------------------------------

    @commands.command(aliases=["mub"])
    @commands.has_permissions(administrator=True)
    async def mass_unban(self, ctx, *, ids: str):
        list_of_ids = ids.split(" ")
        list_of_idsx = list(map(int, list_of_ids))
        success = 0

        for id in list_of_idsx:
            user = await self.client.fetch_user(id)
            await ctx.guild.unban(user)
            success = 0

        embed = discord.Embed(
            description=f"**{str(success)}** Members have been mass-banned by **{ctx.message.author}**",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)
        await user.send(f"You have been unbanned from **{ctx.guild.name}**")

#------------------------------------------------------------------------------------

    @commands.command()
    async def moderation(self, ctx, help=None):
      guild = ctx.guild
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
      if help == None:
        await ctx.reply(f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``moderation help`` ?")
        return
      if help != "help":
          return
      myembed = discord.Embed(title="", color=0x00C4B8)
      myembed.add_field(
        name="Inputs for moderation",
        value="The following commands are the sets for moderation using the Brem bot.",
        inline=False,
    )
      myembed.add_field(
        name="Clearing", value=f"`{prefix}clear/c (optional number)`", inline=False
    )
      myembed.add_field(
        name="Kicking",
        value=f"`{prefix}kick/k [@member/id] (optional reason)`",
        inline=False,
    )
      myembed.add_field(
        name="Banning",
        value=f"`{prefix}ban/b [@member/id] (optional reason)` or `{prefix}unban [id]`",
        inline=False,
    )
      myembed.add_field(
        name="Muting",
        value=f"`{prefix}mute/m [@member/id] (optional reason)` or `{prefix}unmute [id]`",
        inline=False,
    )
      myembed.add_field(
        name="Temp Muting",
        value=f"`{prefix}tempmute/tm [@member/id] [time s/m/h] (optional reason)`",
        inline=False,
    )
      myembed.add_field(
        name="Server Locking/Unlocking",
        value=f"`{prefix}server_lock` or `{prefix}server_unlock`",
        inline=False,
    )
      myembed.add_field(
        name="slowmode",
        value=f"`{prefix}enable slowmode [number]` or `{prefix}disable slowmode`",
        inline=False,
    )
      myembed.set_footer(
        text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
    )
      await ctx.reply(embed=myembed)      


def setup(client):
  client.add_cog(cmd3(client))