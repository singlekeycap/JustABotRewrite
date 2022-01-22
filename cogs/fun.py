import discord, random
from discord.ext import commands
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

class Fun(commands.Cog, name="Fun :smile:"):
    """Fun commands (use with friends)"""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(guild_ids=guild)
    async def choose(self, ctx, choices : str):
        """Choose between things (separated by commas)"""
        choices = choices.split(",")
        await ctx.respond(random.choice(choices))
    
    @commands.slash_command(guild_ids=guild)
    async def gay(self, ctx, user : discord.Member):
        """Are you gay? (meme)"""
        level = random.randint(1,100)
        embed=discord.Embed(title='Gay Meter 2000', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name='{0.name} is...'.format(user), value=str(level)+'% gay!')
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))