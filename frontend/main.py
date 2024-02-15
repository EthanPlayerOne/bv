import telebot
from telebot import types
import config

# создание бота
bot = telebot.TeleBot(config.token)

termins = {
    'Моржинальность': 'Отношение маржи к выручке',
    'Маржа': 'Разница между ценой и себестоимостью',
    'Себестоимость': 'Стоимостная оценка текущих затрат предприятия на производство и реализацию продукции',
    'Цена': 'Количество денег, в обмен на которые продавец готов передать (продать) единицу товара'
}


@bot.message_handler(commands=['start'])
def start_message(message):
    name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Рассчитать цену на товар")
    item2 = types.KeyboardButton("Средняя цена на товар")
    markup.row(item1, item2)

    item3 = types.KeyboardButton("Поиск поставщика по фото")
    item4 = types.KeyboardButton("Словарик")
    markup.row(item3, item4)

    bot.send_message(message.chat.id, f'hi, {name}!', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Рассчитать цену на товар":
        bot.send_message(message.chat.id, 'Отправьте затраты на товар')
        bot.register_next_step_handler(message, get_expenses)
        # bot.send_message(message.chat.id, 'Отправьте какой процент маржинальности вы хотите получить')
        #
        # marja = int(message.text)
        #
        # finalps = expenses * 100 / (100 - marja)
        #
        # bot.send_message(message.chat.id, finalps)

    elif message.text == "Средняя цена на товар":
        bot.send_message(message.chat.id, f'Эта функция еще не доступна')
    elif message.text == "Поиск поставщика по фото":
        bot.send_message(message.chat.id, f'Эта функция еще не доступна')
    elif message.text == "Словарик":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1 = types.KeyboardButton("Моржинальность")
        item2 = types.KeyboardButton("Маржа")
        markup.row(item1, item2)

        item3 = types.KeyboardButton("Себестоимость")
        item4 = types.KeyboardButton("Цена")
        markup.row(item3, item4)

        item5 = types.KeyboardButton("Назад")
        markup.add(item5)

        bot.send_message(message.chat.id, f'Какой термин вас интересует?', reply_markup=markup)

    elif message.text in list(termins.keys()):
        bot.send_message(message.chat.id, termins[message.text])
    elif message.text == 'Назад':
        name = message.from_user.first_name
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1 = types.KeyboardButton("Рассчитать цену на товар")
        item2 = types.KeyboardButton("Средняя цена на товар")
        markup.row(item1, item2)

        item3 = types.KeyboardButton("Поиск поставщика по фото")
        item4 = types.KeyboardButton("Словарик")
        markup.row(item3, item4)

        bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


def get_expenses(message: types.Message):
    expenses = message.text
    bot.send_message(message.chat.id, expenses)

bot.infinity_polling()
