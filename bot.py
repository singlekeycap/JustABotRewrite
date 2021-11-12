import discord
import os
import random
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

#Set constants
ver = "0.1b"
dev = "JustANobody#2107"

bot = discord.Bot()

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('------------------')
    print('Connected to '+str(len(bot.guilds))+' servers!')
    servers = list(bot.guilds)
    for i in range(len(servers)):
        members = str(servers[i].member_count)
        print(' '+ servers[i].name+' with '+members+' members!')

class Defaults():
    @bot.slash_command(guild_ids=[869694274319581184])
    async def hello(ctx):
        """Say hello to the bot"""
        await ctx.respond(f"Hello {ctx.author}!")

    @bot.slash_command(guild_ids=[869694274319581184])
    async def joined(ctx, member: discord.Member = None):
        user = member or ctx.author
        await ctx.respond(f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}")

class BotStuffs():
    @bot.slash_command(guild_ids=[869694274319581184])
    async def invite(ctx):
        """Shows invite info, like server/bot invites"""
        print(ctx.interaction.user)
        useravatar = "https://th.bing.com/th/id/R.388dae0c99ae8338e21c8a73edb00894?rik=MtJISwFjgf2ukg&riu=http%3a%2f%2fwallpapersdsc.net%2fwp-content%2fuploads%2f2017%2f10%2fBig-Rock-Wallpapers-HD.jpg&ehk=gss1k%2fanrDJYSekiNi%2fRKvoqernt270zzzUw0k66M4s%3d&risl=&pid=ImgRaw&r=0"
        username = ctx.author
        embed=discord.Embed(title='Invite Stuff', description="Here is all the invite stuff!", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_author(name=username, icon_url=useravatar)
        embed.add_field(name=":globe_with_meridians:", value="[Invite To Owner's Server](https://justanobody.me/server.html)", inline=False)
        embed.add_field(name=":robot:", value="[Invite Bot To Your Server](https://justanobody.me/bot.html)", inline=False)
        await ctx.respond(embed=embed)
    
    @bot.slash_command(guild_ids=[869694274319581184])
    async def ping(ctx):
        """Shows bot latency ping"""
        t = await ctx.respond('Ping!')
        ms = (t.created_at-ctx.message.created_at).total_seconds() * 1000
        await t.edit(content='Pong! Ping: {}ms'.format(int(ms)))
    
    @bot.slash_command(guild_ids=[869694274319581184])
    async def version(ctx):
        """Shows bot version and changelog"""
        embed = discord.Embed(title="Bot version: "+ver, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="Changelog:", value="**"+ver+" includes:**\n\nUpdated urls and name\n\nSlowly adding in new commands (new help menu possible)\n\nFixed r34 command (no tags necessary)")
        await ctx.respond(embed=embed)

bot.run(TOKEN)