import discord
from discord.ext import commands
import stockquotes as sq
import datetime
import sys



class StockInfo(commands.Cog):


    def __init__(self, client):
        self.client = client
        self.LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo



    def getSharePrice(self, ctx, share=None):
        if (not share):
            return(f"C'mon man. Gimme something to work with! (Error: share ticker symbol missing )")
        else:
            try:
                v = sq.Stock(f'{share}')
                t = datetime.datetime.now().strftime(f"%H:%M {self.LOCAL_TIMEZONE} (%m/%d/%Y)")
                return(f"{share}: ${v.current_price} at {t}")
            except:
                print("Unexpected error:", sys.exc_info()[0])
                return(f"Bruh moment. I can't find a stock called {share}. Sort it out, dumbass.")



    @commands.command()
    async def shareprice(self, ctx, share=None):
        await ctx.channel.send (self.getSharePrice(ctx, share))
        
    
    @commands.command()
    async def sp(self, ctx, share=None):
        await ctx.channel.send (self.getSharePrice(ctx, share))
    
def setup(client): client.add_cog(StockInfo(client))