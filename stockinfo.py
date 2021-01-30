import discord
from discord.ext import commands
import stockquotes as sq
import datetime



class StockInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shareprice(self, ctx, share):
        await ctx.message.delete()
        v = sq.Stock(f'{share}')
        t = datetime.datetime.now().strftime("%H:%M AKST (%m/%d/%Y)")
        await ctx.channel.send(f"{share}: ${v.current_price} at {t}")
    
    @commands.command()
    async def sp(self, ctx, share):
        await ctx.message.delete()
        v = sq.Stock(f'{share}')
        t = datetime.datetime.now().strftime("%H:%M AKST (%m/%d/%Y)")
        await ctx.channel.send(f"{share}: ${v.current_price} at {t}")
    
def setup(client): client.add_cog(StockInfo(client))