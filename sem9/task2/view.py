import telebot
from telebot import types

bot = telebot.TeleBot("5804587400:AAELkmE4RmkQKUl6745HozMTO-DfSZfH0d4")

def enter(a):
    bot.send_message(message.chat.id,"введи два числа через пробел")