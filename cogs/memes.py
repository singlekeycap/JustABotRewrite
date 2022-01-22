import discord, random, requests, requests
from discord.ext import commands
from fake_useragent import UserAgent
from cogs.constants import ver, dev, guild, log_channel, welcome_channel

class Memes(commands.Cog, name="Memes :joy:"):
    """Funny memes haha"""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(guild_ids=guild)
    async def tiktok(self, ctx):
        """Random TikTok quote (Requested by Anonymous)"""
        useravatar = ctx.interaction.user.avatar
        username = ctx.author
        quotelist = ["Hit or miss, I guess they never miss", "I'm already Tracer", "**You need healing**", "*E*", "Alright, one more Tik Tok shenanigan and I'm out"]
        quote = random.choice(quotelist)
        embed = discord.Embed(title="TikTok", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_author(name=username, icon_url=useravatar)
        embed.add_field(name="Here is your quote...", value=quote)
        embed.set_footer(text="TikTok is gay")
        await ctx.respond(embed=embed)
    
    @commands.slash_command(guild_ids=guild)
    async def meme(self, ctx):
        """Random meme from Reddit"""
        useravatar = ctx.interaction.user.avatar
        username = ctx.author
        ua = UserAgent()
        sorts = ['new', 'controversial', 'top', 'hot', 'rising']
        sort = random.choice(sorts)
        subreddits = ['meme', 'memes', 'me_irl', 'dankmemes', 'Edgymemes']
        subreddit = random.choice(subreddits)
        url = 'https://www.reddit.com/r/'+subreddit+'/'+sort+'/.json?'+sort+'=new&t=all&limit=20'
        response = requests.get(url, headers={'User-agent': ua.random})
        if not response.ok:
            print("Error", response.status_code)
        data = response.json()['data']['children']
        images = []
        for i in range(len(data)):
            current_post = data[i]['data']
            images.append(current_post)
        current_post = random.choice(images)
        url = current_post['url']
        if 'imgur.com' in url:
            url = url+'.jpg'
        imagename = current_post['title']
        embed = discord.Embed(title=imagename, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_author(name=username, icon_url=useravatar)
        embed.set_image(url=url)
        embed.set_footer(text="Provided from r/"+subreddit+".")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Memes(bot))