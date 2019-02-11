from discord.ext import commands
import discord, os
try:
    from src.secret import token
    from src.secret import prefix
    from cmd.tic_tac_toe import TicTacToe
    from testing_queue import testing_queue
    from src.secret import bot_game
    from src.error import error
except ModuleNotFoundError:
    print("Make sure you have all files in your path ! See all files here: https://github.com/Bmbus")

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))

@bot.event
async def on_ready():
    print(__file__)
    print(bot.user.name)
    await bot.change_presence(game=discord.Game(name=bot_game),status=discord.Status.idle)
    try:
        s = bot.get_guild(123456789) # If the Bot doesnt delete a server, you can paste the ID here and the server will be deleted !
        await s.delete()
    except AttributeError:
        pass

cogs = [TicTacToe(bot), testing_queue(bot), error(bot)]
    
def Run():
    for cog in cogs
        bot.add_cog(cog)
    bot.run(token)

if __name__ == '__main__':
    Run()
