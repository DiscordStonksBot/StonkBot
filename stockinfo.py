import discord
from discord.ext import commands
import stockquotes as sq
import datetime
import sys



class StockInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shareprice(self, ctx, share):
        #await ctx.message.delete()
        try:
            v = sq.Stock(f'{share}')
            t = datetime.datetime.now().strftime("%H:%M AKST (%m/%d/%Y)")
            await ctx.channel.send(f"{share}: ${v.current_price} at {t}")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            await ctx.channel.send(f"Bruh moment. I can't find a stock called {share}. Sort it out, dumbass.")

    
    @commands.command()
    async def sp(self, ctx, share):
        await ctx.message.delete()
        v = sq.Stock(f'{share}')
        t = datetime.datetime.now().strftime("%H:%M AKST (%m/%d/%Y)")
        await ctx.channel.send(f"{share}: ${v.current_price} at {t}")
    
def setup(client): client.add_cog(StockInfo(client))