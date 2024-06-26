import os
from dotenv import load_dotenv
from telegram import Update 
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    start_handler = CommandHandler('start', start)

    app = ApplicationBuilder().token(token).build()
    app.add_handler(start_handler)
    app.run_polling()
