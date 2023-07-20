# Carter Discord Bot Example

## __Getting started with Carter__

1. Head over to [Carter's Controller](https://controller.carterlabs.ai/welcome) and create an account if you havent allready.
2. Create a Project and an agent - Follow the instructions that are given on the Controller to create your agent.
3. Create an API key and Copy it to your clipboard.

## __Getting started with Discord Developer Portal__

### **Step 1: Create a Discord Application**
1. Visit the Discord Developer Portal at https://discord.com/developers/applications.
2. Log in with your Discord account.
3. Click on the "New Application" button.
4. Enter a name for your bot and click "Create."


### **Step 2: Create a Bot User**
1. In your application settings, navigate to the "Bot" tab on the left sidebar.
2. Click on the "Add Bot" button.
3. Confirm the action by clicking "Yes, do it!" when prompted.
4. Under the "Token" section, click on the "Copy" button to copy your bot token. Keep this token secure, as it provides access to your bot.
5. Turn on the following sliders to allow our bot to be operational:
- PRESENCE INTENT
- SERVER MEMBERS INTENT
- MESSAGE CONTENT INTENT
- PUBLIC BOT - That is optional

### **Step 3: Invite Your Bot to a Server**
1. In the Developer Portal, go to the "OAuth2" tab on the left sidebar.
2. Under the "Scopes" section, select the "bot" checkbox.
3. In the "Bot Permissions" section, choose the permissions your bot requires.
4. Copy the generated OAuth2 URL.
5. Open a new browser tab and paste the URL. Choose the server where you want to add the bot and authorize it.

## __Getting started with the source code__
1. Create an `.env` in the base directory it should look somehing like this: 
```env
DISCORD_TOKEN = ENTER TOKEN
BOT_PREFIX = CREATE A PREFIX
CARTER_TOKEN = ENTER CARTERAPI KEY
```
2. Install Dependencies: Open your terminal and navigate to the directory containing the source code files. Run the following command to install the required dependencies:
```
pip install -r requirements.txt
```
3. In `bot.py` you can customise the following:
- Name of discord Bot >> `line 15`
- Discord activity presence >>`line 20`
- Name of discord bot in all lowercase >> `line 52`
4. Open your terminal
5. Run `python bot.py` to be able to run your bot


## __Contributing__
If you find a bug or would like to suggest a new feature, please open an issue on the GitHub repository. Pull requests & Forks are also welcome.

Thanks to [@TheKronis](https://github.com/TheKronis) for the base template that I have expanded on & [@Cipher58](https://github.com/Cipher58) as well for some devlopment

## __Documentation__
- Carter's Documentation: <https://docs.carterlabs.ai/>
- Discord Dev Portal's Documenation : <https://discord.com/developers/docs/intro/>

## __License__
This project is licensed under the MIT License. See the LICENSE file for more information.


## __Other information/Notes__
This project will be having limited edits to it from me as the owner but still feel free to create Pull Requests. I will still autorise them and monitor this.
