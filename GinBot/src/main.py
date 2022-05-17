from ast import Delete
import datetime
import pprint
import discord
from discord.enums import Status
from discord.ext import commands
import random
import os
import time
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import functools

bot = commands.Bot(command_prefix="g!", description="Gin'Bot", help_command=None)

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)


# mode is on!

#
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
    # if "By order of Gin company" in message.content:
    # await message.channel.send(f"By order of Gin company")
    else:
        await bot.process_commands(message)


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


#


@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(bot.latency * 1000)}ms")


# @bot.command() IM TRYING TO MAKE A CHANNEL Deleter
# async def nuke(ctx):
#   await ctx.delete


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Killing Strangers"
        ),
    )


print("Im Ready My Lord Now 24/7")


bot.run("OTE3ODIyMzAyMDUyMjg2NDg0.GidZFN.Fsitg-tDu8plxWmJoKISV5OBHdMRMFiMLeBlWI")
