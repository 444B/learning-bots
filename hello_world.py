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
