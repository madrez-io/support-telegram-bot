# Telegram Support Bot

A simple Telegram support bot that forwards messages from users to an admin and allows the admin to reply directly.

## Requirements

* Python 3.10+
* Telegram Bot Token
* Aiogram 3

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/madrez-io/support-telegram-bot.git
cd support-telegram-bot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file based on `.env.example`.

### .env.example

```env
BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_telegram_user_id_here
```

## Getting Your Bot Token

1. Open Telegram and search for **@BotFather**.
2. Start a chat with BotFather.
3. Send:

```text
/newbot
```

4. Follow the instructions to create your bot.
5. BotFather will send you a bot token similar to:

```text
1234567890:AAExampleToken1234567890abcdef
```

6. Copy the token and paste it into your `.env` file as the value of `BOT_TOKEN`.

## Getting Your Telegram User ID

1. Open Telegram and search for **@userinfobot**.
2. Start the bot.
3. The bot will send information about your account, including your numeric user ID.

Example:

```text
Id: 123456789
```

4. Copy the ID and paste it into your `.env` file as the value of `ADMIN_ID`.

## Example Configuration

```env
BOT_TOKEN=1234567890:AAExampleToken1234567890abcdef
ADMIN_ID=123456789
```

## Running the Bot

```bash
python bot.py
```

If everything is configured correctly, you should see:

```text
Bot is starting...
```

## License

MIT License
