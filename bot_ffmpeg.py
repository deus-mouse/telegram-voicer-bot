# - *- coding: utf- 8 - *-
import json

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

mac_pattern_1 = r'[Мм]а[кг]'
mac_pattern_2 = r'[Гг][ао]вно+'
mac_pattern_3 = r'г\*{4}'

son_pattern_1 = r'[Мм]олодец'
son_pattern_2 = r'[Сс]ына*'

all_pattern_1 = r'[Рр]ебят'
all_pattern_2 = r'@all'
all_pattern_3 = r'@все'

users = []

# @bot.message_handler(content_types=["voice"])
# def voice_handler(message):
#     id_file = message.voice.file_id
#     file = bot.get_file(id_file)
#     down_file = bot.download_file(file.file_path)
#     with open("voice_ogg.ogg", "wb") as f:
#         f.write(down_file)
#
#     process = subprocess.run(['ffmpeg', '-i', 'voice_ogg.ogg', 'voice_wav.wav', '-y'])
#
#     file = sr.AudioFile('voice_wav.wav')
#
    # try:
    #     with file:
    #         audio = r.record(file)
    #         text = r.recognize_google(audio, language="ru_RU")
    #
    #         matched_1 = re.search(mac_pattern_1, text)
    #         matched_3 = re.search(mac_pattern_3, text)
    #
    #         bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id)
    #         if matched_1 and matched_3:
    #             bot.send_message(message.chat.id, "сам ты говно", reply_to_message_id=message.message_id)
    #
    # except Exception as ex:
    #     bot.send_message(message.chat.id, "пшык/рыг/пердежь", reply_to_message_id=message.message_id)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    matched_1 = re.search(mac_pattern_1, message.text)
    matched_2 = re.search(mac_pattern_2, message.text)
    if matched_1 and matched_2:
        bot.send_message(message.chat.id, "сам ты говно", reply_to_message_id=message.message_id)

    matched_4 = re.search(son_pattern_1, message.text)
    matched_5 = re.search(son_pattern_2, message.text)
    if matched_4 and matched_5:
        bot.send_message(message.chat.id, "спасибо создатель \U0001F916", reply_to_message_id=message.message_id)

    # matched_5 = re.search(all_pattern_1, message.text)

    if message.from_user.id not in users:
        users.append(message.from_user.id)
        username = bot.get_chat_member(message.chat.id, message.from_user.id).user.username
        bot.send_message(279478014, f"новый пользователь {username} = {message.from_user.id}")


bot.polling(none_stop=True)
