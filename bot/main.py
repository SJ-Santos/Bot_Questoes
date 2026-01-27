import os 
import telebot
from dotenv import load_dotenv

load_dotenv()
Token = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['começo'])
def send_welcome(message):
    #usar metodo do handlers.py
    pass

@bot.message_handler(commands=['ajuda'])
def send_help(message):
   #usar metodo do handlers.py
    pass

@bot.message_handler(commands=['sobre'])
def send_about(message):
    #usar metodo do handlers.py
    pass

@bot.message_handler(commands=['gerar_questao']) # o gerar questão ele vai além de gerar as questoes em pdf, tambem vai corrigir
def gerar_questao(message):
    #usar metodo do handlers.py
    pass

@bot.message_handler(commands=['ensinar'])
def ensinar(message):
    #usar metodo do handlers.py
    pass

bot.infinity_polling()