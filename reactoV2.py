import discord, random, os

import setENV

from discord.ext import commands
# from steamScrape import getSteamReviews

#This version of Reacto uses cogs, which is a system of modules for discord.

client = commands.Bot(command_prefix = '.')


# These commands handle loading and unloading things from the cogs file.
@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'): #Endswith! :0
        
        client.load_extension(f'cogs.{filename[:-3]}') # The -3 cuts off the .py to conform with the correct syntax
        print(f'Loaded cogs from {filename}')

client.run(os.environ.get('BOT_KEY'))