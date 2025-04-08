
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut, c’est Jessy 💋")

app = ApplicationBuilder().token("123456789:ABCdefGhIJKlMNOpQRstuVWxyZ").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
