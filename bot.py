import telebot

TOKEN = "8259514020:AAE4TKHp0iopshQpetCLbYqXg2tOFpfEIiA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Bot ishlayapti ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
