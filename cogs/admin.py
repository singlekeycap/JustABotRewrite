import discord, asyncio
from discord.ext import commands
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

class Admin(commands.Cog, name="Admin Commands :hammer_pick:"):
    """Commands that only server admins can run."""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.slash_command(guild_ids=guild)
    async def ban(self, ctx, user : discord.Member, reason : str = None, msgdelete : int = 0):
        """Bans a user"""
        if isinstance(user, int):
            user = await self.bot.fetch_user(user)
        if msgdelete > 7:
            msgdelete = 7
        name = user.name
        if ctx.interaction.user.guild_permissions.ban_members:
            try:
                await ctx.guild.ban(user, reason=reason, delete_message_days=msgdelete)
                embed = discord.Embed(title="Ban succeeded", description="Successfully banned "+name, color=discord.Color(0x32CD32))
                embed.add_field(name="Reason", value=reason)
                await ctx.respond(embed=embed)
            except Exception:
                embed = discord.Embed(title="Ban failed", description="Hey! I can't ban that person!", color=discord.Color(0xFF0000))
                embed.add_field(name="‎", value="Check my perms or role hierarchy.")
                msg = await ctx.respond(embed=embed)
                await asyncio.sleep(5)
                await msg.delete_original_message()
                
        else:
            embed = discord.Embed(title="Ban failed", description="Hey! I can't ban that person!", color=discord.Color(0xFF0000))
            embed.add_field(name="‎", value="YOU DON'T HAVE PERMS :joy::joy::joy:.")
            msg = await ctx.respond(embed=embed)
            await asyncio.sleep(5)
            await msg.delete_original_message()

def setup(bot):
    bot.add_cog(Admin(bot))