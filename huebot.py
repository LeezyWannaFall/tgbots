import random
import telebot
from telebot import types

bot = telebot.TeleBot('6713487649:AAEBVQvu-2RePQC1-78-SZEAv-u-OH0a9fk')

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "Напиши любой текст, и я добавлю хуе к рандомному слову")

@bot.message_handler(func=lambda m: True)
def echo_message(message):
    text = message.text
    words = text.split()
    
    index = random.randint(0, len(words) - 1)
    word = words[index]
    
    new_word = f'хуе{word}'
    
    modified_text = ' '.join([w if i != index else new_word for i, w in enumerate(words)])
    
    bot.send_message(message.chat.id, modified_text)

bot.infinity_polling()

