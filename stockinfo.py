import discord
from discord.ext import commands
import yfinance as yf
import stockquotes as sq
import json
import datetime
import sys
import traceback



class StockInfo(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

    def getErrorMsg(self, share):
        return (f"Bruh moment. I can't find a stock called {share}. Sort it out, dumbass. (Or something went wrong when fetching data. Nah, it probably your fault)")


    def getSharePrice(self, share=None):
        if (not share):
            return(f"C'mon man. Gimme something to work with! (Error: share ticker symbol missing )")
        else:
            try:
                v = sq.Stock(f'{share}')
                t = datetime.datetime.now().strftime(f"%H:%M {self.LOCAL_TIMEZONE} (%m/%d/%Y)")
                return(f"{share}: ${v.current_price} at {t}")
            except:
                print("Unexpected error:", sys.exc_info()[0])
                traceback.print_exc()
                return(self.getErrorMsg(share))


    def getyfInfo(self, share):
        if (not share):
            return share
        return (yf.Ticker(f'{share}').info)
            
        
    


    @commands.command()
    async def shareprice(self, ctx, share=None):
        await ctx.channel.send (self.getSharePrice(share))   
    
    @commands.command()
    async def sp(self, ctx, share=None):
        await ctx.channel.send (self.getSharePrice(share))

    @commands.command()
    async def stockprice(self, ctx, share=None):
        await ctx.channel.send (self.getSharePrice(share))


    @commands.command()
    async def shortpercentage(self, ctx, share=None):
        if (not share):
            await ctx.channel.send(f"C'mon man. Gimme something to work with! (Error: share ticker symbol missing )")
        else:
            data = self.getyfInfo(share)
            try:
                sp = float("{:.2f}".format(float(data["shortPercentOfFloat"])*100))
                msg = ""
                if sp > 50:
                    msg = "Raise your pitchforks folks!"
                await ctx.channel.send (f"Short percent of float for {share}: {sp}% {msg}")

            except:
                traceback.print_exc()
                await ctx.channel.send(self.getErrorMsg(share))

    
def setup(client): client.add_cog(StockInfo(client))