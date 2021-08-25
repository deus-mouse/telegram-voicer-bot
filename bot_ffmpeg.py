'''
https://www.youtube.com/watch?v=0Usraq7SjiM
https://www.youtube.com/watch?v=eMk4feaZ6Gs
'''
import time

import telebot
import speech_recognition as sr
import subprocess

from config import bot_token

r = sr.Recognizer()

bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=["voice"])
def handle(message):
    id_file = message.voice.file_id
    file = bot.get_file(id_file)
    down_file = bot.download_file(file.file_path)
    with open("voice_ogg.ogg", "wb") as f:
        f.write(down_file)

    print("Сохранили")

    process = subprocess.run(['ffmpeg', '-i', 'voice_ogg.ogg', 'voice_wav.wav', '-y'])

    file = sr.AudioFile('voice_wav.wav')
    print("Передали в file")
    print(file)

    with file:
        audio = r.record(file)
        print("audio = r.record(source)")
        text = r.recognize_google(audio, language="ru_RU")
        print("text = r.recognize_google(audio, language=ru_RU)")

        bot.send_message(message.chat.id, text)
        print("bot.send_message(message.chat.id, text)")


bot.polling(none_stop=True)
