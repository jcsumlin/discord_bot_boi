# Work with Python 3.6
import discord
from datetime import datetime
import re
import configparser
import json
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio


config = configparser.ConfigParser()
config.read('auth.ini')
TOKEN = config.get("auth", "discord-token")
bot = commands.Bot(command_prefix="!")

client = discord.Client()

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

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
    if message.content.startswith('!lockdown'):
        msg = 'THIS DISCORD IS NOW ON LOCKDOWN! EVERYONE RETURN TO YOUR CELLS AND PREPARE FOR A SHAKEDOWN\r\r'
        gif = 'https://media1.tenor.com/images/66a0e064ab1aaff80f79a4801b3102a0/tenor.gif?itemid=8691616'
        await client.send_message(message.channel, msg + gif)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)