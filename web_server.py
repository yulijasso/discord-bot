# -*- coding: utf-8 -*-
"""web_server.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c2THJllogk2Kn2bYn3xgSuMWODb8QuVt
"""

from flask import Flask
from threading import Thread
import os
import discord

app = Flask(__name__)

# Define the intents your bot will use
intents = discord.Intents.default()
intents.messages = True  # Enable message events

# Create a Discord client with the defined intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#chat'):
        await message.channel.send('Hello! Happy to chat with you today!')

@app.route('/')
def home():
    return "Discord Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    # Add your bot token here
    bot_token = "my_secret_key"

    if bot_token is None:
        print("Bot token not found. Please set the DISCORD_BOT_TOKEN environment variable.")
    else:
        # Run the bot only if the token is available
        keep_alive()
        client.run(bot_token)

~