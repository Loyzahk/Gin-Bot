
import datetime
import discord
from discord.ext import commands
import random

client = discord.Client()

bot = commands.Bot(command_prefix='t!',
                   description="TSR Bot",
                   help_command=None)


@bot.command()  # Ping Pong
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def wlc(ctx):
    await ctx.send('Welcome! :heart: ')


@bot.command()
async def owner(ctx):
    await ctx.send('The owner is the TSR Staff Team')


@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        (
            'Loyzan noob'

        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command()
async def contact(ctx):
    await ctx.send(
        'if you find a issue/suggest, you can report/suggest to the owner (Discord:Ahk#7009 or jap#4777 or Python#0404 )'
    )


@bot.command()
async def info(ctx):
    await ctx.send(
        'https://tsrtransformice-survivor-ranking9.webnode.com/about-us/ https://discord.gg/AjWDk2HWAa'
    )


@bot.command()
async def help(ctx):
    des = """
   TSR is here!
  > Prefix:  t!\n
  > contact : If you want suggest or report a issue send to Discord: Ahk#7009 or jap#4777 or Python#0404 \n
  > rank : Show you the actual Global Rank (disabled)\n
  > esrank : Show you the actual ES Rank\n
  > rorank : Show you the actual RO Rank\n
  > brrank : Show you the actual BR Rank\n
  > plrank : Show you the actual PL Rank\n
  > trrank : Show you the actual TR Rank\n
  > efrank : Show you the actual EN/FR Rank\n
  > rurank : Show you the actual RU Rank\n
  > arrank : Show you the actual AR Rank\n
  """
    embed = discord.Embed(
        title="Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def esrank(ctx):
    des = """
  If some position was changed pls notify me :D
 
  >  1: Koroca#5003
  >  2: Vicxor#9698(Shisui#2033)
  >  3: Lalechw#0000
  >  4: Se_co#2542
  >  5: Danividalm#0000
  >  6: Hyk#6465
  >  7: Johan#7385
  >  8: Tunblex#3049
  >  9: Vacante
  > 10: Vacante
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/es-server/
  """
    embed = discord.Embed(
        title="ES Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def rorank(ctx):
    des = """ 
  If some position was changed pls notify me :D
  > :one: : :crown: Zjr#6660
  > :two: : :gem: Japq#5404 
  > :three: : :abacus: Andybst#0000
  > :four: : :chess_pawn: Ceagy#7796 
  > :five: : :chess_pawn: Nuratul#0000 
  > :six: : :chess_pawn: Marianxpro#0621 
  > :seven: : :chess_pawn: Dukers#8068
  > :eight: : :chess_pawn: Deus#3913 
  > :nine: : :chess_pawn: Vacant
  > :keycap_ten: : :chess_pawn: Vacant
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/ro-server/
  """
    embed = discord.Embed(
        title="RO Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def plrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: MrKleer#8542
  >  2: Turke11#2003
  >  3: Offsite#3120
  >  4: Fgderdfgreg2#3145
  >  5: I12#2125
  >  6: Dark_rose#5530
  >  7: Hard#3022
  >  8: Adamin#8091
  >  9: Autumn#0740
  > 10: Szczurpk#5642
                    You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/pl-server/
          """
    embed = discord.Embed(
        title="PL Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def efrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: Eztiermice#8930
  >  2: Dondon#3628
  >  3: +Despera#0000
  >  4: Somrak#8801
  >  5: Brunelle#8692
  >  6: Soarens#0000
  >  7: Prroblackops#0000
  >  8: Ougoundare#0000
  >  9: Loulougie#0000
  
  > 10: Vacante.
                    You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/en-fr-server/
          """
    embed = discord.Embed(
        title="EN/FR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def brrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: Black_xx#4260
  >  2: Chaos#2589
  >  3: Y_y#2506 (Onomatopeia#6666)
  >  4: Univ3rse#0000 (Aandreelucas#0000)
  >  5: Rian#0488
  >  6: Raizen#7195
  >  7: Pepoou#4831
  >  8: Arieswar#5705
  >  9: Littlearenan#0000
  > 10: Prax#8896
                    You can verify that in :
 https://tsrtransformice-survivor-ranking9.webnode.com/br-server/          
    """

    embed = discord.Embed(
        title="BR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def arrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: Ex_huh#9630 (Shzya1)
  >  2: Kez#3085 (Ool#7433)
  >  3: Darknight#9998 (Svrmz#0000)
  >  4: Stop#4643
  >  5: Ans#2559
  >  6: King_aymane#8137
  >  7: Eyaddeeba#1831 (Mickey#6771)
  >  8: Abo_jood#8655
  >  9: Xxmareem#0000
  > 10: Xen23#7297
                    You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/ar-server/          
    """

    embed = discord.Embed(
        title="AR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def trrank(ctx):
    des = """ 
  If some position was changed pls notify me :D
  >  1: Gracc#6101
  >  2: Arsenic#2236
  >  3: Rekkles#6542
  >  4: Caps#8846
  >  5: Wubzyyy#0000
  >  6: Alwesh#0000
  >  7: Yestoprak#0000
  >  8: Sunmama#0000
  >  9: Surviv_or1#0000
  > 10: Judgetr#2707
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/tr-server/
  """
    embed = discord.Embed(
        title="TR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def rurank(ctx):
    des = """ 
  If some position was changed pls notify me :D
  >  1: Maximire#0000(+Invitman#0000)
  >  2: Jopyna#1148
  >  3: Zadrot777#4422
  >  4: N1to4ka#5857
  >  5: Monawwwka#2709
  >  6: Kvicls#2000
  >  7: Crazy#8138
  
  >  8: Vacant.
  >  9: Vacant.
  > 10: Vacant.
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/tr-server/
  """
    embed = discord.Embed(
        title="RU Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def rank(ctx):
    des = """ 
  If some position was changed pls notify me :D
 > 1: Alecrac#0000 (ES)
 > 2: Eztiermice#8930 (EN/FR)
 > 3: Vicxor#9698 (ES) 
 > 4: Injustice#1781 (ES)
 > 5: Prax#8896 (BR)
 > 6: Mr_noseybonk (ES)
 > 7: +Despera#0000 (EN/FR)
  
  >  8: Vacante 
  >  9: Vacante
  > 10: Vacante
              You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/ranking/
 
  """
    embed = discord.Embed(
        title="Global Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )

    await ctx.send(embed=embed)


@bot.command() 
async def efrefs(ctx):
    await ctx.send('https://prnt.sc/22fcdsz') #EN FR


@bot.command()
async def plrefs(ctx):
    await ctx.send('https://prnt.sc/22fco4h') #PL


@bot.command()
async def brrefs(ctx):
    await ctx.send('https://prnt.sc/22fcut3') #BR


@bot.command()
async def esrefs(ctx):
    await ctx.send('https://prnt.sc/22ff319') #ES


@bot.command()
async def rorefs(ctx):
    await ctx.send('https://prnt.sc/22ffhqp') #RO

@bot.command()
async def arrefs(ctx):
    await ctx.send('https://prnt.sc/22ff58g') #AR


@bot.command()
async def trrefs(ctx):
    await ctx.send('https://prnt.sc/22fe5wf') #TR


@bot.command()
async def rurefs(ctx):
    await ctx.send('https://prnt.sc/22fecef') #RU


print('Japq noob')


bot.run('OTE3MTI1NjQzNzgxNjg5NDA0.Ya0J0A.UHC52cE4OZf7dv5Depk0CX9fWtE')


################################
##                            ##
##   ######     #    #     #  ##
##   #         # #    #  #    ##
##   #  ###   #   #     #     ##
##   #    #  ## # ##   #      ##
##   ###### #       # #       ##
##                            ##
################################

import datetime
import discord
from discord.ext import commands
import random

client = discord.Client()

bot = commands.Bot(command_prefix='t!',
                   description="TSR Bot",
                   help_command=None)


@bot.command()  # Ping Pong
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def wlc(ctx):
    await ctx.send('Welcome! :heart: ')


@bot.command()
async def owner(ctx):
    await ctx.send('The owner is the TSR Staff Team')


@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        (
            'Loyzan noob'

        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command()
async def contact(ctx):
    await ctx.send(
        'if you find a issue/suggest, you can report/suggest to the owner (Discord:Ahk#7009 or jap#4777 or Python#0404 )'
    )


@bot.command()
async def info(ctx):
    await ctx.send(
        'https://tsrtransformice-survivor-ranking9.webnode.com/about-us/ https://discord.gg/AjWDk2HWAa'
    )


@bot.command()
async def help(ctx):
    des = """
   TSR is here!
  > Prefix:  t!\n
  > contact : If you want suggest or report a issue send to Discord: Ahk#7009 or jap#4777 or Python#0404 \n
  > rank : Show you the actual Global Rank (disabled)\n
  > esrank : Show you the actual ES Rank\n
  > rorank : Show you the actual RO Rank\n
  > brrank : Show you the actual BR Rank\n
  > plrank : Show you the actual PL Rank\n
  > trrank : Show you the actual TR Rank\n
  > efrank : Show you the actual EN/FR Rank\n
  > rurank : Show you the actual RU Rank\n
  > arrank : Show you the actual AR Rank\n
  """
    embed = discord.Embed(
        title="Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def esrank(ctx):
    des = """
  If some position was changed pls notify me :D
 
  >  1: Koroca#5003
  >  2: Vicxor#9698(Shisui#2033)
  >  3: Lalechw#0000
  >  4: Se_co#2542
  >  5: Danividalm#0000
  >  6: Hyk#6465
  >  7: Johan#7385
  >  8: Tunblex#3049
  >  9: Vacante
  > 10: Vacante
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/es-server/
  """
    embed = discord.Embed(
        title="ES Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def rorank(ctx):
    des = """ 
  If some position was changed pls notify me :D
  > :one: : :crown: Zjr#6660
  > :two: : :gem: Japq#5404 
  > :three: : :abacus: Andybst#0000
  > :four: : :chess_pawn: Ceagy#7796 
  > :five: : :chess_pawn: Nuratul#0000 
  > :six: : :chess_pawn: Marianxpro#0621 
  > :seven: : :chess_pawn: Dukers#8068
  > :eight: : :chess_pawn: Deus#3913 
  > :nine: : :chess_pawn: Vacant
  > :keycap_ten: : :chess_pawn: Vacant
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/ro-server/
  """
    embed = discord.Embed(
        title="RO Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def plrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: MrKleer#8542
  >  2: Turke11#2003
  >  3: Offsite#3120
  >  4: Fgderdfgreg2#3145
  >  5: I12#2125
  >  6: Dark_rose#5530
  >  7: Hard#3022
  >  8: Adamin#8091
  >  9: Autumn#0740
  > 10: Szczurpk#5642
                    You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/pl-server/
          """
    embed = discord.Embed(
        title="PL Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def efrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: Eztiermice#8930
  >  2: Dondon#3628
  >  3: +Despera#0000
  >  4: Somrak#8801
  >  5: Brunelle#8692
  >  6: Soarens#0000
  >  7: Prroblackops#0000
  >  8: Ougoundare#0000
  >  9: Loulougie#0000
  
  > 10: Vacante.
                    You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/en-fr-server/
          """
    embed = discord.Embed(
        title="EN/FR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def brrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: Black_xx#4260
  >  2: Chaos#2589
  >  3: Y_y#2506 (Onomatopeia#6666)
  >  4: Univ3rse#0000 (Aandreelucas#0000)
  >  5: Rian#0488
  >  6: Raizen#7195
  >  7: Pepoou#4831
  >  8: Arieswar#5705
  >  9: Littlearenan#0000
  > 10: Prax#8896
                    You can verify that in :
 https://tsrtransformice-survivor-ranking9.webnode.com/br-server/          
    """

    embed = discord.Embed(
        title="BR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def arrank(ctx):
    des = """
  If some position was changed pls notify me :D
  >  1: Ex_huh#9630 (Shzya1)
  >  2: Kez#3085 (Ool#7433)
  >  3: Darknight#9998 (Svrmz#0000)
  >  4: Stop#4643
  >  5: Ans#2559
  >  6: King_aymane#8137
  >  7: Eyaddeeba#1831 (Mickey#6771)
  >  8: Abo_jood#8655
  >  9: Xxmareem#0000
  > 10: Xen23#7297
                    You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/ar-server/          
    """

    embed = discord.Embed(
        title="AR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def trrank(ctx):
    des = """ 
  If some position was changed pls notify me :D
  >  1: Gracc#6101
  >  2: Arsenic#2236
  >  3: Rekkles#6542
  >  4: Caps#8846
  >  5: Wubzyyy#0000
  >  6: Alwesh#0000
  >  7: Yestoprak#0000
  >  8: Sunmama#0000
  >  9: Surviv_or1#0000
  > 10: Judgetr#2707
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/tr-server/
  """
    embed = discord.Embed(
        title="TR Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def rurank(ctx):
    des = """ 
  If some position was changed pls notify me :D
  >  1: Maximire#0000(+Invitman#0000)
  >  2: Jopyna#1148
  >  3: Zadrot777#4422
  >  4: N1to4ka#5857
  >  5: Monawwwka#2709
  >  6: Kvicls#2000
  >  7: Crazy#8138
  
  >  8: Vacant.
  >  9: Vacant.
  > 10: Vacant.
                  You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/tr-server/
  """
    embed = discord.Embed(
        title="RU Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )
    await ctx.send(embed=embed)


@bot.command()
async def rank(ctx):
    des = """ 
  If some position was changed pls notify me :D
 > 1: Alecrac#0000 (ES)
 > 2: Eztiermice#8930 (EN/FR)
 > 3: Vicxor#9698 (ES) 
 > 4: Injustice#1781 (ES)
 > 5: Prax#8896 (BR)
 > 6: Mr_noseybonk (ES)
 > 7: +Despera#0000 (EN/FR)
  
  >  8: Vacante 
  >  9: Vacante
  > 10: Vacante
              You can verify that in :
https://tsrtransformice-survivor-ranking9.webnode.com/ranking/
 
  """
    embed = discord.Embed(
        title="Global Ranking",
        url="https://cdn.discogfgfgfgfrdapp.com/avatars/915204948961165392/401b786f6282ed2afb305875706794a6.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.set_footer(text="Requested by: {}".format(ctx.author.name))
    embed.set_author(
        name="Transformice Survivor Rank",
        icon_url="https://cdn.discordapp.com/avatars/917125643781689404/8e7223452ab6bdb7d739dfca48ae4d5b.png?size=1024%22"
    )

    await ctx.send(embed=embed)


@bot.command() 
async def efrefs(ctx):
    await ctx.send('https://prnt.sc/22fcdsz') #EN FR


@bot.command()
async def plrefs(ctx):
    await ctx.send('https://prnt.sc/22fco4h') #PL


@bot.command()
async def brrefs(ctx):
    await ctx.send('https://prnt.sc/22fcut3') #BR


@bot.command()
async def esrefs(ctx):
    await ctx.send('https://prnt.sc/22ff319') #ES


@bot.command()
async def rorefs(ctx):
    await ctx.send('https://prnt.sc/22ffhqp') #RO

@bot.command()
async def arrefs(ctx):
    await ctx.send('https://prnt.sc/22ff58g') #AR


@bot.command()
async def trrefs(ctx):
    await ctx.send('https://prnt.sc/22fe5wf') #TR


@bot.command()
async def rurefs(ctx):
    await ctx.send('https://prnt.sc/22fecef') #RU


print('Japq noob')


bot.run('OTE3MTI1NjQzNzgxNjg5NDA0.Ya0J0A.UHC52cE4OZf7dv5Depk0CX9fWtE')


################################
##                            ##
##   ######     #    #     #  ##
##   #         # #    #  #    ##
##   #  ###   #   #     #     ##
##   #    #  ## # ##   #      ##
##   ###### #       # #       ##
##                            ##
################################
