import random
import telebot
from telebot import types

bot = telebot.TeleBot('6713487649:AAEBVQvu-2RePQC1-78-SZEAv-u-OH0a9fk')
@bot.message_handler(commands=['start'])
def welcome_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="захуевить слово")
    button2 = telebot.types.KeyboardButton(text="вторая кнопочка")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Привет, вот что я умею: захуевить слово\nкнопка 1")

@bot.message_handler(commands=['hue'])
def echo_message(message):
    bot.send_message(message.chat.id, "Напиши любой текст, и я добавлю хуе в рандомное место")
    text = message.text
    words = text.split()
    if words.isdigit() == True:
        bot.send_message(message.chat.id, "напиши текст без цифр")
    else:
        index = random.randint(0, len(words) - 1)
        word = words[index]
        
        new_word = f'хуе{word}'
        
        modified_text = ' '.join([w if i != index else new_word for i, w in enumerate(words)])
        
        bot.send_message(message.chat.id, modified_text)



bot.infinity_polling()