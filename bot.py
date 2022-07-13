import os
import discord
from dotenv import load_dotenv 

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIXO = os.getenv("PREFIXO")
comprimento = len(PREFIXO)


print(PREFIXO)
print(comprimento)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.content[0:comprimento] == PREFIXO:
		if message.content[comprimento: ] == "hello":
			await message.channel.send("hey dirtbag")
			await message.delete()

		if message.content[comprimento: ] == "clear":
			await message.channel.purge()
			await message.channel.send(f'Agora o {message.channel.name} está limpo')
		




client.run(TOKEN)