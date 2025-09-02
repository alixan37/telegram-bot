import telebot
from flask import Flask, request

TOKEN = "8259514020:AAE4TKHp0iopshQpetCLbYqXg2tOFpfEIiA"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Oddiy handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Men ishga tushdim ✅")

# Flask route (webhook uchun)
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://telegram-bot-t2vb.onrender.com/" + TOKEN)
    return "Webhook set", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
