import telebot
from telebot import types
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime


def log(message):
    file = open('sem9/task1/db.csv', 'a')
    file.write(f'{datetime.datetime.now().time()}, {message.chat.username}, {message.chat.id}, {message.text}\n')
    file.close()