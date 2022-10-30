import telebot

bot=telebot.TeleBot('5561006345:AAF-i4kNBqqpWS-XotCxlStbv9vaSCCdo6o')

@bot.message_handler(commands=['start'])
def start(message):
    mess=f'Salom, <b>{message.from_user.first_name} <u> {message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess, parse_mode='html')


bot.polling(none_stop=True)    