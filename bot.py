
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut, c’est Jessy 💋")

app = ApplicationBuilder().token("7909147695:AAGxDZVEOiuHRtwTCgpV-1FMpNE16iT9W40").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
