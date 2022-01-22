import discord, random, math
from discord.ext import commands
from datetime import datetime
from pytz import timezone
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

class BotStuffs(commands.Cog, name="Bot Things :robot:"):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    """Bot invite, ping, etc."""
    @commands.slash_command(guild_ids=guild)
    async def invite(self, ctx):
        """Shows invite info, like server/bot invites"""
        useravatar = ctx.interaction.user.avatar
        username = ctx.author
        embed=discord.Embed(title='Invites', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_author(name=username, icon_url=useravatar)
        embed.add_field(name="‎", value=":globe_with_meridians: [Invite To Owner's Server](https://discord.gg/CxtxXUcEfC)", inline=False)
        embed.add_field(name="‎", value=":robot: [Invite Bot To Your Server](https://discord.com/api/oauth2/authorize?client_id=486895118134018058&permissions=1644972474367&scope=bot%20applications.commands)", inline=False)
        tz = timezone("UTC")
        now = datetime.now(tz=tz)
        embed.set_footer(text=now.strftime("%b %w %Y • %H:%M UTC"))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(guild_ids=guild)
    async def ping(self, ctx) -> None:
        """Tests server latency by measuring how long it takes to edit a message."""
        embed = discord.Embed(title="Pong!", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.description = "Latency: testing..."
        b = datetime.utcnow()
        await ctx.respond(embed=embed)
        ping = math.floor((datetime.utcnow() - b).total_seconds() * 1000)
        embed.description = ""
        embed.add_field(name="Message Latency", value=f"`{ping}ms`")
        embed.add_field(name="API Latency", value=f"`{math.floor(self.bot.latency*1000)}ms`")
        await ctx.edit(embed=embed)
    
    @commands.slash_command(guild_ids=guild)
    async def version(self, ctx):
        """Shows bot version and changelog"""
        embed = discord.Embed(title="Bot version: "+ver, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="Changelog:", value="**"+ver+" includes:**\n\nUpdated to pycord\n\nFinishing up command transfers\n\nShaking and crying :sob:")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BotStuffs(bot))