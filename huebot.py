import telebot
from telebot import types

bot = telebot.TeleBot('6713487649:AAEBVQvu-2RePQC1-78-SZEAv-u-OH0a9fk')

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "Напиши любой текст, и я добавлю хуе к рандомному слову")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    new_message = list(str(message.text.split(" ")))
    for i in range(new_message):
        bot.reply_to(message, "хуе" + new_message[2].text)

bot.infinity_polling()

