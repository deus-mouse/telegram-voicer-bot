'''
https://www.youtube.com/watch?v=0Usraq7SjiM
https://www.youtube.com/watch?v=eMk4feaZ6Gs
'''
import time

import telebot
import soundfile
import os

import speech_recognition as sr

r = sr.Recognizer

bot = telebot.TeleBot("1716765907:AAE7oGBYGGFgqcVas6Wlas6PZBVbpGBmfAo")


@bot.message_handler(content_types=["voice"])
def handle(message):
    file_id = message.voice.file_id
    file = bot.get_file(file_id)
    down_file = bot.download_file(file.file_path)
    with open("new.ogg", "wb") as f:
        f.write(down_file)

    print("Сохранили")

    # data, samplerate = soundfile.read('old.ogg')
    # soundfile.write('new.wav', data, samplerate, subtype='PCM_16')
    #
    # file = sr.AudioFile('new.wav')
    # print("Передали в file")
    # print(file)
    #
    #
    #
    # try:
    #     with file:
    #         print("зашли в with")
    #         time.sleep(5)
    #         audio = r.record(source=file)
    #         print("audio = r.record(source)")
    #         text = r.recognize_google(audio, language="ru_RU")
    #         print("text = r.recognize_google(audio, language=ru_RU)")
    #
    #         bot.send_message(message.chat.id, text)
    #         print("bot.send_message(message.chat.id, text)")
    # except Exception as err:
    #     print(err)

bot.polling(none_stop=True)
