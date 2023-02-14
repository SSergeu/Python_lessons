import telebot

bot = telebot.TeleBot("6145434903:AAGY8MOxFfDIcYfg3NbG5p3DrBJGxb3AJt0", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Бот тех поддержки запущен. Мы готовы выслушать Ваши обращения")

@bot.message_handler(content_types=['text'])
def echo_all(message):
    data = open('seminar_10/question.txt', 'a', encoding='UTF-8')
    data.writelines(f'{message.from_user.id}: {message.text}\n')
    data.close()

bot.infinity_polling()
