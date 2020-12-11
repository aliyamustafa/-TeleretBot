from googlesearch import search
import telebot




bot = telebot.TeleBot('1470030743:AAESIdJ-X9Srw1VYcQKFK9xCfA17XrO8F5k')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет,мой друг!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Пока, мой друг!')
    else:
        res=search(message.text)
        for element in res:
            bot.reply_to(message, element)
bot.polling()
