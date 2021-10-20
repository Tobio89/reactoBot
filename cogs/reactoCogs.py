import discord
import random
from discord.ext import commands


class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()  # This is equal to @client.event, but for cogs.
    async def on_ready(self):
        print('Reacto has been awakened...')

    # Commands
    # This allows you to do commands.
    @commands.command(brief='Find out your latency!')
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

    # @commands.command(aliases=['erase'], brief='Erases one message by default.', hidden=True)
    # async def clear(self, ctx, amount=2, pw=None):
    #     if amount > 5:
    #         if pw == 'begone':
    #             print('Correct password!')

    #         else:
    #             print(f'Password {pw} was wrong, capped at 5')
    #             amount = 5

    #     await ctx.channel.purge(limit=amount+1)

    # @commands.command(brief='Change the bot status', hidden=True)
    # async def status(self, ctx, status):
    #     statuses = {
    #         'idle' : discord.Status.idle,
    #         'online' : discord.Status.online,
    #         'offline': discord.Status.offline,
    #         'dnd': discord.Status.do_not_disturb,
    #         'invisible': discord.Status.invisible
    #     }
    #     print(f'Changed status to {status}')
    #     if status == 'help':
    #         await ctx.send('Status can be: online, idle, dnd, invisible and offline.')

    #     try:
    #         await self.client.change_presence(status=statuses[status]) # This line is about statuses
    #     except:
    #         await ctx.send(f"Nope, I'm not being {status}. Try online, idle, dnd, invisible or offline")

    # @commands.command(brief="Mess with what the bot is playing")
    # async def activity(self, ctx, *, activity):
    #     print(f'Changed activity to "Playing {activity}"')
    #     await self.client.change_presence(activity=discord.Game(activity))


def setup(client):
    client.add_cog(Basic(client))
