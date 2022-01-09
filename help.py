import discord, asyncio, random

class HelpButtons(discord.ui.View):
    def __init__(self, bot : discord.Bot, ctx, page : int):
        super().__init__()
        self.bot = bot
        self.ctx = ctx
        self.page = page
        self.max = len(self.bot.cogs)-1
    
    def get_page(self, left, right, page):
        cogs = self.bot.cogs
        max = len(self.bot.cogs)-1
        cogs = list(cogs.values())
        num = self.page
        if page != -1:
            num = page
        else:
            if left:
                num = num - 1
            elif right:
                num = num + 1
        if num > max:
            num = max
        elif num < 0:
            num = 0
        cog = cogs[num]
        embed = discord.Embed(title=cog.qualified_name, description=cog.description, color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        for command in cog.walk_commands():
            embed.add_field(name=command.name, value=command.description)
        return [embed, num]
    
    @discord.ui.button(label = "⬅️", style=discord.ButtonStyle.blurple)
    async def left(self, button: discord.ui.Button, interaction = discord.Interaction):
        await self.ctx.interaction.edit_original_message(embed = self.get_page(True, False, -1)[0], view = HelpButtons(self.bot, self.ctx, self.get_page(True, False, -1)[1]))

    @discord.ui.button(label = "⏹️", style=discord.ButtonStyle.blurple)
    async def stop(self, button: discord.ui.Button, interaction = discord.Interaction):
        await self.ctx.interaction.edit_original_message(embed = self.get_page(False, False, -1)[0], view = DisabledHelp())

    @discord.ui.button(label = "➡️", style=discord.ButtonStyle.blurple)
    async def right(self, button: discord.ui.Button, interaction = discord.Interaction):
        await self.ctx.interaction.edit_original_message(embed = self.get_page(False, True, -1)[0], view = HelpButtons(self.bot, self.ctx, self.get_page(False, True, -1)[1]))

    @discord.ui.button(label = "🔢", style=discord.ButtonStyle.blurple)
    async def num(self, button: discord.ui.Button, interaction = discord.Interaction):
        await self.ctx.interaction.edit_original_message(embed = self.get_page(False, False, -1)[0], view = HelpButtons(self.bot, self.ctx, self.get_page(False, False, -1)[1]))
    
class DisabledHelp(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label = "⬅️", style=discord.ButtonStyle.blurple, disabled=True)
    async def left(self, button: discord.ui.Button, interaction = discord.Interaction):
        await asyncio.sleep(1)

    @discord.ui.button(label = "⏹️", style=discord.ButtonStyle.blurple, disabled=True)
    async def stop(self, button: discord.ui.Button, interaction = discord.Interaction):
        await asyncio.sleep(1)

    @discord.ui.button(label = "➡️", style=discord.ButtonStyle.blurple, disabled=True)
    async def right(self, button: discord.ui.Button, interaction = discord.Interaction):
        await asyncio.sleep(1)

    @discord.ui.button(label = "🔢", style=discord.ButtonStyle.blurple, disabled=True)
    async def num(self, button: discord.ui.Button, interaction = discord.Interaction):
        await asyncio.sleep(1)