
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


class cmd4(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["Create_role", "cr"])
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, *, role_name):
        guild = ctx.guild
        await ctx.send(
            "What color do you want the role to be? ``purple-green-blue-yellow-pink-grey-beige-light_blue``"
        )
        colors = await self.client.wait_for(
            "message",
            check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,
        )
        if colors.content.lower() == "green":
            await guild.create_role(name=role_name, color=0x00FF00)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        if colors.content.lower() == "yellow":
            await guild.create_role(name=role_name, color=0xFFFF00)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        if colors.content.lower() == "purple":
            await guild.create_role(name=role_name, color=0x6A0DAD)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        if colors.content.lower() == "blue":
            await guild.create_role(name=role_name, color=0x0000FF)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        if colors.content.lower() == "grey":
            await guild.create_role(name=role_name, color=0x808080)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        if colors.content.lower() == "pink":
            await guild.create_role(name=role_name, color=0xFFC0CB)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        if colors.content.lower() == "light_blue":
            await guild.create_role(name=role_name, color=0x00FFFF)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        if colors.content.lower() == "beige":
            await guild.create_role(name=role_name, color=0xF5F5DC)
            await ctx.send(
                f"Created ``{role_name}``, with a ``{colors.content}`` color"
            )
            return

        else:
            await ctx.send("No color matched giving options :/")

#-------------------------------------------------------------------------------------

    @commands.command(aliases=["Delete_role", "dr"])
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, role: discord.Role = None):
        await role.delete()
        await ctx.send(f"We have deleted ``{role}`` successfully.")

#-------------------------------------------------------------------------------------

    @commands.command(aliases=["gr", "Give_role"])
    @commands.has_permissions(manage_roles=True)
    async def give_role(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Giving {member} ``{role}``...")
        async with ctx.typing():
            await asyncio.sleep(2)
        await member.add_roles(role)
        await ctx.send(f"Gave {member} the role ``{role}``")

#-------------------------------------------------------------------------------------

    @commands.command(aliases=["rr", "Remove_role"])
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Removing ``{role}`` from ``{member}``...")
        await member.remove_roles(role)
        await ctx.send(f"Removed ``{role}`` from ``{member}``")

#------------------------------------------------------------------------------------    

    @commands.command()
    async def nick(self, ctx, member: discord.Member, *, nick):
        await member.edit(nick=nick)
        await ctx.send(f"Nickname has been changed for ``{member}``")

def setup(client):
  client.add_cog(cmd4(client))