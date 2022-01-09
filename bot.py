import discord, os, random, math, requests, requests, urllib3, substring, certifi, asyncio
from discord.ext import commands
from discord.ext import tasks
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv
from help import HelpButtons, DisabledHelp
load_dotenv()
TOKEN = os.getenv("TOKEN")

#Set constants
ver = "0.1b"
dev = "JustANobody#2107"
guild = [906774586987794483, 869694274319581184]

bot = discord.Bot("jt!")

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('------------------')
    print('Connected to '+str(len(bot.guilds))+' servers!')
    servers = list(bot.guilds)
    for i in range(len(servers)):
        members = str(servers[i].member_count)
        print(' '+ servers[i].name+' with '+members+' members!')

class BotStuffs(commands.Cog, name="Bot Things :robot:"):
    """Bot invite, ping, etc."""
    @commands.slash_command(guild_ids=guild)
    async def invite(self, ctx):
        """Shows invite info, like server/bot invites"""
        useravatar = ctx.interaction.user.avatar
        username = ctx.author
        embed=discord.Embed(title='Invites', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_author(name=username, icon_url=useravatar)
        embed.add_field(name="‎", value=":globe_with_meridians: [Invite To Owner's Server](https://justanobody.me/server.html)", inline=False)
        embed.add_field(name="‎", value=":robot: [Invite Bot To Your Server](https://justanobody.me/bot.html)", inline=False)
        tz = timezone("UTC")
        now = datetime.now(tz=tz)
        embed.set_footer(text=now.strftime("%b %w %Y • %H:%M UTC"))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(guild_ids=guild)
    async def ping(self, ctx) -> None:
        """Tests server latency by measuring how long it takes to edit a message."""
        embed = discord.Embed(title="Pong!", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url=bot.user.display_avatar)
        embed.description = "Latency: testing..."
        b = datetime.utcnow()
        await ctx.respond(embed=embed)
        ping = math.floor((datetime.utcnow() - b).total_seconds() * 1000)
        embed.description = ""
        embed.add_field(name="Message Latency", value=f"`{ping}ms`")
        embed.add_field(name="API Latency", value=f"`{math.floor(bot.latency*1000)}ms`")
        await ctx.edit(embed=embed)
    
    @commands.slash_command(guild_ids=guild)
    async def version(self, ctx):
        """Shows bot version and changelog"""
        embed = discord.Embed(title="Bot version: "+ver, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="Changelog:", value="**"+ver+" includes:**\n\nUpdated to pycord\n\nFinishing up command transfers\n\nShaking and crying :sob:")
        await ctx.respond(embed=embed)

bot.add_cog(BotStuffs(bot))

class Math(commands.Cog, name="Math :heavy_division_sign:"):
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

bot.add_cog(Math(bot))

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

bot.add_cog(Memes(bot))

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

bot.add_cog(Fun(bot))

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

bot.add_cog(NSFW(bot))

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
                    f.write(cmd.read())
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

bot.add_cog(OwnerOnly(bot))

class Utilities(commands.Cog, name="Utilities :hammer_pick:"):
    """General use tools for this bot."""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.slash_command(guild_ids=guild)
    async def help(self, ctx, cmd : str = None, page : int = 0):
        """Show all commands"""
        if cmd:
            command = bot.get_command(cmd)
            embed = discord.Embed(title="Help Menu", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.add_field(name=command.name, value=command.description)
        else:
            cogs = self.bot.cogs
            max = len(self.bot.cogs)
            cogs = list(cogs.values())
            cog = cogs[page]
            embed = discord.Embed(title=cog.qualified_name, description=cog.description, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            for command in cog.walk_commands():
                embed.add_field(name=command.name, value=command.description)
            await ctx.respond(embed=embed, view = HelpButtons(bot, ctx, page))

bot.add_cog(Utilities(bot))

class Admin(commands.Cog, name="Admin Commands :hammer_pick:"):
    """Commands that only server admins can run."""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.slash_command(guild_ids=guild)
    async def ban(self, ctx, user : discord.Member = None):
        """Bans a user"""

bot.add_cog(Admin(bot))

@tasks.loop(seconds = 20)
async def myLoop():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(name=str(len(bot.guilds))+' guilds', type=3))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game(name='Need help? /help'))

myLoop.start()

bot.run(TOKEN)