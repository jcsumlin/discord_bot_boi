# Work with Python 3.6
import discord
from datetime import datetime
import re
import configparser
import json


config = configparser.ConfigParser()
config.read('auth.ini')
TOKEN = config.get("auth", "discord-token")

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!hiatus'):
        date_of_last_episode = datetime.strptime(config.get('auth', 'hiatus_date'),
                                                 '%b %d %Y %I:%M%p')  # Set from config
        days = re.search('\d{1,3}\s', str(datetime.now() - date_of_last_episode)).group(0)
        msg = "Days since last episode:\n\n" + "[" + days + "Days]"
        await client.send_message(message.channel, msg)
    if message.content.startswith('!ded'):
        msg = 'https://media.giphy.com/media/3oriff4xQ7Oq2TIgTu/giphy.gif'
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)