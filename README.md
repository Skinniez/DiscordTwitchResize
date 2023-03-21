# Discord Image Resizing Bot
## This bot is a Discord bot that can resize images attached to messages in a Discord server. It uses the Python programming language and several libraries, including discord, discord.ext, dotenv, io, and PIL.

## Features
Resizes images attached to messages in Discord
Can resize images to three different sizes: 128x128, 56x56, and 28x28
Checks if an attachment is an image before resizing it
Sends the resized image back to the channel where the original message was posted
## Installation
To use this bot, you will need to have Python 3 installed on your computer. You will also need to create a Discord bot and obtain a bot token. You can follow the instructions in the Discord documentation to create a bot and get a token.

Clone this repository to your computer https://github.com/Skinniez/DiscordTwitchResize
Navigate to the cloned repository directory using cd discord-image-resizing-bot
Create a virtual environment using python3 -m venv venv
Activate the virtual environment using source venv/bin/activate (on Linux/Mac) or venv\Scripts\activate (on Windows)
Install the required Python packages using pip install -r requirements.txt
Create a .env file in the project directory and add your Discord bot token to it using DISCORD_BOT_TOKEN=your-bot-token-here
Run the bot using python bot.py
Usage
Once the bot is running and connected to your Discord server, it will automatically detect when an image is posted to a channel. It will resize the image to three different sizes: 128x128, 56x56, and 28x28. The bot will then send the resized images back to the channel where the original message was posted.

You can customize the sizes that the bot resizes the images to by modifying the sizes list in the on_message event.

To use the bot, simply attach an image to a message in Discord and send it to a channel where the bot is present. The bot will take care of the rest!

Contributing
If you would like to contribute to this bot, feel free to open a pull request or an issue on the GitHub repository. We welcome any and all contributions!
