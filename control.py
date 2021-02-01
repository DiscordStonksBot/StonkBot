import discord
from discord.ext import commands
import os, sys



class Control(commands.Cog):

    def isAdmin(ctx):
        if (ctx.message.author.server_permissions.administrator):
            return 1
        elif False:
            return 2
        else:
            return False



    def __init__(self, client):
        self.client = client

    @commands.command()
    async def enable(self, ctx, extension):
        if (not isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            self.client.load_extension(extension)
    
    @commands.command()
    async def enableall(self, ctx):
        if (not isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            for filename in os.listdir('C:/Users/sfg99/3D Objects/StonkBot'):
                if filename.endswith(".py"):
                    if filename != "main.py":
                        self.client.load_extension(filename[:-3])
            await ctx.send(f'Loaded All Cogs!', delete_after = 5)

    @commands.command()
    async def disable(self, ctx, extension):
        if (not isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            self.client.unload_extension(extension)

    @commands.command()
    async def disableall(self, ctx):
        if (not isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            for filename in os.listdir('C:/Users/sfg99/3D Objects/StonkBot'):
                if filename.endswith(".py"):
                    if filename != "main.py":
                        self.client.unload_extension(filename[:-3])
            await ctx.send(f'Loaded All Cogs!', delete_after = 5)
    
    @commands.command()
    async def reload(self, ctx, extension):
        if (not isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            self.client.unload_extension(extension)
            self.client.load_extension(extension)
    
    @commands.command()
    async def reloadall(self, ctx):
        if (not isAdmin(ctx)):
            await ctx.send(f'Error: You are not an admin')
        else:
            for filename in os.listdir('C:/Users/sfg99/3D Objects/StonkBot'):
                if filename.endswith(".py"):
                    if filename != "main.py":
                        self.client.unload_extension(filename[:-3])
                        self.client.load_extension(filename[:-3])
            await ctx.send(f'Reloaded All Cogs!', delete_after = 5)

    @commands.command()
    async def restart(self, ctx):
        if (not isAdmin(ctx)):
            await ctx.send(f'Error: You are not an bot operator')
        else:
            await ctx.send(f'Restarting bot')
            sys.exit()

    

def setup(client):
    client.add_cog(Control(client))