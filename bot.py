import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

async def start(update, context):
    await update.message.reply_text("Hello toi... Moi c’est Jessy. 😏")

async def echo(update, context):
    await update.message.reply_text("Tu viens de dire : " + update.message.text)

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()
