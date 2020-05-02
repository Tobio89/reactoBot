import discord, random
from discord.ext import commands


reactionlist = {
        'sandattack' : 'https://i.imgur.com/0vTN4JC.mp4',
        'fthis': 'https://i.imgur.com/gZCTn5f.gif',
        'ilied': 'https://i.imgur.com/fIpyfQC.gif',
        'dontbelieve': 'https://i.imgur.com/4HoAjtC.gif',
        'rain': 'https://i.imgur.com/0S1fmZZ.gif',
        'itstrue': 'https://i.imgur.com/OgG5Hfv.mp4',
        'waiting': 'https://i.imgur.com/DNsXXq9.jpg',
        'gotany': 'https://media.tenor.com/images/3a2c23670879ea70fa852f953d9a09f7/tenor.gif',
        'wtf': 'https://i.imgur.com/5ccLtCs.mp4',
        'wow': 'https://thumbs.gfycat.com/HarmfulPessimisticGoldenretriever-size_restricted.gif'
    }


class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Events
    @commands.Cog.listener() #This is equal to @client.event, but for cogs.
    async def on_ready(self):
        print('Reacto has been awakened...')


    # Commands
    @commands.command(brief='Find out your latency!') #This allows you to do commands.
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms.')

    @commands.command(aliases=['8ball', 'advice'], brief='Ask Reacto and he shall tell you your future.')
    async def _8ball(self, ctx, *, question): 

        questionProofingList = question.split(' ')

        if '?' not in questionProofingList[-1]:
            questionProofingList[-1] = f'{questionProofingList[-1]}?'
        for i in range(len(questionProofingList)):
            if questionProofingList[i] == 'I':
                questionProofingList[i] = 'you'
        
        editedQuestion = ' '.join(questionProofingList)
        
        responses = [
                    'It is certain.',
                    'It is decidedly so.',
                    'Wthout a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    "Don't count on it.",
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.',
                    ]
        
        await ctx.send(f'{editedQuestion}\n\n {random.choice(responses)}')


    @commands.command(aliases=['erase'], brief='Erases one message by default.')
    async def clear(self, ctx, amount=2, pw=None):
        if amount > 5:
            if pw == 'begone':
                print('Correct password!')
                
            else:
                print(f'Password {pw} was wrong, capped at 5')
                amount = 5
            
        await ctx.channel.purge(limit=amount+1)

    @commands.command(brief='An image is worth one reaction - pastes an image to support your point.')
    async def react(self, ctx, reaction):
        
        if reaction in reactionlist.keys():
            await ctx.send(reactionlist[reaction])
        elif reaction == 'list':
            responses = [key for key in reactionlist.keys()]
            response = '\n'.join(responses)
            await ctx.send(f'Reactions you can use include...\n{response}')

        else:
            await ctx.send('https://i.imgur.com/ZcSzUj6.mp4')

    @commands.command(brief='Change the bot status')
    async def status(self, ctx, status):
        statuses = {
            'idle' : discord.Status.idle,
            'online' : discord.Status.online,
            'offline': discord.Status.offline,
            'dnd': discord.Status.do_not_disturb,
            'invisible': discord.Status.invisible
        }
        print(f'Changed status to {status}')
        
        await self.client.change_presence(status=statuses[status]) # This line is about statuses

    @commands.command(brief="Mess with what the bot is playing")
    async def activity(self, ctx, *, activity):
        print(f'Changed activity to "Playing {activity}"')
        await self.client.change_presence(activity=discord.Game(activity))
        

def setup(client):
    client.add_cog(Basic(client))