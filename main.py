from settings import settings
import discord
import join
from bot_logic import *

# Intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Bot listo
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Respuestas del bot
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip()

    # --- OTROS COMANDOS ---
    if content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')

    elif content.startswith('$smile'):
        await message.channel.send(gen_emodji())

    elif content.startswith('$flip'):
        await message.channel.send(flip_coin())

    elif content.startswith('$password'):
        await message.channel.send(gen_pass(12))

    elif content.startswith('$add'):
        # Uso: $add <left> <right>
        parts = content.split()
        if len(parts) != 3:
            await message.channel.send('Uso: $add <número> <número>. Ej: $add 2 3')
        else:
            try:
                left = int(parts[1])
                right = int(parts[2])
                await message.channel.send(str(left + right))
            except ValueError:
                await message.channel.send('Error: ambos argumentos deben ser números enteros. Ej: $add 2 3')

    elif content.startswith('$joined'):
        if message.mentions:
            member = message.mentions[0]
            if member.joined_at is None:
                await message.channel.send(f'{member} no tiene fecha de ingreso.')
            else:
                await message.channel.send(
                    f'{member} se unió {discord.utils.format_dt(member.joined_at)}')
        else:
            await message.channel.send('Uso: $joined @usuario')

    elif content.startswith('$bye'):
        await message.channel.send(gen_emodji())

    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

# Iniciar bot
client.run(settings["TOKEN"])