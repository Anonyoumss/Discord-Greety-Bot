# Discord-Greety-Bot

A bot that greets and says Hi to anybody who says HI or is new!

A Versatile and Friendly Discord Bot
This bot is a practical and welcoming addition to any Discord server, designed to streamline communication and enhance community interaction. Built using the discord.py library, it offers a suite of intuitive, natural-language features that are easy for any user to learn and enjoy.

<br>
<br>

Use Cases and How to Use It
The bot is perfect for any group, from small teams to large communities, that wants to add a touch of automation and organization to their server.

Friendly Responses: The bot recognizes and responds to common greetings ("hi", "hello") and farewells ("bye", "goodbye"), making the server feel more dynamic and engaging for new and old members alike.

Status Management: Users can quickly check on the availability of others. Typing "online" will list all members currently online, while "offline" will list those who are offline.

"Be Right Back" (BRB) System: If a user needs to step away, they can simply type "brb" or a similar phrase, and the bot will track their status. As soon as they send a new message, they are automatically removed from the BRB list, ensuring the information is always up-to-date.

<br>
<br>

Key Features and Technical Design
The bot's design prioritizes stability, security, and ease of deployment.

Replit Hosting: The bot is configured to run on Replit's platform, providing a free and accessible hosting environment.

24/7 Uptime: It uses a dedicated keep_alive.py utility to run a web server in the background, which prevents the bot from going idle and ensures it remains online around the clock.

Git Integration: The project is fully version-controlled with Git, allowing for easy updates. You can pull new changes directly from a GitHub repository to your Replit instance, simplifying maintenance and feature deployment.

Secure Token Handling: The bot's sensitive authentication token is stored securely as an environment variable within Replit, preventing it from being exposed in the code and protecting the application from unauthorized access.

<details>
  <summary><h2 id="features">✨ Key Features</h2></summary>

- **Discord Integration:** Built using the discord.py library for stable and efficient connection to the Discord API.
- **Intuitive Commands:** Responds to a variety of greetings, farewells, and status phrases using natural language.
- **In-Memory State Management:** Tracks “brb” users in memory for fast, temporary status management.
- **Replit Hosting:** Configured to run on Replit for free, always-on hosting of Python apps.
- **24/7 Uptime:** Uses `keep_alive.py` and external monitoring to prevent sleeping.
- **Secure Token Handling:** Bot token is stored as an environment variable for safety.
- **Git Integration:** Easy to update via GitHub for streamlined deployment.

</details>

<p align="center"></p>

<details>
  <summary><h2 id="use-cases">🛠️ Use Cases</h2></summary>

- **Community Engagement:** Greets new members and replies to “hi”, “hello”, etc., making your server more active and welcoming.
- **Status Management:** Lets members quickly check who’s online/offline (with `online` or `offline`), and tracks BRB statuses.
- **Temporary Availability:** Simple “brb” system shows who’s temporarily away, auto-removing them when they return.
- **Organized Communication:** Helps keep everyone informed about member status in busy servers.

</details>

<p align="center"></p>

<details>
  <summary><h2 id="mainpy">📄 main.py Overview</h2></summary>

**Main entry point for the Discord bot application.**

- **Client/Intents Setup:** Initializes the Discord client with permissions for messages, members, and presences.
- **Event Handling:** 
  - `on_ready()` confirms bot login.
  - `on_message()` processes every message for keywords.
- **Dynamic Responses:** Replies to greetings (“hi”, “hello”) and farewells (“bye”, “goodbye”).
- **Status Commands:** “online”/“offline” lists members by status.
- **BRB System:** Tracks users who say “brb” and removes them when they return.
- **Execution:** Loads the bot token securely, and imports `keep_alive.py` to keep the process alive.

</details>

<p align="center"></p>

<details>
  <summary><h2 id="keepalivepy">🌐 keep_alive.py Overview</h2></summary>

**Utility to keep the bot running on Replit:**

- **Flask Web Server:** Starts a lightweight server on port 8080 to respond to external pings (for uptime monitoring).
- **Threaded:** Runs in a separate thread so it doesn’t block the bot.
- **How to Use:** Import and call `keep_alive()` from `main.py` to ensure the bot stays online.

</details>

---

## How to Use the Bot

- **Greetings:** Type "hello", "hi", "hey", or "yo"—the bot replies with a greeting and your name.
- **Farewells:** Type "bye", "goodbye", "cya", or "later"—the bot sends a polite farewell.
- **Status:** Type `online` or `offline` to check who’s available.
- **BRB:** Type "brb", "be right back", or "afk" to be added to the BRB list; send any message to auto-remove yourself.

---

> **Tip:** Each section above can be expanded/collapsed by clicking on the dropdown, and quickly accessed via the button images at the top!
