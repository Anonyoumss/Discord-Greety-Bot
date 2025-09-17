# Discord-Greety-Bot

A bot that greets and says Hi to anybody who says HI or is new!

🤖 Meet your new Discord friend!
Make your server feel more alive with a bot that's both smart and friendly. This bot is designed to be your community's go-to for quick info and fun interactions.

Friendly & Smart: The bot greets members as they join and says goodbye when they leave, making everyone feel welcome.

Know Who's Online: Just type online or offline to see who's around.

The "BRB" System: Stepping away? Just type brb and the bot will track your status. It automatically knows when you're back and removes you from the list!

---

<p align="center">
  <a href="#features"><img width="100" height="100" src="https://img.icons8.com/stickers/100/automatic.png" alt="Key Features" title="Key Features" /></a>
  <span style="font-size:2em;"></span>
  <a href="#use-cases"><img width="100" height="100" src="https://img.icons8.com/bubbles/100/cursor.png" alt="Use Cases" title="Use Cases" /></a>
  <span style="font-size:2em;"></span>
  <a href="#mainpy"><img width="100" height="100" src="https://img.icons8.com/clouds/100/python.png" alt="main.py (Python)" title="main.py (Python)" /></a>
  <span style="font-size:2em;"></span>
  <a href="#keepalivepy"><img width="94" height="94" src="https://img.icons8.com/3d-fluency/94/last-24-hours.png" alt="keep_alive.py (24/7)" title="keep_alive.py (24/7)" /></a>
</p>

---

<details>
  <summary><h2 id="features">✨ Key Features</h2></summary>

- Stable Discord integration with discord.py
- Responds to greetings, farewells, and status words
- Tracks “brb” users in memory
- Free Replit hosting (always-on)
- 24/7 uptime via keep_alive.py and external pinging
- Secure token via environment variable
- Easy updates via GitHub

</details>

<p align="center"></p>

<details>
  <summary><h2 id="use-cases">🛠️ Use Cases</h2></summary>

- Greets new members and replies to “hi”, “hello”, etc.
- Check who’s online/offline with `online` or `offline`
- “brb” system shows who’s away and removes them when back
- Keeps your server organized and welcoming

</details>

<p align="center"></p>

<details>
  <summary><h2 id="mainpy">🐍 main.py Overview</h2></summary>

- Entry point for the Discord bot
- Sets up client/intents, event handlers, and command logic
- Handles greetings, farewells, status, and BRB
- Loads token securely, imports keep_alive.py for uptime

</details>

<p align="center"></p>

<details>
  <summary><h2 id="keepalivepy">🕛 keep_alive.py (24/7)</h2></summary>

- Runs a lightweight Flask web server for uptime monitoring
- Keeps the bot alive on Replit by responding to pings
- Import and call `keep_alive()` from `main.py`

</details>

---

## How to Use

- **Greetings:** Type "hello", "hi", etc. for a reply.
- **Farewells:** Type "bye", "goodbye", etc. for a polite farewell.
- **Status:** Type `online` / `offline` to see who’s available.
- **BRB:** Type "brb" to be added to the list; send any message to return.

---

> **Tip:** Click the images at the top to jump to each section!

---

<!-- Embed Scribe tutorial at the end -->
Scribe Toturial to setup
https://scribehow.com/embed/Create_and_Add_a_Greety_Bot_to_Your_Server__6gLXerxuQ7ySjCAHLmDFog
