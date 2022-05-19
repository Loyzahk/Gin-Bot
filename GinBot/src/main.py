from inspect import indentsize
import os
from typing import AsyncIterable
import requests
import json
import datetime
import discord
from discord.ext import commands
import asyncio

async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes
    
bot = commands.Bot(command_prefix = determine_prefix , description="Gin'Bot", help_command=None)
custom_prefixes = {}
#possibly using the json module to save and load
#or a database
default_prefixes = ['g!']
###########################################
@bot.command()
@commands.has_permissions(administrator=True)
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send(f"Prefixes set to `{prefixes}` ")
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

#######################
@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    if "Gin'scord" in message.content:
        await message.channel.send(f"Gin comunnity https://dsc.gg/ginebra")
    if "What's Ginebra?" in message.content:
        await message.channel.send(
            f"We're a company dedicated to dont answer questions."
        )
    if "Gin'ebra" in message.content:
        await message.channel.send(f"I'm ready my lord")
    else:
        await bot.process_commands(message)

@bot.command()
async def script(ctx):
    code = "14151617a"
    await ctx_send:("Please enter your code")
        await ctx_send:("web")
        

@bot.command()
async def av(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author.name
    avatar = discord.Embed(
        title=f"{member.name}'s avatar",
        color=0x000000,
        timestamp=ctx.message.created_at,
    )
    avatar.set_footer(text=f"Requested by {ctx.author.name} ")

    avatar.set_image(url=f"{member.avatar_url}".format(member.avatar_url))
    await ctx.send(embed=avatar)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(bot.latency * 1000)}ms")


@bot.command()
async def help(ctx):
    des = """
 :gem: **My commands are**:
 - "av" | **To see the avatar**
 - "ping" | **To check the network connection**
 - "kick/unkick" **Kick a member**
 - "ban/unban"  *Ban/Unban a member**
 - "wlc" | **Give the welcomes !** :smile: 
 """

    embed = discord.Embed(
        title="I'm Gin'ebra , Sup!!",
        descriptionurl="https://cdn.discordapp.com/avatars/917822302052286484/cc70991418a2c144387743956ea35f72.webp?size=1024x28",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=0x000000,
    )
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Gin'ebra Company",
        icon_url="https://cdn.discordapp.com/avatars/917822302052286484/cc70991418a2c144387743956ea35f72.webp?size=1024x256",
    )

    await ctx.send(embed=embed)
    await ctx.send("Thank you for call me! :tophat:")



# Wlc
@bot.command()
async def wlc(ctx):
    guild = ctx.guild
    gif = "https://tenor.com/view/peaky-blinders-john-shelby-gif-11333816"
    await ctx.send(f"**Welcome to {guild.name}!!!**:partying_face: :tophat: ")
    await ctx.send(gif)


## State


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(type=discord.ActivityType.watching, name="g!"),
    )


##ban/unban##


@bot.command()
async def ban(ctx, user: discord.User):
    guild = ctx.guild
    mbed = discord.Embed(
        title="Succes!", description=f"{user} has succesfully been banned."
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed=mbed)
        await guild.ban(user=user)


@bot.command()
async def unban(ctx, user: discord.User):
    guild = ctx.guild
    ashwinegay = discord.Embed(
        title="Succes!", description=f"{user} has succesfully been unbanned."
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed=ashwinegay)
        await guild.unban(user=user)


####


####purge /clear commands


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send("Cleared by {}".format(ctx.author.mention))
    await ctx.message.delete()


@purge.error
async def clear_error(ctx, error):
    if isinstance(error.command.MissingPermissions):
        await ctx.send("You don't have enough permissions!")


####


@bot.command()
async def fox(ctx):
    response = requests.get("https://some-random-api.ml/img/fox")  # Get-
    json_data = json.loads(response.text)  #  JSON

    embed = discord.Embed(color=0xFF9900, title="Random Fox")  #  Embed'a
    embed.set_image(url=json_data["link"])  #   Embed'a
    await ctx.send(embed=embed)  #  Embed


#######



################ROLES
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 0  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name="🔴"): 0,  # ID of the role associated with unicode emoji '🔴'.
            discord.PartialEmoji(name="🟡"): 0,  # ID of the role associated with unicode emoji '🟡'.
            discord.PartialEmoji(name="green", id=0): 0,  # ID of the role associated with a partial emoji's ID.
        }

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally, add the role.
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        try:
            # Finally, remove the role.
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
####
##

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Welcome {member.mention} to {guild.name}!"
            await guild.system_channel.send(to_send)
            
####
print("Im Ready My Lord Now 24/7")

bot.run("OTE3ODIyMzAyMDUyMjg2NDg0.GidZFN.Fsitg-tDu8plxWmJoKISV5OBHdMRMFiMLeBlWI")
