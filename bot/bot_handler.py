# - *- coding: utf- 8 - *-
from importlib import reload
import sys
from bot.helpers import mac_govno, nice_son, pin_all, communism, abrakadabra_translator, get_audio, convert_ogg_to_wav, \
    audio_speech_recognition, chatgpt, boobs
from bot.instances import *


reload(sys)


@bot.message_handler(content_types=["voice"])
def voice_handler(message):
    try:
        get_audio(message)
        file = convert_ogg_to_wav()
        audio_speech_recognition(message, file)
    except Exception as ex:
        # bot.send_message(279478014, ex)
        print(f'Exception {ex}')


# @bot.message_handler(content_types=["text"])
@bot.message_handler(regexp="@deusmouse_shifterbot")
def logic_handler(message):
    # chat_id = message.chat.id
    # text = message.text
    # message_id = message.message_id
    # from_user_id = message.from_user.id
    # mac_govno(message)
    # nice_son(message)
    chatgpt(message)
    # pin_all(message)
    # communism(message)
    # abrakadabra_translator(message)
    # get_new_member_id(message)


# @bot.message_handler(regexp="сиськи")
# def logic_handler(message):
#     boobs(message)

