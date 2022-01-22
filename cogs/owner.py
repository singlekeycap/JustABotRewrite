import discord, os
from discord.ext import commands
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

class OwnerOnly(commands.Cog, name="Owner Only :no_entry:"):
    """Bot owner commands only."""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.slash_command(guild_ids=guild)
    async def exec(self, ctx, exec:str):
        """Execute commands on local system"""
        if(ctx.interaction.user.id == 312319419240022017):
            cmd = os.popen(exec)
            output = cmd.read()
            if len(output) > 2000:
                with open('output.txt', 'w') as f:
                    f.write(output)
                    f.close()
                file = discord.File('output.txt')
                await ctx.respond(file = file)
                os.remove('output.txt')
            else:
                if exec[:4] == "curl":
                    await ctx.respond("```Check system to see if download is complete.```")
                elif output == "":
                    embed=discord.Embed(title='Exec results', color=discord.Color(0xFF0000))
                    embed.add_field(name="ERROR", value="Your command was either not correctly formatted or was just dumb!")
                    await ctx.respond(embed = embed)
                else:
                    await ctx.respond("```"+str(output)+"```") 
        else:
            embed=discord.Embed(title='Exec results', color=discord.Color(0xFF0000))
            embed.add_field(name="NO", value="You are not allowed to run exec!")
            await ctx.respond(embed = embed)

    @commands.slash_command(guild_ids=guild)
    async def img(self, ctx, name:str):
        """Send file from name"""
        if(ctx.interaction.user.id == 312319419240022017):
            try:
                file = discord.File(name)
                await ctx.respond(file = file)
            except Exception:
                embed=discord.Embed(title='File results', color=discord.Color(0xFF0000))
                embed.add_field(name="ERROR", value="The file isn't available on the system")
                await ctx.respond(embed = embed)
        else:
            embed=discord.Embed(title='File results', color=discord.Color(0xFF0000))
            embed.add_field(name="NO", value="You are not allowed to run img!")
            await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(OwnerOnly(bot))