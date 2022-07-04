import discord
from discord.ext import commands
from datetime import datetime

import os
import sys
import asyncio


def restart_bot():
    os.execv(sys.executable, ["python"] + sys.argv)


class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def restart(self, ctx):
        await ctx.send("Executing the restart protocol...")
        restart_bot()

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

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel, *, reason=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False

        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title="Channel lock", color=0x00C4B8)
        embed.add_field(
            name="Reason/message :arrow_heading_down:", value=f"{reason}", inline=False
        )
        await channel.send(embed=embed)

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

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            await ctx.reply(
                f"well {ctx.author.name}, you need to mention a channel for that!"
            )
            return

        else:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

            embed = discord.Embed(title="Channel unlocked", color=0x00C4B8)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mass_channel_delete(self, ctx, *, ids: str):
        list_of_ids = ids.split(" ")
        list_of_idsx = list(map(int, list_of_ids))
        success = 0

        for id in list_of_idsx:
            channel = self.client.get_channel(id)
            await channel.delete()
            success += 1

        embed = discord.Embed(
            description=f"**{str(success)}** Channels have been deleted by **{ctx.message.author}**",
            color=0x00C4B8,
        )
        await ctx.send(embed=embed)

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

    @commands.command(aliases=["c", "Purge", "p", "purge"])
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)
        await ctx.send(
            f"Deleted {amount} messages succesfully :white_check_mark:, `this message will be deleted in 5 seconds`",
            delete_after=5.0,
        )

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
                    read_messages=True,
                    view_channel=True,
                )
                embed = discord.Embed(
                    title="Created Role Successfully :white_check_mark:"
                )
                await ctx.send(embed=embed)

        embed = discord.Embed(
            description=f"**{member.mention}** has been muted\n**Responsible Moderator:** {ctx.author}",
            color=0x00C4B8,
        )
        embed.add_field(name="reason:", value=reason, inline=False)
        await member.add_roles(mutedRole)
        await ctx.send(embed=embed)
        await member.send(
            f"You have been muted from: **{guild.name}** reason: __{reason}__"
        )

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

    @commands.command(aliases=["rr", "Remove_role"])
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Removing ``{role}`` from ``{member}``...")
        await member.remove_roles(role)
        await ctx.send(f"Removed ``{role}`` from ``{member}``")

    @commands.command(aliases=["gr", "Give_role"])
    @commands.has_permissions(manage_roles=True)
    async def give_role(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Giving {member} ``{role}``...")
        async with ctx.typing():
            await asyncio.sleep(2)
        await member.add_roles(role)
        await ctx.send(f"Gave {member} the role ``{role}``")

    @commands.command(aliases=["Delete_role", "dr"])
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, role: discord.Role = None):
        await role.delete()
        await ctx.send(f"We have deleted ``{role}`` successfully.")

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

    @commands.command()
    async def nick(self, ctx, member: discord.Member, *, nick):
        await member.edit(nick=nick)
        await ctx.send(f"Nickname has been changed for ``{member}``")

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


def setup(client):
    client.add_cog(mod(client))
