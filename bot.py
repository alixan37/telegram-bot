from flask import Flask, request
import telebot

TOKEN = "8259514020:AAE4TKHp0iopshQpetCLbYqXg2tOFpfEIiA"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Oddiy /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men ishlayapman 🚀")

# Render webhookdan update olishi uchun
@app.route("/", methods=["POST"])
def getMessage():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# Oddiy test uchun
@app.route("/")
def webhook():
    return "Bot ishlayapti!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
