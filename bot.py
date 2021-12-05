import discord, os, random, time, math, requests
from fake_useragent import UserAgent
from datetime import datetime
from pytz import timezone
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

class BotStuffs():
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def invite(ctx):
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
    
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def ping(ctx) -> None:
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
    
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def version(ctx):
        """Shows bot version and changelog"""
        embed = discord.Embed(title="Bot version: "+ver, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="Changelog:", value="**"+ver+" includes:**\n\nUpdated urls and name\n\nSlowly adding in new commands (new help menu possible)\n\nFixed r34 command (no tags necessary)")
        await ctx.respond(embed=embed)

class Math:
    """Math Commands for the needy"""
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def simple(ctx, operation : str):
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

class Memes():
    """Funny memes"""
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def tiktok(ctx):
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
    
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def meme(ctx):
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

class Fun():
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def choose(ctx, choices : str):
        """Choose between things (separated by commas)"""
        choices = choices.split(",")
        await ctx.respond(random.choice(choices))
    
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def gay(ctx, user : discord.Member):
        """Are you gay? (meme)"""
        level = random.randint(1,100)
        embed=discord.Embed(title='Gay Meter 2000', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name='{0.name} is...'.format(user), value=str(level)+'% gay!')
        await ctx.respond(embed=embed)

class OwnerOnly:
    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def exec(ctx, exec:str):
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

    @bot.slash_command(guild_ids=[906774586987794483, 869694274319581184])
    async def img(ctx, name:str):
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

bot.run(TOKEN)