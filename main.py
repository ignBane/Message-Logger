import discord, json

from colorama import Fore,init
from discord.ext import commands

init()

with open('config.json','r') as f:
    config = json.load(f)

client = commands.Bot(command_prefix="-", selfbot=True)

@client.event
async def on_connect():
    print(f'''{Fore.BLUE}
    ╔╦╗┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐  ╦  ┌─┐┌─┐┌─┐┌─┐┬─┐
    ║║║├┤ └─┐└─┐├─┤│ ┬├┤   ║  │ ││ ┬│ ┬├┤ ├┬┘
    ╩ ╩└─┘└─┘└─┘┴ ┴└─┘└─┘  ╩═╝└─┘└─┘└─┘└─┘┴└─
           Logged In As | {client.user} 
{Fore.RESET}''')

@client.event
async def on_message_delete(message):
    print(f'{Fore.RED}[DELETED] Sent : {message.author} | Mesage : {message.content} | Server : {message.guild} | Channel : {message.channel}{Fore.RESET}')

client.run(config['token'], bot=False)
