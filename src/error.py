from discord.ext import commands
import discord
from src.secret import color_red, time

class error:
    def __init__(self,bot):
        self.bot = bot

    async def on_command_error(self,ctx,exception):
        if isinstance(exception, commands.CheckFailure):
            embed = discord.Embed(title="Please send me a private message!", color=color_red)
            await ctx.author.send(embed=embed)
        elif isinstance(exception, commands.CommandNotFound):
            pass
