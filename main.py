import discord
from discord import player
from discord.ext import commands
import random
#bot link
#https://discord.com/api/oauth2/authorize?client_id=879147976860270592&permissions=8&scope=bot
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def create(ctx, *, players):
    playerList = list(players.split(" "))
    
    random.shuffle(playerList)

    if len(playerList) <= 3:
        await ctx.send('**Innacurate Input**\nNot enough players :tired_face:')
    elif len(playerList) > 10:
        await ctx.send('**Innacurate Input**\nToo many players :sweat:')
    else:
        attackers = []
        defenders = []

        halfpoint = int(len(playerList) / 2)

        attackers = playerList[0:halfpoint]
        defenders = playerList[(halfpoint):]

        #await ctx.send(f'**Player List -->** {playerList}')
        await ctx.send(f'**Team 1 / Attackers -->** {attackers}')
        await ctx.send(f'**Team 2 / Defenders -->** {defenders}')

        '''
        await ctx.send(f'**Team 1 / Attackers -->** {playerList[0], playerList[1], playerList[2], playerList[3], playerList[4]}')
        await ctx.send(f'**Team 2 / Defenders -->** {playerList[5], playerList[6], playerList[7], playerList[8], playerList[9]}')
        '''

@client.command()
async def map(ctx):
    maps = ['Bind', 'Haven', 'Split', 'Ascent', 'Icebox', 'Breeze']
    dMap = random.choice(maps)
    await ctx.send(f'You have to play on --> **{dMap}**')

@client.command()
async def gun(ctx):
    guns = ['Stinger', 'Spectre', 'Bucky', 'Judge', 'Bulldog', 'Guardian', 'Phantom', 'Vandal', 'Marshal', 'Operator', 'Ares', 'Odin']
    dGun = random.choice(guns)
    await ctx.send(f'You can only use --> **{dGun}**')

@client.command()
async def agent(ctx):
    agents = ['Brimstone', 'Viper', 'Omen', 'Killjoy', 'Cypher', 'Sova', 'Sage', 'Phoenix', 'Jett', 'Reyna', 'Raze', 'Breach', 'Skye', 'Yoru', 'Astra', 'KAY/O']
    dAgent = random.choice(agents)
    await ctx.send(f'Your agent is --> **{dAgent}**')

@client.command()
async def doja(ctx):
    await ctx.send('Doja cat the best female artist of all time :tired_face:')

@client.command()
async def motivation(ctx):
    await ctx.send('https://www.youtube.com/watch?v=tYzMYcUty6s&ab_channel=TeamPsycosmos')

@client.command()
async def commandlist(ctx):
    await ctx.send(f'Use --> . before referencing any command\n'
    '**join** --> joins vc\n'
    '**leave** --> leaves vc\n'
    '**create** --> creates teams of (must input a minimum of 4 players)\n'
    '**map** --> Chooses a random map for you bums\n'
    '**gun** --> Chooses a random gun for you bums\n'
    '**agent** --> Assigns a random agent to you bums\n'
    '**doja** --> Speaks factual fax only :triumph:\n'
    '**motivation** --> helps motivate you bums\n')

client.run('enter token')
