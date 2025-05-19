import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Configuration de logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Détection du ton
def detect_tone(message):
    message = message.lower()
    if any(word in message for word in ["hihi", "tu veux", "chaud", "viens", "envie"]):
        return "flirt"
    elif any(word in message for word in ["lol", "mdr", "blague", "haha"]):
        return "humour"
    elif any(word in message for word in ["ah bon", "vraiment", "ok...", "super"]):
        return "ironie"
    else:
        return "neutre"

# Réponse en fonction du ton
def jessy_reply(tone):
    if tone == "flirt":
        return "Tu cherches à me faire craquer ? Parce que tu t'y prends plutôt bien 😏"
    elif tone == "humour":
        return "T’es vraiment un petit clown toi 😂"
    elif tone == "ironie":
        return "Wow, quelle répartie... j’en suis presque impressionnée 😌"
    else:
        return "Mmmh… dis-m’en plus, j’écoute 💋"

# Génération de vocal avec ElevenLabs
def generate_voice(text, filename):
    api_key = os.getenv("ELEVEN_API_KEY")
    voice_id = "EXAVITQu4vr4xnSDxMaL"  # Voix par défaut, à personnaliser
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        return True
    else:
        logging.error(f"Erreur vocal: {response.text}")
        return False

# Gestion des messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    tone = detect_tone(user_text)
    reply_text = jessy_reply(tone)

    await update.message.reply_text(reply_text)

    # Génère et envoie le vocal
    voice_path = f"voice/jessy_reply.ogg"
    if generate_voice(reply_text, voice_path):
        with open(voice_path, "rb") as voice_file:
            await update.message.reply_voice(voice_file)

# Main bot
if __name__ == '__main__':
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()