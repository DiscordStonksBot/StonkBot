import discord
from discord.ext import commands
import os, sys


DIRPATH = os.path.abspath(os.getcwd())
FS = os.path.sep


class Control(commands.Cog):

    def isAdmin(self, ctx):
        print(ctx.message.author.id)
        print(self.client.admins)
        if (str(ctx.message.author.id) in self.client.admins['admins']):
            return True
        else:
            return False


    def __init__(self, client):
        self.client = client


    @commands.command()
    async def enable(self, ctx, extension):
        if (not self.isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            self.client.load_extension(extension)
    
    @commands.command()
    async def enableall(self, ctx):
        for filename in os.listdir(DIRPATH + FS):
            if filename.endswith(".py"):
                if filename != "main.py":
                    self.client.load_extension(filename[:-3])
        await ctx.send(f'Loaded All Cogs!', delete_after = 5)

    @commands.command()
    async def disable(self, ctx, extension):
        if (not self.isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            self.client.unload_extension(extension)

    @commands.command()
    async def disableall(self, ctx):
        for filename in os.listdir(DIRPATH + FS):
            if filename.endswith(".py"):
                if filename != "main.py":
                    self.client.unload_extension(filename[:-3])
        await ctx.send(f'Loaded All Cogs!', delete_after = 5)
    
    @commands.command()
    async def reload(self, ctx, extension):
        if (not self.isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            self.client.unload_extension(extension)
            self.client.load_extension(extension)
    
    @commands.command()
    async def reloadall(self, ctx):
        for filename in os.listdir(DIRPATH + FS):
            if filename.endswith(".py"):
                if filename != "main.py":
                    self.client.unload_extension(filename[:-3])
                    self.client.load_extension(filename[:-3])
        await ctx.send(f'Reloaded All Cogs!', delete_after = 5)

def setup(client): client.add_cog(Control(client))
