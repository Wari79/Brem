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





class cmd2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def report(self, ctx):
        timenow = datetime.now()

        await ctx.reply(
            f"Alright then {ctx.author}, let's start the report system process, i will be asking you several questions please give the information i need."
        )

        async with ctx.typing():
            await asyncio.sleep(1)

        step1 = discord.Embed(
            title="Step 1",
            description="Please send the ID of the user you are reporting, __**Send cancel/end to stop this report**__",
            color=0x00C4B8,
        )
        await ctx.reply(embed=step1)

        id = await self.client.wait_for(
            "message",
            check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,
        )

        if id.content.lower() == "cancel" or id.content.lower() == "end":
            end = discord.Embed(
                description=":x:**Report Cancelled**:x:", color=0xFF0000
            )
            await ctx.reply(embed=end)

        else:

            step2 = discord.Embed(
                description="Step 1 completed, please wait a moment", color=0x90EE90
            )
            await ctx.reply(embed=step2)
            async with ctx.typing():
                await asyncio.sleep(3)

            step3 = discord.Embed(
                description="What is the reason of this report?", color=0x00C4B8
            )
            await ctx.send(embed=step3)

            reason = await self.client.wait_for(
                "message",
                check=lambda m: m.author == ctx.author
                and m.channel.id == ctx.channel.id,
            )
            step4 = discord.Embed(
                description="Please provide a proof of this by sending the **link to the image**, ``(send the screenshot to any text channel < right click on the image < copy image address)``",
                color=0x00C4B8,
            )
            await ctx.reply(embed=step4)

            proof = await self.client.wait_for(
                "message",
                check=lambda m: m.author == ctx.author
                and m.channel.id == ctx.channel.id,
            )
            step5 = discord.Embed(
                title="Creating final report, please wait a moment", color=0x90EE90
            )
            await ctx.send(embed=step5)
            async with ctx.typing():
                await asyncio.sleep(3)
            reports = discord.Embed(
                title="Report",
                description=f"In: ``{ctx.guild.name}``\nReporter: ``{ctx.author} ({ctx.author.id})``\nAgainst: ``{id.content}``\nFor: ``{reason.content}``\nProof: ``{proof.content}``\nIssued At: ``{timenow.strftime('%A, %B %d %Y @ %I:%M %p')}``",
                color=0x00C4B8,
            )
            await ctx.send(embed=reports)
            async with ctx.typing():
                await asyncio.sleep(2)
            finnal = discord.Embed(
                title=":warning:Sending the report to Brem's staff team:warning:",
                color=0xFEE75C,
            )
            await ctx.send(embed=finnal)
            async with ctx.typing():
                await asyncio.sleep(3)
            owner = self.client.get_user(798280308071596063)
            await owner.send(embed=reports)
            guild = ctx.guild
            channel0 = discord.utils.get(guild.text_channels, name="brem-reports")

            if not channel0:
                report_channel = discord.Embed(
                    title=":warning:Creating Brem's unique ``report channel``:warning:",
                    color=0xFEE75C,
                )
                await ctx.send(embed=report_channel)
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(
                        read_messages=True,
                        send_messages=False,
                        add_reactions=False,
                        read_message_history=True,
                    ),
                    guild.me: discord.PermissionOverwrite(
                        send_messages=True, view_channel=True
                    ),
                }
                channel1 = await guild.create_text_channel(
                    name="brem-reports", overwrites=overwrites
                )
                report_channel2 = discord.Embed(
                    title="Created Report channel successfully :white_check_mark:",
                    color=0x90EE90,
                )
                await ctx.send(embed=report_channel2)
                await channel1.send(embed=reports)
                message = await channel1.send(
                    f"{guild.owner.mention} do you wish to ban the member from your server?"
                )
                await message.add_reaction("✅")
                await message.add_reaction("❌")

                def check(reaction, user):
                    return user == guild.owner

                reaction = None
                while True:
                    if str(reaction) == "✅":
                        await message.clear_reactions()
                        user = await self.client.fetch_user(int(id.content))
                        await ctx.guild.ban(user)
                        banning = discord.Embed(
                            description="**Banned this user**", color=0xFEE75C
                        )
                        await message.edit(embed=banning)
                    elif str(reaction) == "❌":
                        await message.clear_reactions()
                        cancel_ban = discord.Embed(
                            title="", description="Ban Cancelled", color=0xFF0000
                        )
                        await message.edit(embed=cancel_ban)
                        break
                    try:
                        reaction, user = await self.client.wait_for(
                            "reaction_add", timeout=50.0, check=check
                        )
                        await message.remove_reaction(reaction, user)
                    except:
                        break
            else:
                found = discord.Embed(
                    description=f"Found an existing channel, {channel0.mention}",
                    color=0x00C4B8,
                )
                await ctx.send(embed=found)
                await channel0.send(embed=reports)
                message = await channel0.send(
                    f"{guild.owner.mention} do you wish to ban the member from your server?"
                )
                await message.add_reaction("✅")
                await message.add_reaction("❌")

                def check(reaction, user):
                    return user == guild.owner

                reaction = None
                while True:
                    if str(reaction) == "✅":
                        await message.clear_reactions()
                        user = await self.client.fetch_user(int(id.content))
                        await ctx.guild.ban(user)
                        banning = discord.Embed(
                            description="**Banned this user**", color=0xFEE75C
                        )
                        await message.edit(embed=banning)
                    elif str(reaction) == "❌":
                        await message.clear_reactions()
                        cancel_ban = discord.Embed(
                            title="", description="Ban Cancelled", color=0xFF0000
                        )
                        await message.edit(embed=cancel_ban)
                        break
                    try:
                        reaction, user = await self.client.wait_for(
                            "reaction_add", timeout=50.0, check=check
                        )
                        await message.remove_reaction(reaction, user)
                    except:
                        break

#-------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def server_lock(self, ctx, *, reason=None):
        Emergency = discord.Embed(
            title="Confirmation!",
            description=":warning:Are you sure you want to perform this command? :warning: (This will lock all channels)",
            color=0x00C4B8,
        )
        message = await ctx.reply(embed=Emergency)
        await message.add_reaction("✅")
        await message.add_reaction("❌")

        def check(reaction, user):
            return user == ctx.author

        reaction = None
        while True:
            Emergency2 = discord.Embed(
                description="Proceeding with the lock down protocol...", color=0x24C41A
            )
            if str(reaction) == "✅":
                await message.clear_reactions()
                await message.edit(embed=Emergency2)
                async with ctx.typing():
                    await asyncio.sleep(2)
                    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                    overwrite.send_messages = False
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(
                        ctx.guild.default_role, overwrite=overwrite
                    )
                    embed = discord.Embed(
                        title="Server lockdown",
                        description=":no_entry:You are not muted this is a SERVER LOCK EMERGENCY:no_entry:",
                        color=0x00C4B8,
                    )
                    embed.add_field(
                        name="Reason/message :arrow_heading_down:",
                        value=f"{reason}",
                        inline=False,
                    )
                    await channel.send(embed=embed)
            elif str(reaction) == "❌":
                await message.clear_reactions()
                Emergency_cancel = discord.Embed(
                    description="Cancelling the lock down protocol", color=0xFF0000
                )
                await message.edit(embed=Emergency_cancel)
                break

            try:
                reaction, user = await self.client.wait_for(
                    "reaction_add", timeout=30.0, check=check
                )
                await message.remove_reaction(reaction, user)
            except:
                break

#-------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def server_unlock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True

        for channel in ctx.guild.text_channels:
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

            embed = discord.Embed(
                title="Server Unlocked",
                description="Thank you guys for waiting!",
                color=0x00C4B8,
            )
            await channel.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel, *, reason=None):
        if channel == None:
            channel = ctx.channel
            return
        else:
          channel = channel or ctx.channel
          overwrite = channel.overwrites_for(ctx.guild.default_role)
          overwrite.send_messages = False

          await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

          embed = discord.Embed(title="Channel lock", color=0x00C4B8)
          embed.add_field(
            name="Reason/message :arrow_heading_down:", value=f"{reason}", inline=False
        )
          await channel.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel
            return

        else:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

            embed = discord.Embed(title="Channel unlocked", color=0x00C4B8)
            await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["es", "Enable_slowmode"])
    @commands.has_permissions(manage_channels=True)
    async def enable(self, ctx, slowmode, seconds: int = None):
        if slowmode == None:
            await ctx.reply(
                f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant `enable slowmode`?"
            )
            return
        if slowmode != "slowmode":
            return
        if seconds == None:
            await ctx.reply("Well obv you need to set the seconds for the slowmode..")
            return

        else:
            await ctx.channel.edit(slowmode_delay=seconds)

            embed = discord.Embed(
                description=f"Slow mode is now set to {seconds} seconds! :white_check_mark:",
                color=0x00C4B8,
            )
            await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["ds", "Disable_slowmode"])
    @commands.has_permissions(manage_channels=True)
    async def disable(self, ctx, slowmode=None):
        if slowmode == None:
            await ctx.reply(
                f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant `disable slowmode`?"
            )
            return
        if slowmode != "slowmode":
            return
        await ctx.channel.edit(slowmode_delay=0)

        embed = discord.Embed(
            description=f"Slow mode is now disabled! :white_check_mark:", color=0x00C4B8
        )
        await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------

def setup(client):
  client.add_cog(cmd2(client))