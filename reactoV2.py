import discord
import random
import os

import setENV

from discord.ext import commands
# from steamScrape import getSteamReviews

# This version of Reacto uses cogs, which is a system of modules for discord.

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())


# These commands handle loading and unloading things from the cogs file.
@client.command(hidden=True)
async def load(_, extension):
    client.load_extension(f'cogs.{extension}')


@client.command(hidden=True)
async def unload(_, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):  # Endswith! :0

        # The -3 cuts off the .py to conform with the correct syntax
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cogs from {filename}')

client.run(os.environ.get('BOT_KEY'))
