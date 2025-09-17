import discord

# Define the intents for the bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

# Create the bot client with the specified intents
client = discord.Client(intents=intents)

# List of greeting and farewell words
greetings = ['hi', 'hello', 'hey', 'greetings', 'welcome', 'yo']
farewells = ['bye', 'goodbye', 'cya', 'see you', 'later', 'farewell']
brb_phrases = ['brb', 'be right back', 'coming back later', 'afk']

# A dictionary to store users who are "brb"
brb_users = {}

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

    # Check if the user is in the brb list and remove them if they send any message
    if message.author.id in brb_users:
        del brb_users[message.author.id]
        print(f"Removed {message.author.name} from the BRB list.")

    msg_content = message.content.lower()

    # Handle commands and phrases
    if any(word in msg_content for word in greetings):
        user_name = message.author.name
        await message.channel.send(f'Hey there, {user_name}!')

    if any(word in msg_content for word in farewells):
        user_name = message.author.name
        await message.channel.send(f'See you later, {user_name}!')

    if any(phrase in msg_content for phrase in brb_phrases):
        user_id = message.author.id
        brb_users[user_id] = message.author.name
        await message.channel.send(f'{message.author.mention} is away right now. They\'ll be back later!')

    if msg_content == 'online':
        online_members = [
            member.name
            for member in message.guild.members
            if member.status == discord.Status.online and not member.bot
        ]

        if online_members:
            online_list = '\n'.join(online_members)
            await message.channel.send(f'**Online Members:**\n{online_list}')
        else:
            await message.channel.send('There are no members currently online.')

    if msg_content == 'offline':
        offline_members = [
            member.name
            for member in message.guild.members
            if member.status == discord.Status.offline and not member.bot
        ]

        if offline_members:
            offline_list = '\n'.join(offline_members)
            brb_list = [name for user_id, name in brb_users.items() if user_id in [m.id for m in message.guild.members]]

            response = '**Offline Members:**\n' + offline_list
            if brb_list:
                response += f'\n\n**Members who will be right back:**\n' + '\n'.join(brb_list)

            await message.channel.send(response)
        else:
            await message.channel.send('Everyone is currently online or away.')


# The token will be pulled from Replit's environment variables
import os
from keep_alive import keep_alive

keep_alive()

bot_token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(bot_token)
