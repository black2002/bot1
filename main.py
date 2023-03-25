import telebot
from cfg import *
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])

def text(message):
      if message.text=="Привет": bot.send_message(message.from_user.id,'Привет')
      elif message.text == "Пока": bot.send_message(message.from_user.id, 'Пока')
      elif message.text != "/start": bot.send_message(message.from_user.id, 'Не понял')
bot.infinity_polling()