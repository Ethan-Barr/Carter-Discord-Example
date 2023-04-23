# Carter Discord Bot Example

This is a Discord bot built using Python and the nextcord library. It is designed to preform a variety of tasks but mainly to help with your programming queries. Outputs will consist of API responses from CarterLabs or from built in functions.

## Getting Started

To run your bot on your own server, you will need to set up a few things first.

1. Clone or download the repository to your local machine.
2. Navigate to the directory where the repository was cloned or downloaded.
3. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.
4. Create a new application on the [Discord Developer Portal](https://discord.com/developers/applications).
5. Create a new bot for your application and copy the bot token.
6. Create a new project on the [CarterLabs](https://controller.carterlabs.ai/welcome) dashboard and name your character. Follow the prompts on the dashboard and then create a new API key and copy it.
7. Open the config.py file and fill in or change the necessary details, as detailed below:

DiscordAPI = "ENTER YOUR DISCORD BOT TOKEN HERE."
UIName = "ENTER THE NAME OF YOUR BOT HERE."
Prefix = "ENTER YOUR PREFERRED PREFIX FOR AUTOMATION COMMANDS HERE."

8. Start running the bot `python Bot.py` in your terminal.

## Commands

The bot currently supports the following commands (Work in progress):

- `>>hello`: Jarvis will greet you.
- `>>ping`: Jarvis will respond with "Pong!" and latency.

MODERATION:
- `>>clear <number of messages>`: The bot will delete the specified number of messages in the current channel. (Only if member has the `manage messages` role)
- `>>ban <user> <reason> `: The bot will ban that user from the server. (Only if member has the `ban users` role)
- `>>clear <number of messages>`: The bot will delete the specified number of messages in the current channel. (Only if member has the `manage messages` role)
- `>>ban <user> <reason>`: The bot will ban that user from the server. (Only if member has the `ban users` role)
- `>>unban <user>`: The bot will remove the ban on the specified user from the server. (Only if member has the `ban users` role)
- `>>kick <user> <reason>`: The bot will kick the specified user from the server. (Only if member has the `kick members` role)
- `>>mute <user> <duration> <reason>`: The bot will mute the specified user for the given duration and reason. (Only if member has the `manage messages` role)
- `>>unmute <user>`: The bot will remove the mute on the specified user. (Only if member has the `manage messages` role)

Please make sure to adjust the role permissions according to your specific server's settings.


## Contributing

If you find a bug or would like to suggest a new feature, please open an issue on the GitHub repository. Pull requests are also welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
