import discord
from discord.ext import commands



class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send(f'Pong! {ctx.author}: {round(self.client.latency * 1000)}ms', delete_after = 15)
    
    @commands.command()
    async def version(self, ctx):
        vs = discord.Embed(title = "Current Version", color = 0x00ff00)
        vs.add_field(name = "Version Code:", value = "v1.0.0")
        vs.add_field(name = "Date Released:", value = "January 29th, 2021")
        vs.set_footer(text = "Stanley G.")

        await ctx.message.delete()
        await ctx.channel.send(embed = vs, delete_after = 30)

def setup(client): client.add_cog(Misc(client))