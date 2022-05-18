import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="g!", description="Gin'Bot", help_command=None)

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)


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
  I'm Gin'ebra, hello.
My commands are:
av = shows user avatar
ping = chek ping
kick/unkick
ban/unban
wlc
thanks for call me. :tophat: """

    embed = discord.Embed(
        title="Gin'ebra",
        descriptionurl="https://cdn.discordapp.com/avatars/917822302052286484/cc70991418a2c144387743956ea35f72.webp?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue(),
    )
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Gin'ebra Company",
        icon_url="https://cdn.discordapp.com/avatars/917822302052286484/cc70991418a2c144387743956ea35f72.webp?size=1024",
    )

    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(type=discord.ActivityType.watching, name="g!"),
    )


print("Im Ready My Lord Now 24/7")

bot.run("OTE3ODIyMzAyMDUyMjg2NDg0.GidZFN.Fsitg-tDu8plxWmJoKISV5OBHdMRMFiMLeBlWI")
