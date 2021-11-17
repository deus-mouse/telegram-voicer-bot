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

sich_members = {"Я": 279478014,
                "Влад": 226334433,
                "Мех": 368933884,
                "Авдеев": 84857915,
                "Артем": 359600402,
                "Андрей": 251890418,
                "Крем": 150825016,
                "Валек": 135607947,
                "Вадим": 223594982,
                "Кодзима": 330559689,
                }

family_members = {"Я": 279478014,
                "Денис": 565712281,
                "Настя": 402577355,
                "Лена": 457526700,
                "Лиза": 565280817,
                "Тоня": 279478014,
                }
    # [565280817,
# 457526700,
# 402577355,
# 279478014,
# 565712281]
# 279478014, 226334433, 368933884, 84857915, 359600402, 251890418, 150825016, 135607947, 223594982, 330559689]


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

            matched_1 = re.search(mac_pattern_1, text)
            matched_3 = re.search(mac_pattern_3, text)

            bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id)
            if matched_1 and matched_3:
                bot.send_message(message.chat.id, "сам ты говно", reply_to_message_id=message.message_id)

    except Exception as ex:
        bot.send_message(message.chat.id, "пшык/рыг/пердежь", reply_to_message_id=message.message_id)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    matched_1 = re.search(mac_pattern_1, message.text)
    matched_2 = re.search(mac_pattern_2, message.text)
    if matched_1 and matched_2:
        bot.send_message(message.chat.id, "сам ты говно", reply_to_message_id=message.message_id)

    # Молодец сына -
    # matched_4 = re.search(son_pattern_1, message.text)
    # matched_5 = re.search(son_pattern_2, message.text)
    # if matched_4 and matched_5:
    #     bot.send_message(message.chat.id, "спасибо создатель \U0001F916", reply_to_message_id=message.message_id)

    matched_5 = re.search(all_pattern_2, message.text)
    matched_6 = re.search(all_pattern_3, message.text)
    if matched_5 or matched_6:
        usernames = ""
        mentions = []
        for member in sich_members:
            user_id = sich_members[member]
            username = bot.get_chat_member(message.chat.id, user_id).user.username
            if username is None:
                username = "Хербезника"
            mention = "["+username+"](tg://user?id="+str(user_id)+")"
            mentions.append(mention)
        string = ' '.join(mentions)
        bot.send_message(message.chat.id, string, parse_mode="Markdown")

    matched_7 = re.search(all_pattern_1, message.text)
    if matched_7:
        usernames = ""
        mentions = []
        for member in family_members:
            user_id = family_members[member]
            username = bot.get_chat_member(message.chat.id, user_id).user.username
            if username is None:
                username = "Челбезника"
            mention = "["+username+"](tg://user?id="+str(user_id)+")"
            mentions.append(mention)
        string = ' '.join(mentions)
        bot.send_message(message.chat.id, string, parse_mode="Markdown")

    # # данный блок собирает id вновь написавших пользователей
    # if message.from_user.id not in family_members:
    #     family_members.append(message.from_user.id)
    #     username = bot.get_chat_member(message.chat.id, message.from_user.id).user.username
    #     bot.send_message(279478014, f"новый пользователь {username} = {message.from_user.id}")


bot.polling(none_stop=True)
