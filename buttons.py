import asyncio, discord, random
class HelpButtons(discord.ui.View):
    def __init__(self, bot : discord.Bot, ctx, page : int, id : int):
        super().__init__()
        self.bot = bot
        self.ctx = ctx
        self.page = page
        self.id = id
    
    def get_page(self, left, right, page : int = None):
        cogs = self.bot.cogs
        max = len(self.bot.cogs)-1
        cogs = list(cogs.values())
        if page != None:
            num = page
        else:
            num = self.page
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
        if self.id == interaction.user.id:
            await self.ctx.interaction.edit_original_message(embed = self.get_page(True, False)[0], view = HelpButtons(self.bot, self.ctx, self.get_page(True, False)[1], self.id))

    @discord.ui.button(label = "⏹️", style=discord.ButtonStyle.blurple)
    async def stop(self, button: discord.ui.Button, interaction = discord.Interaction):
        if self.id == interaction.user.id:
            await self.ctx.interaction.edit_original_message(embed = self.get_page(False, False)[0], view = DisabledHelp())

    @discord.ui.button(label = "➡️", style=discord.ButtonStyle.blurple)
    async def right(self, button: discord.ui.Button, interaction = discord.Interaction):
        if self.id == interaction.user.id:
            await self.ctx.interaction.edit_original_message(embed = self.get_page(False, True)[0], view = HelpButtons(self.bot, self.ctx, self.get_page(False, True)[1], self.id))

    @discord.ui.button(label = "🔢", style=discord.ButtonStyle.blurple)
    async def num(self, button: discord.ui.Button, interaction = discord.Interaction):
        if self.id == interaction.user.id:
            def check(message : discord.Message):
                return message.channel == self.ctx.interaction.channel and message.author.id == self.id
            try:
                pagenum = await self.bot.wait_for('message', check=check, timeout=20)
            except asyncio.TimeoutError:
                await self.ctx.interaction.edit_original_message(embed = self.get_page(False, False)[0], view = DisabledHelp())
            else:
                await self.ctx.interaction.edit_original_message(embed = self.get_page(False, False, int(pagenum.content))[0], view = HelpButtons(self.bot, self.ctx, self.get_page(False, False, int(pagenum.content))[1], self.id))
    
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