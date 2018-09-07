import os
import random
import re
from datetime import datetime

import discord
from discord import Game
from discord.ext.commands import Bot

SEPERATOR = "\n------\n"
BOT_PREFIX = "!"
TOKEN = os.environ['token']
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
bdsm_self = ['{author} pulls a book out of their bookshelf revealing a hidden doorway. Could this be their sex dungeon?',
             'The channel looks on in horror as {author} exposes their bdsm collection.']
bdsm_user = ['{author} ties up {victim} with and gags them.',
             '{author} whips {victim} playfully.',
             '{victim} pleads for mercy, but {author} knows they secretly like it and continues whipping them.',
             '{author} steps on {victim}\'s crotch, causing them to moan in both agony and pleasure.',
             '{victim} looks on in horror as {author} reveals a collection of whips that hang from the wall.']
bdsm_bot = ['Sorry, i\'m with Lapis :blush:',
            'Only Lapis\' chains and whips can touch me.',
            'I\'m sorry, I only like you as a friend']


def user_is_mod(user):
    author_roles = user.roles
    has_right_role = False
    for role in author_roles:
        if role.name == os.environ['mod_role']:
            has_right_role = True
    return has_right_role

def user_is_admin(user):
    author_roles = user.roles
    has_right_role = False
    for role in author_roles:
        if role.name == os.environ['admin_role']:
            has_right_role = True
    return has_right_role

def user_is_custom_role(user):
    author_roles = user.roles
    has_right_role = False
    for role in author_roles:
        if role.name == os.environ['custom_role']:
            has_right_role = True
    return has_right_role

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
        message = '{username} bid farewell to this cruel world.'.format(
            username=victim.mention)
    elif victim.name == "Peribot":
        message = 'Silly human you can make me killbind myself!'
    elif victim.id != author.id:
        message = "{username} tricks {victim} into bidding farewell to this cruel world.".format(username=author.mention, victim=victim.mention)
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

@client.command(name='bdsm',
                description="This command will bdsm a user or yourself",
                breif="BDSM fun",
                pass_context=True)
async def lick(ctx, victim: discord.Member):
    author = ctx.message.author
    if victim.id == author.id:
        message = random.choice(bdsm_self).format(author=victim.mention)
    elif victim.name == "Peribot":
        message = random.choice(bdsm_bot)
    elif victim.id != author.id:
        message = random.choice(bdsm_user).format(author=author.mention, victim=victim.mention)
    else:
        message = 'That\'s not how this command works you bint. {author}'.format(author=ctx.message.author.mention)
    await client.say(message)

@client.command(name='lick',
                description="This command will lick a user",
                breif="Dont killbind me please",
                pass_context=True)
async def lick(ctx, victim: discord.Member):
    author = ctx.message.author
    if victim.id == author.id:
        message = random.choice(lick_self).format(username=victim.mention) + '\r\r' + random.choice(lick_gif)
    elif victim.name == "Peribot":
        message = 'AGH Gross! You got slobber in my circuits, J\_C\_\_\_ will not be happy!'
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

@client.command(name='phoenix',
                pass_context=False)
async def phoenix():
    date_of_last_episode = datetime.strptime('Sep 2 2018 10:00AM',
                                             '%b %d %Y %I:%M%p')  # Set from config
    days = re.search('\d{1,3}\s', str(datetime.now() - date_of_last_episode)).group(0)
    msg = "Days since last word from PhoenixVersion1:\n\n" + "[" + days + "Days]"
    await client.say(msg)


@client.command()
async def ping():
    await client.say("Pong!")

@client.command(pass_context=True)
async def newinvite(ctx):
    if user_is_mod(ctx.message.author) or user_is_admin(ctx.message.author) or user_is_custom_role(ctx.message.author):
        max_age = 0
        max_age_text = "Never"
        max_uses = 0
        max_uses_text = "Unlimited"
    else:
        max_age = 900
        max_age_text = "15 Minutes"
        max_uses = 3
        max_uses_text = str(max_uses)

    invitelinknew = await client.create_invite(destination=ctx.message.channel,
                                            max_uses=max_uses, max_age=max_age)
    embedMsg = discord.Embed(color=0x90ee90,title="__NEW INVITE LINK GENERATED__")
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.add_field(name="Discord Invite Uses", value=max_uses_text)
    embedMsg.add_field(name="Discord Invite Expiration", value=max_age_text)
    embedMsg.set_footer(text="Discord server invite link generated by {author}".format(author=ctx.message.author))
    await client.send_message(ctx.message.channel, embed=embedMsg)

@client.command(pass_context=True)
async def changegame(ctx, game):
    if user_is_mod(ctx.message.author) or user_is_admin(ctx.message.author) or user_is_custom_role(ctx.message.author):
        await client.change_presence(game=Game(name=game))
        embedMsg = discord.Embed(color=0x90ee90, title="Game changed successfully")
        await client.send_message(ctx.message.channel, embed=embedMsg)
    else:
        await client.say("You do not have permissions for this command! :robot:")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Python 3.6"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # await client.say("%s booting process complete." % client.user.name)


client.run(TOKEN)