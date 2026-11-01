import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. Render bepul tarifda uxlab qolmasligi uchun kichik veb-server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# 2. Telegram bot qismi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men serverda muvaffaqiyatli ishlayapman. Tez orada Mafiya o'yinini qo'shamiz!")

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("XATO: BOT_TOKEN topilmadi!")
        return

    threading.Thread(target=run_web_server, daemon=True).start()

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot ishga tushdi...")
    application.run_polling()

if __name__ == '__main__':
    main()
