from discord.ext.commands import Bot
import random
from discord import Game
import discord
from datetime import datetime
import re

BOT_PREFIX = "!"
TOKEN = "NDg0NDYxMDM1MzE1NTI3NzAw.DmiWYQ.JLuuih6E16Z_CENsFMYt97BVzTY"
client = Bot(command_prefix=BOT_PREFIX)

lick_self = ['{username} stretches their leg towards the sky and begins to lick themself like a cat',
             '{username} begins to lick the palm of their hand hoping no one noticed.',
             '{username} uses *Lick*, its super effective!']
lick_gif = ["https://media.giphy.com/media/12iJvAFE4VuQeI/giphy.gif",
            "https://media.giphy.com/media/NzbcdfP2B6GKk/giphy.gif",
            "https://media.giphy.com/media/LKRtMj7xvviUg/giphy.gif",
            "https://media.giphy.com/media/cMso9wDwqSy3e/giphy.gif",
            "https://media.giphy.com/media/3IZUZUViz7B1S/giphy.gif",
            "https://media.giphy.com/media/ZnnHMeC7iDSzC/giphy.gif"]
lick_user = ['{username} sneaks up behind {victim} adn licks their elbow, I don\'t think they even noticed.',
             '{username} slyly licks {victim} on the cheek, blushing intensely',
             '{username} walks over to {victim} to wisper a secret in their ear, but licks them instead!',
             '{username} tries to lick {victim} but they notice and roundhouse them into next week.']

@client.command(name='8ball',
                description="This command will answer all of your questions just like an 8-Ball would!",
                breif="Ask me your questions!",
                aliases=['eight_ball', '8b', 'eightball'],
                pass_context=True)
async def eight_ball(ctx):
    possible_responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no',
        'Outlook not so good.',
        'Very doubtful.'
    ]
    await client.say('**The Magic 8 Ball says:** \r"' + random.choice(possible_responses) + '",\r' + ctx.message.author.mention)


@client.command(name='killbind',
                description="This command will killbind a user",
                breif="Dont killbind me please",
                aliases=['kb', 'kill-bind'],
                pass_context=True)
async def killbind(ctx, victim: discord.Member):
    author = ctx.message.author
    if victim.id == author.id:
        message = '{username} bids farewell to this cruel world as they press their kill-bind hey killing themself in a glorious ragdoll fassion'.format(
            username=victim.mention)
    elif victim.name == "Peridot_Bot":
        message = 'Silly human you can make me killbind myself!'
    elif victim.id != author.id:
        message = "{username} sneaks up behind {victim} and presses his kill-bind key causing him to lose the game in the worst way.".format(username=author.mention, victim=victim.mention)
    else:
        message = 'That\'s not how this command works you bint. {author}'.format(author=ctx.message.author.mention)
    await client.say(message)


@client.command(name='hiatus',
                description="How long has this Hiatus been going on for?",
                breif="The hiatus is cold and long",
                pass_context=False)
async def hiatus():
    date_of_last_episode = datetime.strptime('Apr 7 2018 01:00AM',
                                             '%b %d %Y %I:%M%p')  # Set from config
    days = re.search('\d{1,3}\s', str(datetime.now() - date_of_last_episode)).group(0)
    msg = "Days since last episode:\n\n" + "[" + days + "Days]"
    await client.say(msg)


@client.command()
async def ded():
    msg = 'https://media.giphy.com/media/3oriff4xQ7Oq2TIgTu/giphy.gif'
    await client.say(msg)


@client.command()
async def lockdown():
    msg = '**THIS DISCORD IS NOW ON LOCKDOWN!**\r\r EVERYONE RETURN TO YOUR CELLS AND PREPARE FOR A SHAKEDOWN\r\r'
    gif = 'https://media1.tenor.com/images/66a0e064ab1aaff80f79a4801b3102a0/tenor.gif?itemid=8691616'
    await client.say(msg + gif)


@client.command(name='lick',
                description="This command will lick a user",
                breif="Dont killbind me please",
                pass_context=True)
async def lick(ctx, victim: discord.Member):
    author = ctx.message.author
    if victim.id == author.id:
        message = random.choice(lick_self).format(username=victim.mention) + '\r\r' + random.choice(lick_gif)
    elif victim.name == "Peridot_Bot":
        message = 'AGH Gross! You got slobber in my circuits, J_C___ will not be happy!'
    elif victim.id != author.id:
        message = random.choice(lick_user).format(username=author.mention, victim=victim.mention) + '\r\r' + random.choice(lick_gif)
    else:
        message = 'That\'s not how this command works you bint. {author}'.format(author=ctx.message.author.mention)
    await client.say(message)


@client.command(aliases=['r'])
async def roll():
    msg = random.randint(1,20)
    if msg == 1:
        msg = "***Critical Fail!***\r [1] "
    elif msg == 20:
        msg = "***Critical Success!***\r [20] "
    else:
        msg = "[" + str(msg) + "] "
    await client.say(msg + ":game_die:")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Python 3.6"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)