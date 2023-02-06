import telebot
import speech_recognition as sr
import config
import openai


r = sr.Recognizer()

bot = telebot.TeleBot(config.bot_token)
openai.api_key = config.openai_api_key


mac_pattern_1 = r'[Мм]а[кг]'
mac_pattern_2 = r'[Гг][ао]вно+'
mac_pattern_3 = r'г\*{4}'

son_pattern_1 = r'[Мм]олодец'
son_pattern_2 = r'[Сс]ына*'

all_pattern_1 = r'@all'
all_pattern_2 = r'@все'

reds_pattern_1 = r'(^|\s)[Кк]расн'
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
