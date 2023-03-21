import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

async def process_image(message, size):
    attachment = message.attachments[0]
    if attachment.content_type and attachment.content_type.startswith('image/'):
        print(f"Processing image {attachment.filename} to size {size}x{size}")
        # Download the image and open it with PIL
        image_data = await attachment.read()
        image = Image.open(BytesIO(image_data))

        # Resize the image and save it to a buffer
        resized_image = image.copy()
        resized_image.thumbnail((size, size))
        buffer = BytesIO()
        resized_image.save(buffer, format=image.format)

        # Send the resized image back to Discord
        buffer.seek(0)
        await message.channel.send(file=discord.File(buffer, filename=f"{size}x{size}_{attachment.filename}"))
    else:
        await message.channel.send("The attached file is not an image.")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        print(f"Attachments detected")
        sizes = [128, 56, 28]
        for size in sizes:
            await process_image(message, size)

    await bot.process_commands(message)

bot.run(TOKEN)
