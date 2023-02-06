import re
from bot.instances import *
from random import randint
import subprocess


def mac_govno(message):
    matched_1 = re.search(mac_pattern_1, message.text)
    matched_2 = re.search(mac_pattern_2, message.text)
    if matched_1 and matched_2:
        bot.send_message(message.chat.id, "сам ты говно", reply_to_message_id=message.message_id)


def nice_son(message):
    matched_4 = re.search(son_pattern_1, message.text)
    matched_5 = re.search(son_pattern_2, message.text)
    if matched_4 and matched_5 and message.from_user.id == 279478014:  # Я
        bot.send_message(message.chat.id, "спасибо создатель \U0001F916", reply_to_message_id=message.message_id)


def pin_all(message):
    if message.chat.id in members_dict.keys():
        matched_5 = re.search(all_pattern_1, message.text)
        matched_6 = re.search(all_pattern_2, message.text)
        if matched_5 or matched_6:
            mentions = []
            for member in members_dict[message.chat.id]:
                username = bot.get_chat_member(message.chat.id, member).user.username
                if username is None:
                    username = "Хербезника"
                mention = "[" + username + "](tg://user?id=" + str(member) + ")"
                mentions.append(mention)
            pin_message = ' '.join(mentions)
            bot.send_message(message.chat.id, pin_message, parse_mode="Markdown")


def communism(message):
    matched_7 = re.search(reds_pattern_1, message.text)
    matched_8 = re.search(reds_pattern_2, message.text)
    if matched_7 or matched_8:
        dice = randint(1, 24)
        if dice < 12:
            bot.send_audio(chat_id=message.chat.id, audio=open(f'media/communism/audio ({dice}).mp3', 'rb'),
                           reply_to_message_id=message.message_id)
        elif dice >= 12:
            bot.send_photo(message.chat.id, photo=open(f'media/communism/photo ({dice}).jpg', 'rb'),
                           reply_to_message_id=message.message_id)


def get_new_member_id(message):
    if message.from_user.id not in members_dict[message.chat.id].keys():
        # family_members.append(message.from_user.id)
        username = bot.get_chat_member(message.chat.id, message.from_user.id).user.username
        bot.send_message(279478014, f"новый пользователь {username} = {message.from_user.id}")


def abrakadabra_translator(message):
    matched_9 = re.search(layout_pattern_1, message.text)
    matched_10 = re.search(layout_pattern_2, message.text)
    matched_11 = re.search(layout_pattern_3, message.text)
    if (matched_9 or matched_10) and not matched_11:
        bot.send_message(message.chat.id, message.text.translate(layout), reply_to_message_id=message.message_id)


def get_audio(message):
    id_file = message.voice.file_id
    file = bot.get_file(id_file)
    down_file = bot.download_file(file.file_path)
    with open("voice_ogg.ogg", "wb") as f:
        f.write(down_file)


def convert_ogg_to_wav():
    subprocess.run(['ffmpeg', '-i', 'voice_ogg.ogg', 'voice_wav.wav', '-y'])
    file = sr.AudioFile('voice_wav.wav')
    return file


def audio_speech_recognition(message, file):
    try:
        with file:
            audio = r.record(file)
            text = r.recognize_google(audio, language="ru_RU")
            bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id)
    except Exception:
        bot.send_message(message.chat.id, "пшык/рыг/пердежь", reply_to_message_id=message.message_id)
    finally:
        bot.send_message(279478014, f'asr uses in {message.chat.id}')


def answer_from_chatgpt(prompt: str):
    answer = 'sorry, very busy'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    if response:
        answer = response.get('choices')[0].get('text')
    return answer


def chatgpt(message):
    try:
        answer = answer_from_chatgpt(message.text)
        bot.send_message(message.chat.id, answer, reply_to_message_id=message.message_id)
    except Exception as ex:
        bot.send_message(message.chat.id, "sorry, very busy", reply_to_message_id=message.message_id)
        bot.send_message(279478014, f"chatgpt error in {message.chat.id}: {ex}")
    finally:
        bot.send_message(279478014, f'chatgpt uses in {message.chat.id}')

