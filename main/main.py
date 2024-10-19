import random
import telebot
from telebot.types import Message
bot = telebot.TeleBot('7481085810:AAFwunvRN52IQhVfXvpHGZupWA46q8qp23w')



@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message, 'Привет 😊')


@bot.message_handler(commands=['random'])
def cmd_random(message: Message):
    if random.randint(0, 1) == 0:
        bot.reply_to(message, 'Вам выпала решка!')
    else:
        bot.reply_to(message, 'Вам выпал орёл!')

@bot.message_handler(commands=['admin777'])
def admin777(message: Message):
    bot.reply_to(message, 'Se!#c&*ret Com3&*and ACTIVATED!')

@bot.message_handler(commands=['Play'])
def Play(message: Message):
    bot.reply_to(message, 'cs2 or BS')

@bot.message_handler(commands=['cs2'])
def cs2(message: Message):
    x = random.randint(1, 4)
    if x == 1:
        bot.reply_to(message, 'Нож!')
    elif x == 2:
        bot.reply_to(message, 'Пусто ¯\_(ツ)_/¯')
    elif x == 3:
        bot.reply_to(message, 'Safari Mesh- AK 47')
    elif x == 4:
        bot.reply_to(message, 'Forest Leaves.')      
    

@bot.message_handler(commands=['BS'])
def BS(message: Message):
    x = random.randint(1, 4)
    if x == 1:
        bot.reply_to(message, 'ЛЕОН!')
    elif x == 2:
        bot.reply_to(message, 'Брок')
    elif x == 3:
        bot.reply_to(message, 'Пенни')
    elif x == 4:
        bot.reply_to(message, 'Менди!')      





bot.polling()
