import telebot
from flask import Flask, request

API_TOKEN = "SIZNING_TOKEN"
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Oddiy handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom, bot ishga tushdi!")

# Webhook qabul qiluvchi
@app.route(f'/{API_TOKEN}', methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# Asosiy sahifa
@app.route("/")
def webhook():
    return "Bot ishlayapti!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
