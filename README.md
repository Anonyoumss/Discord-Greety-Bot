# Discord-Greety-Bot
A bot that greets and says Hi to anybody who says HI or is new !

"""
main.py

This is the main entry point for the Discord bot application. It uses the
discord.py library to connect to the Discord API and handle server interactions.

The script performs the following key functions:

- **Client and Intents Initialization**: Sets up the Discord client and defines
  the required intents (message content, members, and presences) to allow the
  bot to read messages and member statuses.

- **Event Handling**: The `on_ready()` and `on_message()` functions act as event
  listeners.
    - `on_ready()` confirms the bot has successfully logged in.
    - `on_message()` processes every message sent in a channel the bot has access to.

- **Dynamic Responses**: The bot checks for specific keywords in messages to
  provide automated responses for greetings ('hi', 'hello') and farewells ('bye',
  'goodbye').

- **Status Tracking**: It includes commands to check the online and offline
  status of server members. When a user types `online` or `offline`, the bot
  lists the members accordingly.

- **BRB (Be Right Back) System**: A simple in-memory system tracks users who
  type 'brb' or similar phrases. The bot adds them to a temporary list and
  removes them automatically when they send their next message, ensuring the
  list stays up-to-date.

- **Execution**: The script uses a secure method to retrieve the bot token from
  environment variables and starts the bot, while the `keep_alive.py` module
  (imported) ensures the application remains active.
"""


"""
keep_alive.py

This utility script is designed to keep the main bot application running on a
Replit server indefinitely. Replit's free plan may stop a Repl if it's inactive,
which would cause the Discord bot to go offline.

The script's primary function is to:

- **Launch a Web Server**: It uses the lightweight Flask framework to start a
  simple web server. This server listens for incoming connections on port 8080.
  The server's only purpose is to respond to pings from an external uptime
  monitoring service.

- **Run in a Separate Thread**: The web server runs in a new thread, preventing
  it from blocking the main bot code in `main.py`. This ensures that the bot
  can continue to handle Discord events while the web server runs in the
  background.

By importing and calling the `keep_alive()` function from the main bot script,
you ensure the bot remains active and available to users 24/7.
"""



"""

Use Cases
This bot is a practical tool for any Discord server, from small friend groups to large communities. It's designed to streamline communication and provide a more organized and welcoming environment.

Community Engagement: It provides a friendly, automated way to greet members, making the server feel more active and welcoming, especially to newcomers. It also encourages a sense of community by responding to polite phrases like "goodbye."

Status Management: It helps members quickly check who's available without having to scroll through the member list or manually ping people. This is especially useful in larger servers or for gaming groups that need to know who's online and ready to play.

Temporary Availability Status: The BRB system is perfect for coordinating activities. If a user needs to step away for a short period, they can quickly let others know, and the bot will track their status until they return. This reduces confusion and helps maintain smooth conversations and events.

How to Use the Bot
Using this bot is straightforward. It responds to simple text commands and common phrases typed directly into any text channel it has access to.

Greetings:

To greet the bot: Simply type "hello," "hi," "hey," or "yo." The bot will respond with a friendly greeting that includes your name.

Farewells:

To say goodbye: Type "bye," "goodbye," "cya," or "later." The bot will respond with a polite farewell.

Status Commands:

To check who is online: Type online

To check who is offline: Type offline The bot will provide a list of users based on their Discord status. It will also list any users who have recently said a BRB phrase.

BRB (Be Right Back) System:

To let people know you're leaving: Type "brb," "be right back," or "afk." The bot will tag you in a message to let others know you're away.

To be removed from the list: Simply send any message to the channel after your return. The bot will automatically take you off the "who will be right back" list.

"""


"""

Key Features of the Bot
This Discord bot is a robust and flexible application designed for easy deployment and continuous operation. Its features are built around providing a seamless user experience while ensuring reliability and simplified maintenance.

Functionality
Discord Integration: The bot is built using the discord.py library, ensuring a stable and efficient connection to the Discord API.

Intuitive Commands: It responds to a variety of natural language phrases for greetings, farewells, and status updates, making it easy for anyone to use.

In-Memory State Management: The bot uses a simple in-memory dictionary to track users who are "brb," providing a fast and temporary way to manage user status.

Technical Design
Replit Hosting: The bot is configured to run on Replit's platform, offering a free and accessible environment for hosting Python applications.

24/7 Uptime: It utilizes a keep_alive.py utility and an external monitoring service to prevent the Replit instance from idling, ensuring the bot remains online around the clock.

Secure Token Handling: The bot's authentication token is stored securely as an environment variable on Replit, preventing it from being exposed in the code.

Git Integration: The project is designed to be version-controlled with Git, allowing you to pull updates directly from a GitHub repository to your Replit instance. This simplifies the process of deploying new features and bug fixes.

"""
