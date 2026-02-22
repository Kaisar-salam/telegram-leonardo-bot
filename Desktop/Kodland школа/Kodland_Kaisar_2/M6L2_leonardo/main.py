import telebot
import config 
import leonardo


bot = telebot.TeleBot(config.token_tg)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для генерации изображений с помощью Leonardo AI. Напиши мне, что ты хочешь увидеть на картинке, и я сгенерирую её для тебя!")

@bot.message_handler(content_types=['text'])
def processing_message(message):
    text = message.text
    img = leonardo.generate_image(text)
    bot.send_message(message.chat.id, img)    
    
bot.infinity_polling()