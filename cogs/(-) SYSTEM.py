import discord
from discord.ext import commands
from discord.ext.commands import (
    has_permissions,
    MissingPermissions,
    has_role,
    MissingRole,
    cooldown,
    BucketType,
    NotOwner,
    CommandNotFound,
    MissingRequiredArgument,
)
import json


class errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        guild = ctx.guild
        owner = self.client.get_user(798280308071596063)
        with open("prefix.json", "r", encoding="utf-8") as fp:
            custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
        if isinstance(error, commands.NotOwner):
            await ctx.reply(
                f"Woah there you can't do this command, only wari#3533 can do that. How did you know about this command..."
            )
        elif isinstance(error, MissingPermissions):
            await ctx.reply(
                f"Hey there **{ctx.author.name}**, I'm sorry but i can't let you perform this command as you need ``{error.missing_perms}`` permission for it!"
            )
        elif isinstance(error, MissingRequiredArgument):
            await ctx.reply(
                f"Hey there **{ctx.author.name}**, You missed an __argument__ while trying to perform this command, you need to mention ``{error.param.name}``"
            )
        elif isinstance(error, CommandNotFound):
            await ctx.reply(
                f"Hey there **{ctx.author.name}**, you tried excuting a command called ``{ctx.message.content}``, However there is no such command in brem, maybe you misspelled it, Either way check the bot's commands using ``{prefix}commands``"
            )
        elif isinstance(error, discord.Forbidden):
            emergency = discord.Embed(
                title="",
                description="I am not high enough to perform this command please try moving my role up the role list like in the images :white_check_mark:",
                color=0xFF0000,
            )
            emergency.set_image(
                url="https://discord.com/channels/960189413349019688/960189414477295632/964544873812357160"
            )
            emergency.set_image(
                url="https://discord.com/channels/960189413349019688/960189414477295632/964544997355556874"
            )
            await ctx.reply(embed=emergency)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(
                f"Sorry {ctx.author.name}, this command is on a %.2fs cooldown"
                % error.retry_after
            )
        else:
            em = discord.Embed(
                title=f"Error!",
                description=f"If this error keeps occuring, please contact {owner} regarding the issue! thank you!",
                color=0x0000,
            )
            em.add_field(
                name="Terminal error :arrow_heading_down:",
                value=f"``{str(error)}``",
                inline=True,
            )
            await ctx.send(embed=em)
            await ctx.message.add_reaction("❌")
            raise error


def setup(client):
    client.add_cog(errors(client))
