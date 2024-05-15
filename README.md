
# Learning Bots

This repository contains a basic "Hello, World!" Telegram bot using the `python-telegram-bot` library. The bot responds to the `/start` command and echoes any text messages sent to it.

## Prerequisites

- Python (version 3.8 or higher recommended)
- A Telegram bot token (you can get this from [BotFather](https://core.telegram.org/bots#botfather) on Telegram)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/learning-bots.git
   cd learning-bots
   ```

2. **Set Up the Environment with `pipenv`**

   Ensure you have `pipenv` installed. If not, install it using `pip`:

   ```bash
   pip install pipenv
   ```

   Create a virtual environment with `pipenv` and activate it:

   ```bash
   pipenv --python 3.8  # or another version of Python if preferred
   pipenv shell
   ```

3. **Install Dependencies**

   Install the `python-telegram-bot` library:

   ```bash
   pipenv install python-telegram-bot
   ```

4. **Set the Telegram API Key**

   Export your Telegram API key as an environment variable:

   **On Linux/macOS:**

   ```bash
   export TELEGRAM_API_KEY="YOUR_TELEGRAM_API_KEY"
   ```

   **On Windows:**

   ```bash
   set TELEGRAM_API_KEY="YOUR_TELEGRAM_API_KEY"
   ```

5. **Run the Bot**

   Run the `hello_world.py` script:

   ```bash
   python3 hello_world.py
   ```

## Code Explanation

The main script `hello_world.py` sets up a basic Telegram bot that responds to the `/start` command and echoes any text messages.

```python
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Set up logging to stdout
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"Received /start command from user {update.effective_user.id}")
    await update.message.reply_text('Hello! Welcome to my bot.')

# Function to handle text messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    logger.info(f"Received message: {user_text} from user {update.effective_user.id}")
    await update.message.reply_text(user_text)

def main() -> None:
    """Start the bot."""
    # Load the API token from the environment variable
    api_key = os.getenv('TELEGRAM_API_KEY')
    if not api_key:
        logger.error("No API key provided. Set TELEGRAM_API_KEY environment variable.")
        raise ValueError("No API key provided. Set TELEGRAM_API_KEY environment variable.")

    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token(api_key).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    
    # Register message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    logger.info("Starting the bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
```

## Troubleshooting

- Ensure your Telegram API key is correctly set as an environment variable.
- Make sure you have a stable internet connection.
- Check the logs in the terminal for any error messages.

Feel free to open an issue or submit a pull request if you encounter any problems or have suggestions for improvements.
