import discord
from discord.ext import commands
import os
import datetime
import json

DIRPATH = os.path.abspath(os.getcwd()))
FS = os.path.sep

Directory1 = 'C:/Users/sfg99/3D Objects/StonkBot/settings.json'
Directory2 = 'C:/Users/sfg99/3D Objects/StonkBot/secret.json'

print("Discord v" + discord.__version__)
with open(DIRPATH+FS+"settings.json") as f: settings = json.load(f)
with open(DIRPATH+FS+"secret.json") as f: key = json.load(f)
client = commands.Bot(command_prefix = settings['prefix'])



@client.event
async def on_ready(): print(f'{client.user} has connected to Discord!')

@client.event
async def on_command_error(ctx, error): await ctx.send(f'Error. Try $help ({error})')



for filename in settings['autoLoad']:
    client.load_extension(filename[:-3])
    print(f'Loaded {filename}!')



client.run(key['token'])
