import discord
import random
from discord.ext import commands

opt = ["rock", "paper", "scissors"]
def determine_winner(pm, bm):
    if(pm == bm):
        return 'Draw'
    if((pm == 0 and bm == 2) or (pm == 1 and bm == 0) or (pm == 2 and bm == 1)):
        return 'Player wins'
    return 'Bot wins'

class custom_bot(commands.Bot):
    async def on_ready(self):
        print('Ready')

rps = custom_bot(command_prefix = '!')

@rps.command()
async def play(ctx, arg):
    arg = arg.lower()
    try:
        opt.index(arg)
    except:
        await ctx.send('Try again bruh')
    bmove = random.randrange(2)
    pmove = opt.index(arg) 
    bot_move = opt[bmove]
    await ctx.send(f'Player: {arg} vs Bot: {bot_move}\nResult: {determine_winner(pmove, bmove)}')

rps.run('NzcyNDIyOTIwOTczNzEzNDI5.X56c5w.PD08O_fmusGWlTXI44IyafPQDzg')