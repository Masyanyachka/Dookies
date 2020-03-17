import telebot
import config
import random
import quotes
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🍪 Получить печеньку с предсказанием!")
    item2 = types.KeyboardButton("⌛ Сколько времени осталось?")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот который выдает печеньку с предсказанием!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🍪 Получить печеньку с предсказанием!':
        	quote = quote.Quote(quotes.QUOTES)
            bot.send_message(message.chat.id, str(random.choices(quote)))
        elif message.text == '⌛ Сколько времени осталось?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
# RUN
bot.polling(none_stop=True)
