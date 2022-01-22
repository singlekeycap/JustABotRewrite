import discord, random
from discord.ext import commands
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

class Math(commands.Cog, name="Math :heavy_division_sign:"):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    """Math Commands for the needy"""
    @commands.slash_command(guild_ids=guild)
    async def simple(self, ctx, operation : str):
        """Type 1st value, followed by [+, -, *, /] and then 2nd value"""
        title = "Here is your result!"
        color=discord.Color(random.randint(0x000000, 0xFFFFFF))
        if '+' in operation:
            operation.split('+')
            A=float(operation.split('+')[0])
            B=float(operation.split('+')[1])
            answer=A+B
            result=str(A)+"+"+str(B)+"="
        elif '-' in operation:
            operation.split('-')
            A=float(operation.split('-')[0])
            B=float(operation.split('-')[1])
            answer=A-B
            result=str(A)+"-"+str(B)+"="
        elif '*' in operation:
            operation.split('*')
            A=float(operation.split('*')[0])
            B=float(operation.split('*')[1])
            answer=A*B
            result=str(A)+'*'+str(B)+'='
        elif '/' in operation:
            operation.split('/')
            A=float(operation.split('/')[0])
            B=float(operation.split('/')[1])
            try:
                answer=A/B
                result=str(A)+'/'+str(B)+'='
            except ZeroDivisionError:
                title = "You can't do that!"
                color = 0xff0000
                result = "You tried to divide by zero..."
                answer = "**That's illegal math!**"
        embed=discord.Embed(title=title, color=color)
        embed.add_field(name=result, value=answer)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Math(bot))