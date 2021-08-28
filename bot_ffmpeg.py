# - *- coding: utf- 8 - *-

import telebot
import speech_recognition as sr
import subprocess
from importlib import reload
import sys
import re

reload(sys)

import config

r = sr.Recognizer()

bot = telebot.TeleBot(config.bot_token)


@bot.message_handler(content_types=["voice"])
def voice_handler(message):
    id_file = message.voice.file_id
    file = bot.get_file(id_file)
    down_file = bot.download_file(file.file_path)
    with open("voice_ogg.ogg", "wb") as f:
        f.write(down_file)

    process = subprocess.run(['ffmpeg', '-i', 'voice_ogg.ogg', 'voice_wav.wav', '-y'])

    file = sr.AudioFile('voice_wav.wav')

    try:
        with file:
            audio = r.record(file)
            text = r.recognize_google(audio, language="ru_RU")

            bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id)
    except Exception as ex:
        bot.send_message(message.chat.id, "пшык/рыг/пердежь")


mac_pattern_1 = r'[Мм]ак'
mac_pattern_2 = r'[Гг][ао]вно+'


@bot.message_handler(content_types=["text"])
def text_handler(message):
    matched_1 = re.search(mac_pattern_1, message.text)
    matched_2 = re.search(mac_pattern_2, message.text)
    if matched_1 and matched_2:
        bot.send_message(message.chat.id, "сам ты говно", reply_to_message_id=message.message_id)


bot.polling(none_stop=True)
