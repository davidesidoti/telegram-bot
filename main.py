import telebot
import random
import pyttsx3
from datetime import datetime
from time import sleep
import os

bot = telebot.TeleBot('5134596705:AAFhi6EFc_-Q_gz4EvH9aLHr9KgZOC9fh3Y')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


@bot.message_handler(commands=['tts'])
def tts(message):
    """
    The function takes a message as an argument, and then converts it to speech and saves it as an mp3
    file. 
    Then, the bot sends the file to the user. 
    Finally, the function removes the mp3 file from the bot's server.
    
    :param message: The message object that the bot received
    """
    message_tts = message.text.replace('/tts ', '')
    file_name = f'tts.mp3'
    engine.save_to_file(message_tts, file_name)
    engine.runAndWait()
    bot.send_audio(message.chat.id, audio=open(
        f'/public_html/cgi-bin/{file_name}', 'rb'))
    sleep(1)
    os.remove(f'/public_html/cgi-bin/{file_name}')


@bot.message_handler(commands=['randomn'])
def randomn(message):
    """
    Reply to message with random number.

    :param message: The message object that was sent by the user
    """
    params = message.text.split(' ')
    if len(params) == 2:
        result = random.randint(0, int(params[1]))
        bot.reply_to(message, str(result))
    elif len(params) == 3:
        result = random.randint(int(params[1]), int(params[2]))
        bot.reply_to(message, str(result))
    else:
        bot.reply_to(
            message, 'Utilizzo: /randomn [numero_massimo] [(opt) random_da_a]')


@bot.message_handler(content_types=['text'])
def message_content(message):
    """
    It sends a message to the user.

    :param message: The message object that the user sent
    """
    if 'mah' in message.text.lower():
        testo = ''
        for i in range(26):
            testo += 'mah '
        bot.send_message(message.chat.id, testo)
    elif 'matteo gay' in message.text.lower() or 'gay' in message.text.lower():
        testo = ''
        for i in range(26):
            testo += 'Matteo = \U0001F3F3\uFE0F\u200D\U0001F308 '
        bot.send_message(message.chat.id, testo)


bot.polling()
