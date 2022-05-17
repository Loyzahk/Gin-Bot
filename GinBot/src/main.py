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

##########################
welcomechannel = await client.fetch_channel(channel_id) # https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID
# Make sure you get the ID of your channel by right-clicking it and clicking `Copy ID`. Make sure developer mode is on!
@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
 # Customise the message below to what you want to send new users!
newUserMessage = """
You
can
put
your
multiline
message
here!
"""

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    try: 
        await client.send_message(member, newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)
    embed=discord.Embed(
        title="Welcome "+member.name+"!"
        description="We're so glad you're here!"
        color=discord.Color.green()
    )
        
    role = discord.utils.get(member.server.roles, name="name-of-your-role") #  Gets the member role as a `role` object
    await client.add_roles(member, role) # Gives the role to the user
    print("Added role '" + role.name + "' to " + member.name)

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
    embed=discord.Embed(
        title="😢 Goodbye "+member.name+"!",
        description="Until we meet again old friend." # A description isn't necessary, you can delete this line if you don't want a description.
        color=discord.Color.red() # There are lots of colors, you can check them here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
    )
########################
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
            type=discord.ActivityType.watching, name="g!"
        ),
    )


print("Im Ready My Lord Now 24/7")


bot.run("OTE3ODIyMzAyMDUyMjg2NDg0.GidZFN.Fsitg-tDu8plxWmJoKISV5OBHdMRMFiMLeBlWI")
