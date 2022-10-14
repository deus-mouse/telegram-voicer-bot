from bot.bot_handler import bot


if __name__ == '__main__':
    # bot.polling(none_stop=True)
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
