import telebot

TOKEN = "8259514020:AAE4TKHp0iopshQpetCLbYqXg2tOFpfEIiA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Bot ishlayapti ✅")

bot.polling()
