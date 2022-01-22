#Import requirements
import discord, os, random, asyncio
from discord.ext import tasks
from datetime import datetime
from dotenv import load_dotenv

#Import constants
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
bot = discord.Bot("jt!", intents=intents)

#Import cogs
cogs = ["cogs.botstuff", "cogs.math", "cogs.memes", "cogs.fun", "cogs.nsfw", "cogs.owner", "cogs.utilities", "cogs.admin"]
for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('------------------')
    print('Connected to '+str(len(bot.guilds))+' servers!')
    for srv in bot.guilds:
        guild.append(srv.id)
        members = str(srv.member_count)
        print(' '+ srv.name+' with '+members+' members!')
    channel = bot.get_channel(log_channel)
    embed = discord.Embed(title="Bot started!", description=datetime.now().strftime('%A, %B %d, %Y at %H:%M:%S UTC-5 (Eastern Standard Time)'), color=discord.Color(0x00FF00))
    await channel.send(embed=embed)

@bot.event
async def on_member_join(member):
    if member.guild.id == 934093023191633930:
        mem = str(member.id)
        embed=discord.Embed(title="Welcome to Nobody's Void", description="Make sure to check out rules, and have fun!", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        channel = bot.get_channel(welcome_channel)
        await channel.send(content="<@"+mem+">", embed=embed)

@tasks.loop(seconds = 20)
async def myLoop():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(name=str(len(bot.guilds))+' guilds', type=3))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game(name='Need help? /help'))

myLoop.start()

bot.run(TOKEN)