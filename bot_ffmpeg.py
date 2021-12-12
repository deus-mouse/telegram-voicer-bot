# - *- coding: utf- 8 - *-
import json

import telebot
import speech_recognition as sr
import subprocess
from importlib import reload
import sys
import re
import config
from random import randint

reload(sys)

r = sr.Recognizer()

bot = telebot.TeleBot(config.bot_token)

mac_pattern_1 = r'[Мм]а[кг]'
mac_pattern_2 = r'[Гг][ао]вно+'
mac_pattern_3 = r'г\*{4}'

son_pattern_1 = r'[Мм]олодец'
son_pattern_2 = r'[Сс]ына*'

all_pattern_1 = r'@all'
all_pattern_2 = r'@все'

reds_pattern_1 = r'[Кк]расны[йе]'
reds_pattern_2 = r'[Кк]оммунизм[ау]?'

layout_pattern_1 = r'[a-z]'
layout_pattern_2 = r'http'
layout_pattern_3 = r'www'

members_dict = {-1001331225117:  # сычевальня
                    {279478014: "Я",
                     226334433: "Влад",
                     368933884: "Мех",
                     84857915: "Авдеев",
                     359600402: "Артем",
                     251890418: "Андрей",
                     150825016: "Крем",
                     135607947: "Валек",
                     223594982: "Вадим",
                     330559689: "Кодзима",
                     },
                -282972466:  # семья
                    {279478014: "Я",
                     402577355: "Настя",
                     492791113: "Тоня",
                     565280817: "Лиза",
                     565712281: "Денис",
                     457526700: "Лена",
                     }}

layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                           "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))

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
def logic_handler(message):
    chat_id = message.chat.id

    matched_1 = re.search(mac_pattern_1, message.text)
    matched_2 = re.search(mac_pattern_2, message.text)
    if matched_1 and matched_2:
        bot.send_message(message.chat.id, "сам ты говно", reply_to_message_id=message.message_id)

    # Молодец сына -
    matched_4 = re.search(son_pattern_1, message.text)
    matched_5 = re.search(son_pattern_2, message.text)
    if matched_4 and matched_5 and message.from_user.id == 279478014:
        bot.send_message(message.chat.id, "спасибо создатель \U0001F916", reply_to_message_id=message.message_id)

    # @all @все
    matched_5 = re.search(all_pattern_1, message.text)
    matched_6 = re.search(all_pattern_2, message.text)
    if matched_5 or matched_6:
        mentions = []
        for member in members_dict[chat_id]:
            username = bot.get_chat_member(message.chat.id, member).user.username
            if username is None:
                username = "Хербезника"
            mention = "[" + username + "](tg://user?id=" + str(member) + ")"
            mentions.append(mention)
        string = ' '.join(mentions)
        bot.send_message(message.chat.id, string, parse_mode="Markdown")

    # красные
    matched_7 = re.search(reds_pattern_1, message.text)
    matched_8 = re.search(reds_pattern_2, message.text)
    if matched_7 or matched_8:
        dice = randint(1, 24)
        if dice < 12:
            bot.send_audio(chat_id=chat_id, audio=open(f'media/communism/audio ({dice}).mp3', 'rb'),
                           reply_to_message_id=message.message_id)
        elif dice >= 12:
            bot.send_photo(chat_id, photo=open(f'media/communism/photo ({dice}).jpg', 'rb'),
                           reply_to_message_id=message.message_id)

    # # данный блок собирает id вновь написавших пользователей
    # if message.from_user.id not in family_members.values():
    #     # family_members.append(message.from_user.id)
    #     username = bot.get_chat_member(message.chat.id, message.from_user.id).user.username
    #     bot.send_message(279478014, f"новый пользователь {username} = {message.from_user.id}")

    # перевод абракадабры
    matched_9 = re.search(layout_pattern_1, message.text)
    matched_10 = re.search(layout_pattern_2, message.text)
    matched_11 = re.search(layout_pattern_3, message.text)
    if (matched_9 or matched_10) and not matched_10:
        bot.send_message(message.chat.id, message.text.translate(layout), reply_to_message_id=message.message_id)


bot.polling(none_stop=True)
