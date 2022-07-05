import discord
from discord.ext import commands
import json
import asyncio
from datetime import datetime




class cmd1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx, *, member: discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title="Identification card", color=0x00C4B8)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=member.avatar_url)
        embed.add_field(name="User's name:", value=f"{member.name}", inline=False)
        embed.add_field(
            name="Discriminator/tag:", value=f"{member.discriminator}", inline=False
        )
        embed.add_field(name="Bot", value=f"{member.bot}", inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="User's id:", value=f"{member.id}", inline=False)
        if len(member.roles) > 1:
            role_string = " ".join([r.mention for r in member.roles][1:])
            embed.add_field(
                name="Roles [{}]".format(len(member.roles) - 1),
                value=role_string,
                inline=False,
            )
            embed.add_field(
                name="Member Joined guild at:",
                value=f"{member.joined_at.strftime('%A, %B %d %Y @ %I:%M %p')}",
                inline=False)
            embed.add_field(
                name="Account creation date:",
                value=f"{member.created_at.strftime('%A, %B %d %Y @ %I:%M %p')}",
                inline=False,
            )
            hypesquad_class = (
                str(member.public_flags.all())
                .replace("[<UserFlags.", "")
                .replace(">]", "")
                .replace("_", " ")
                .replace(":", "")
                .title()
            )
            hypesquad_class = "".join([i for i in hypesquad_class if not i.isdigit()])
            embed.add_field(name="Flags", value=f"{hypesquad_class}", inline=False)
            embed.add_field(
                name="Avatar",
                value=f"[Link to member's avatar]({member.avatar_url})",
                inline=False,
            )
            await ctx.reply(embed=embed)
          
#----------------------------------------------------------
          
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            await ctx.send(
                "You didn't mention a member so i will execute the command on you"
            )

        embed = discord.Embed(
            title=f"{member}'s Avatar",
            description=f"[Click here to download (pfft creep if you would..)]({member.avatar_url})", color=0x00c4b8
        )
        embed.set_image(url=member.avatar_url)
        embed.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
        )
        await ctx.reply(embed=embed)

#----------------------------------------------------------
      
    @commands.command(aliases=["srvr", "SERVER", "sr", "Server", "s", "S"])
    async def server(self, ctx):
        list1 = discord.Embed(title=f"Information on {ctx.guild.name}", color=0x00C4B8)
        list1.add_field(
            name=":necktie: Owner of server:",
            value=f"```{ctx.guild.owner}```",
            inline=False,
        )
        list1.add_field(
            name=":1234: Owner's ID:", value=f"```{ctx.guild.owner.id}```", inline=False
        )
        list1.add_field(
            name=":abacus: Server id:", value=f"```{ctx.guild.id}```", inline=False
        )
        list1.add_field(
            name=":globe_with_meridians: Server Region:",
            value=f"```{str(ctx.guild.region)}```",
            inline=False,
        )
        list1.add_field(
            name=":birthday: Server's Creation Date:",
            value=f"```{ctx.guild.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}```",
            inline=False,
        )
        list1.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
        )
        list1.set_thumbnail(url=ctx.guild.icon_url)

        list2 = discord.Embed(title="Statistics and Numbers [USERS]", color=0x00C4B8)
        list2.add_field(
            name=":family_mmb: All Member Count:",
            value=f"```{ctx.guild.member_count}```",
            inline=True,
        )
        list2.add_field(
            name=":coat: Total Members (no bots):",
            value=f"```{sum(not member.bot for member in ctx.guild.members)}```",
            inline=False,
        )
        list2.add_field(
            name=":green_circle: Total Online Members:",
            value=f"```{sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)}```",
            inline=False,
        )
        list2.add_field(
            name=":crescent_moon: Total Idle Members:",
            value=f"```{sum(member.status==discord.Status.idle and not member.bot for member in ctx.guild.members)}```",
            inline=False,
        )
        list2.add_field(
            name=":no_entry: Total Do Not Disturb Members:",
            value=f"```{sum(member.status==discord.Status.do_not_disturb and not member.bot for member in ctx.guild.members)}```",
            inline=False,
        )
        list2.add_field(
            name=":red_circle: Total Offline Members:",
            value=f"```{sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)}```",
            inline=False,
        )
        list2.add_field(
            name=":robot: Total Bots",
            value=f"```{sum(member.bot for member in ctx.guild.members)}```",
            inline=False,
        )
        list2.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
        )

        list3 = discord.Embed(
            title="Statistics and Numbers [ROLES/EMOJIS]", color=0x00C4B8
        )
        list3.add_field(
            name=":man_bowing: Default Role",
            value=f"```{ctx.guild.default_role}```",
            inline=False,
        )
        list3.add_field(
            name=":police_car: Role(s):",
            value=f"```{len(ctx.guild.roles)}```",
            inline=False,
        )
        list3.add_field(
            name=":stuck_out_tongue_winking_eye: Emojis:",
            value=f"```{len(ctx.guild.emojis)}```",
            inline=False,
        )
        list3.add_field(
            name=":lock: Emoji Limit",
            value=f"```{ctx.guild.emoji_limit}```",
            inline=False,
        )
        list3.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
        )

        list4 = discord.Embed(
            title="Statistics and Numbers [CHANNELS/BOOSTS]", color=0x00C4B8
        )
        list4.add_field(
            name=":keyboard: Total Channels:",
            value=f"```{len(ctx.guild.channels)}```",
            inline=True,
        )
        list4.add_field(
            name=":computer: Total Categories:",
            value=f"```{len(ctx.guild.categories)}```",
            inline=True,
        )
        list4.add_field(
            name=":mouse_three_button: Total Text Channels",
            value=f"```{len(ctx.guild.text_channels)}```",
            inline=True,
        )
        list4.add_field(
            name=":microphone2: Total Voice Channels",
            value=f"```{len(ctx.guild.voice_channels)}```",
            inline=True,
        )
        list4.add_field(
            name=":rocket: Boost Level",
            value=f"```{ctx.guild.premium_tier}```",
            inline=True,
        )
        list4.add_field(
            name=":rocket: Boost Count",
            value=f"```{ctx.guild.premium_subscription_count}```",
            inline=True,
        )
        list4.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
        )

        lists = [list1, list2, list3, list4]
        async with ctx.typing():
            await asyncio.sleep(2)
        message = await ctx.reply(embed=list1)
        await message.add_reaction("⏮")
        await message.add_reaction("◀")
        await message.add_reaction("▶")
        await message.add_reaction("⏭")

        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
            if str(reaction) == "⏮":
                i = 0
                await message.edit(embed=lists[i])
            elif str(reaction) == "◀":
                if i > 0:
                    i -= 1
                    await message.edit(embed=lists[i])
            elif str(reaction) == "▶":
                if i < 3:
                    i += 1
                    await message.edit(embed=lists[i])
            elif str(reaction) == "⏭":
                i = 3
                await message.edit(embed=lists[i])

            try:
                reaction, user = await self.client.wait_for(
                    "reaction_add", timeout=50.0, check=check
                )
                await message.remove_reaction(reaction, user)
            except:
                break

        await message.clear_reactions()

#----------------------------------------------------------

    @commands.command()
    async def bot(self, ctx):
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed = discord.Embed(title="Brem's Information", color=0x00C4B8)
        embed.add_field(name="Bot's name", value="``Brem``", inline=True)
        embed.add_field(name="Bot's Tag", value="``6606``", inline=True)
        embed.add_field(name="Bot's ID", value="``901389809283629067``", inline=True)
        embed.add_field(name="Bot's default prefix", value="``*``", inline=True)
        embed.add_field(
            name="Bot's Creation Date",
            value="``Saturday, October 23 2021 @ 08: 41:17 AM``",
            inline=True,
        )
        embed.add_field(
            name="Uptime",
            value=f"``{days}d, {hours}h, {minutes}m, {seconds}s``",
            inline=True,
        )
        embed.add_field(
            name="Number Of Servers bot is in",
            value=f"``{len(self.client.guilds)} servers``",
            inline=True,
        )
        embed.add_field(name="Brem's coder/creator", value="``Ham#5550``", inline=True)
        embed.add_field(
            name="Ping", value=f"`{round(self.client.latency * 1000)} ms`", inline=True
        )
        embed.add_field(
            name="Valuable links",
            value=f"[top.gg](https://top.gg/bot/901389809283629067/vote) | [bot invitation](https://discord.com/api/oauth2/authorize?client_id=901389809283629067&permissions=8&scope=bot)",
            inline=True,
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/901397587758813254/901425889210941450/logo.png"
        )
        embed.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

#----------------------------------------------------------

    @commands.command(aliases=["invite", "Invite"])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def create(self, ctx, invite=None):
        if invite == None:
            await ctx.reply(
                f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``create invite`` or ``invite`` ?"
            )
            return

        if invite != "invite":
            return
        invite = await ctx.channel.create_invite(max_age=0, max_uses=0)
        await ctx.reply("You sure you want to perform this command? **yes/no**")

        msg = await self.client.wait_for(
            "message",
            check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,
        )
        if msg.content.lower() == "yes":
            message = await ctx.reply("Creating your invite link...")
            async with ctx.typing():
                await asyncio.sleep(3)
            await message.edit(content="Damn why is this hard ffs...")

            async with ctx.typing():
                await asyncio.sleep(3)
            await message.edit(content="mehh almost there...")

            async with ctx.typing():
                await asyncio.sleep(4)
            await message.edit(content="Done!", delete_after=7.0)
            await ctx.send(f"**Here it is!** {ctx.author.name}'s invite: {invite}")
            return

        else:
            message2 = ctx.reply("Cancelling command then...")
            async with ctx.typing():
                await asyncio.sleep(3)
            await message2.edit(
                "Command cancelled succesfully :white_check_mark:", delete_after=7.0
            )

#----------------------------------------------------------

    @commands.command(alliases=["Information", "informations", "Informations"])
    async def information(self, ctx, help=None):
      guild = ctx.guild
      with open("prefix.json", "r", encoding="utf-8") as fp:
          custom_prefixes = json.load(fp)
          prefix = custom_prefixes[f"{guild.id}"]
      if help == None:
            await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``information help`` ?"
        )
            return
      if help != "help":
          return
      embed = discord.Embed(title="", color=0x00C4B8)
      embed.add_field(
        name=f"`{prefix}info (@member/id)`",
        value="Which gives the user an information card about his/her account on discord however if you mention a member or their id, you will recieve an identification card of them.",
        inline=False,
    )
      
      embed.add_field(name=f"`{prefix}avatar (@member/id)`", value="Sends the requested avatar of you or the member you mentioned.", inline=False)

      embed.add_field(name=f"`{prefix}server`", value="Gives you detailed pages of the server's information and statistics", inline=False)

      embed.add_field(name=f"`{prefix}bot`", value="Gives a detailed information about brem's usage and statistics.", inline=False)

      
      embed.add_field(name=f"`{prefix}create invite`", value="This command is fun and useful, creates an invite to the server that you excuted the command at.", inline=False)      
      
      await ctx.reply(embed=embed)


def setup(client):
  client.add_cog(cmd1(client))