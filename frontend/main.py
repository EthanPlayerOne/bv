import telebot
from telebot import types
import config
import random

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Рассчитать цену на товар")
    item2 = types.KeyboardButton("Поиск поставщика")
    markup.row(item1, item2)
    bot.send_message(message.chat.id, f'hi, {name}!', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Рассчитать цену на товар":
        words = ['пися', 'попа', 'член']
        while True:
            bot.send_message(message.chat.id, random.choice(words))

bot.infinity_polling()
