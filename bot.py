import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'Wiadomosc od {message.author}: {message.content}')

    if  message.content.lower() in ('cześć') != '-1':
        await message.channel.send(f'Cześć **{message.author.display_name}**!')
    elif  message.content.lower() in ('witam') != '-1':
        await message.channel.send(f'Witam, witam **{message.author.display_name}**!')
    elif  message.content.lower() in ('czesc') != '-1':
        await message.channel.send(f'Cześć **{message.author.display_name}**!')
    elif  message.content.lower() in ('hej') != '-1':
        await message.channel.send(f'Hejka **{message.author.display_name}**!')
    elif message.content.lower() in ('siema') != '-1':
        await message.channel.send(f'Siema **{message.author.display_name}**!')
    elif message.content.lower() in ('elo') != '-1':
        await message.channel.send(f'Elo! **{message.author.display_name}**!')
    elif message.content.lower() in ('dzień dobry') != '-1':
        await message.channel.send(f'Dzień dobry! **{message.author.display_name}**!')
    elif message.content.lower() in ('dzien dobry') != '-1':
        await message.channel.send(f'Dzień dobry! **{message.author.display_name}**!')
    elif message.content == 'kod 1233434123':
        await message.channel.send(f'**Hahaha**')
    

    
    
    

client.run(TOKEN)