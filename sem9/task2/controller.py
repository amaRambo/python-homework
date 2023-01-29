import telebot
from telebot import types
global a1, a2
bot = telebot.TeleBot("5804587400:AAELkmE4RmkQKUl6745HozMTO-DfSZfH0d4")

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id,"/button")
    
@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=None)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    but5 = types.KeyboardButton("^")

    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)

    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)

@bot.message_handler(content_types = "text")
def controller(message):
    print(message.text)
    if message.text == "+":
        bot.send_message(message.chat.id,"введи два числа через пробел")
        bot.register_next_step_handler(message,plus)
    elif message.text == "-":
        bot.send_message(message.chat.id,"введи два числа через пробел")
        bot.register_next_step_handler(message,plus)
    elif message.text == "*":
        bot.send_message(message.chat.id,"введи два числа через пробел")
        bot.register_next_step_handler(message,plus)
    elif message.text == "/":
        bot.send_message(message.chat.id,"введи два числа через пробел")
        bot.register_next_step_handler(message,plus)
    elif message.text == "^":
        bot.send_message(message.chat.id,"введи два числа через пробел")
        bot.register_next_step_handler(message,plus)

def plus(message):
    a = message.text
    bot.send_message(message.chat.id,f"{int(a.split()[0])} + {int(a.split()[1])} = {int(a.split()[0]) + int(a.split()[1])}")
    button(message)


    
bot.infinity_polling()
