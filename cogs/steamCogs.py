import discord
from discord.ext import commands
from steamScrape import getSteamReviews


class Steam(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(aliases=['sshop'], brief='Generates steam store search URL for a game.')
    async def steamshop(cself, ctx, *, gameName):

        steamStoreURLPrefix = 'https://store.steampowered.com/search/?term='
        rawGameName = gameName.split(' ')
        gameNamePLUS = '+'.join(rawGameName)

        steamStoreURLResponse = f'{steamStoreURLPrefix}{gameNamePLUS}'
        
        await ctx.send(steamStoreURLResponse)

        
    @commands.command(brief="Searches for a game, returns first result's name, reviews, price and shop link.")
    async def steam(self, ctx, *, gameName):
        try:
            searchedTerm, returnedName, gamePrice, gameReview, gameURL = getSteamReviews(gameName)

            response = f'''\n
                            You searched for '{searchedTerm}', and I found:
                            {returnedName}, which costs {gamePrice}.
                            The reviews are: {gameReview}
                            And you can buy it from {gameURL}
                        '''
        except:
            print(f'Check out {gameName}: it went wrong.')
            response = f'I searched for {gameName} but something went wrong. Fiddlesticks!'
            
        await ctx.send(response)




def setup(client):
    client.add_cog(Steam(client))