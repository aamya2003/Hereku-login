import telebot


bot = telebot.TeleBot("6336490086:AAEpQooiX8qpOQ-DY7ohRGSqcJ05KwwG2f4")


@bot.message_handler()
def Myfunc(message):
    bot.send_message(message.chat.id, "Hi, What's happend?")


bot.infinity_polling(skip_pending=True)
