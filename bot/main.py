import os 
import telebot
from dotenv import load_dotenv

load_dotenv()

Token = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['começo'])
def send_welcome(message):
    bot.reply_to(message, "Bem-vindo ao Bot de Questões!")

@bot.message_handler(commands=['ajuda'])
def send_help(message):
    bot.reply_to(message, "ajuda")

@bot.message_handler(commands=['sobre'])
def send_about(message):
    bot.reply_to(message, "sobre")

@bot.message_handler(commands=['gerar_questao'])
def gerar_questao(message):
    bot.reply_to(message, "gerar_questao")

@bot.message_handler(commands=['ensinar'])
def ensinar(message):
    bot.reply_to(message, "ensinar")

bot.infinity_polling()