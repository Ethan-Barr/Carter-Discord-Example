# Jarvis Discord Bot

Jarvis is a Discord bot built using Python and the nextcord library. Jarvis is designed to preform a varirity of tasks but mainly to help with your programming querys. Outputs will consit of API responses from CarterLabs or from built in functions

## Getting Started

To run Jarvis on your own server, you will need to set up a few things first.

1. Clone or download the repository to your local machine.
2. Navigate to the directory where the repository was cloned or downloaded.
3. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.
4. Create a new application on the [Discord Developer Portal](https://discord.com/developers/applications).
5. Create a new bot for your application and copy the bot token.
6. Create a new project on the [CarterLabs](https://controller.carterlabs.ai/welcome) dashboard and name your charater. Follow the promts on the dashboard and then create a new API key and copy it.
7. Create a file called `config.json` in the folder `Utils`. Copy this code but change the relative parts:

```json
{
  "token": "ADD DISCORD BOT TOKEN",
  "prefix": "ADD YOUR DISCORD BOT PREFIX/WAKEWORD",
  "carterKey": "ADD CARTERLABS API KEY"
}
```

8. Start running the bot `python Jarvis.py` in your terminal.

## Commands

Jarvis currently supports the following commands:

- `!hello`: Jarvis will greet you.
- `!ping`: Jarvis will respond with "Pong!" and latency.
- `!clear <number of messages>`: Jarvis will delete the specified number of messages in the current channel.

## Contributing

If you find a bug or would like to suggest a new feature, please open an issue on the GitHub repository. Pull requests are also welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
