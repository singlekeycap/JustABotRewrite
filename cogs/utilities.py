import discord, random
from discord.ext import commands
from cogs.constants import ver, dev, guild, log_channel, welcome_channel
from buttons import HelpButtons

class Utilities(commands.Cog, name="Utilities :hammer_pick:"):
    """General use tools for this bot."""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.slash_command(guild_ids=guild)
    async def help(self, ctx, cmd : str = None, page : int = 0):
        """Show all commands"""
        if cmd:
            command = self.bot.get_command(cmd)
            embed = discord.Embed(title="Help Menu", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.add_field(name=command.name, value=command.description)
        else:
            id = ctx.interaction.user.id
            cogs = self.bot.cogs
            max = len(self.bot.cogs)
            cogs = list(cogs.values())
            cog = cogs[page]
            embed = discord.Embed(title=cog.qualified_name, description=cog.description, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            for command in cog.walk_commands():
                embed.add_field(name=command.name, value=command.description)
            await ctx.respond(embed=embed, view = HelpButtons(self.bot, ctx, page, id))

def setup(bot):
    bot.add_cog(Utilities(bot))