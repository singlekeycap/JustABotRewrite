import discord, random, urllib3, certifi, substring, requests
from discord.ext import commands
from bs4 import BeautifulSoup
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

class NSFW(commands.Cog, name="NSFW :underage:"):
    """NSFW stuff. Only execute in NSFW channels."""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(guild_ids=guild)
    async def neko(self, ctx):
        """Gives a neko based on NSFW or not"""
        if ctx.interaction.channel.nsfw:
            http = urllib3.PoolManager(
                cert_reqs='CERT_REQUIRED',
                ca_certs=certifi.where()
            )
            neko = http.request('GET', 'https://nekos.life/api/v2/img/lewd')
            neko = str(neko.data)
            neko = substring.substringByChar(neko, startChar='h', endChar='g')
            embed = discord.Embed(title='Lewds!', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.set_image(url=neko)
            embed.set_footer(text='Image from nekos.life/lewd')
            await ctx.respond(embed=embed)
        else:
            http = urllib3.PoolManager(
                cert_reqs='CERT_REQUIRED',
                ca_certs=certifi.where()
            )
            neko = http.request('GET', 'https://nekos.life/api/v2/img/neko')
            neko = str(neko.data)
            neko = substring.substringByChar(neko, startChar='h', endChar='g')
            embed = discord.Embed(title='Nya!', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.set_image(url=neko)
            embed.set_footer(text='Image from nekos.life')
            await ctx.respond(embed=embed)
    
    @commands.slash_command(guild_ids=guild)
    async def rule34(self, ctx, tags : str = None):
        """Searches Rule34 for tags (split by spaces)"""
        if ctx.interaction.channel.nsfw:
            if tags:
                tags = tags.split()
            else:
                tags = ""
            url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&tags={}'.format("+".join(tags))
            page = requests.get(url)
            if not page.ok:
                await ctx.respond("Error"+str(page.status_code))
            soup = BeautifulSoup(page.text, 'html.parser')
            file_urls = []
            for element in soup.find_all(file_url=True):
                file_urls.append(element["file_url"])
            if len(file_urls) == 0:
                embed = discord.Embed(color=0xFF0000)
                embed.add_field(name=':warning:', value='No results found on rule34.xxx')
                await ctx.respond(embed=embed)
            else:
                file_url = random.choice(file_urls)
                embed = discord.Embed(title='Rule34 Search:', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
                embed.set_image(url=file_url)
                await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=':warning:', value='Must be a NSFW channel!')
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(NSFW(bot))