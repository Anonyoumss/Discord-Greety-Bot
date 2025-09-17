import discord

# Define the intents for the bot
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

# Create the bot client with the specified intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """This function runs when the bot is connected to Discord."""
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    """This function runs every time a message is sent in a channel the bot can see."""
    # Don't let the bot respond to its own messages to avoid a loop
    if message.author == client.user:
        return

    # Check if the message content is "hello" or "hi" (case-insensitive)
    if message.content.lower() in ('hello', 'hi'):
        # Get the user's name and send a greeting
        user_name = message.author.name
        await message.channel.send(f'Hello there, {user_name}!')

# The token will be pulled from Replit's environment variables
# This is a secure way to store secrets
import os
from keep_alive import keep_alive # Import the keep_alive function

# The keep_alive function will start a simple web server
# to keep the repl running 24/7.
keep_alive()

# The bot token is stored as a secret in the REPL's environment variables.
bot_token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(bot_token)
