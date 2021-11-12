import discord
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = discord.Bot()

@bot.slash_command(guild_ids=[869694274319581184])
async def hello(ctx):
    """Say hello to the bot"""
    await ctx.respond(f"Hello {ctx.author}!")

@bot.slash_command(guild_ids=[869694274319581184])
async def joined(ctx, member: discord.Member = None):
    user = member or ctx.author
    await ctx.respond(f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}")

bot.run(TOKEN)