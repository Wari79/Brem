import discord
from discord.ext import commands

import json


class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        owner = self.client.get_user(798280308071596063)
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = discord.Embed(title=f"Sup '{guild.name}'!", color=0x00C4B8)
                embed.add_field(
                    name="Configuration :arrow_heading_down:",
                    value="Hello there and thank you guys for inviting me in! my default prefix is `*` and say `*commands` to get a list of commands that you can use! **You can change my prefix by saying `*change_prefix [prefix]` if you wish to**",
                    inline=False,
                )

                with open("prefix.json", "r") as f:
                    prefixes = json.load(f)
                    prefixes[str(guild.id)] = "*"
                with open("prefix.json", "w") as f:
                    json.dump(prefixes, f, indent=4)

            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/901397587758813254/901425889210941450/logo.png"
            )
            embed.set_footer(text=f"{owner} <3")
            await channel.send(embed=embed)

            invite = await ctx.channel.create_invite(max_age=0, max_uses=0)

            await owner.send(
                f"Brem joined a new server called {guild.name}, we hittin that, right wari :fire:?"
            )
            await owner.send(
                f"info: **name** ``{guild.name}``, **id** ``{guild.id}``, **owner** ``{guild.owner}``, **member count** ``{guild.member_count}``"
            )
            break

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        owner = self.client.get_user(798280308071596063)
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

            prefixes.pop(str(guild.id))

            with open("prefix.json", "w") as f:
                json.dump(prefixes, f, indent=4)
        await owner.send(
            f"Brem left a server called **{guild.name}** ``({guild.id})``, owner: **{guild.owner}** ``({guild.owner.id})``"
        )


def setup(client):
    client.add_cog(welcome(client))
