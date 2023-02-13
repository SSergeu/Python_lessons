import telebot 
import random

bot = telebot.TeleBot("5882864761:AAF7T2me-rzwgE8kYCbtrRQup6XLRykv09E", parse_mode=None)
ind = False
game = False

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"Привет! Вы запустили моего бота.\n\
		Чтобы воспользоваться калькулятором, введите команду:\n'/считать'\n\
		Чтобы поиграть в 'Угадай число', введите команду:'/играть'")

@bot.message_handler(commands=['считать'])
def send_welcome(message):
	global ind
	bot.reply_to(message, "Введите выражение: (Например: 1+4*2)")
	ind = True

@bot.message_handler(commands=['играть'])
def send_welcome(message):
	global game
	bot.reply_to(message, f"Игра началась! Я загадал число от 1 до 1000, Ваша задача угадать его, какие варианты?\
		(Если захотите закончить игру введите сообщение 'конец игры')")
	game = True
	global numbers
	numbers = random.randint(1,1000)


	
@bot.message_handler(content_types=['text'])
def echo_all(message):
	global ind
	global game
	global numbers
	if ind:
		ans = eval(message.text)
		bot.reply_to(message, f'Ответ: {ans}')
		ind = False	
	if game:
		if message.text.isdigit():	
			if int(message.text) == numbers:
				bot.reply_to(message, 'Ура! Вы угадали! Игра закончена')
				game = False
			else:
				if int(message.text) > numbers:
					bot.reply_to(message, 'Моё число меньше')
				else:
					bot.reply_to(message, 'Моё число больше')
		elif message.text == 'конец игры':
			bot.reply_to(message, 'Игра закончена')
			game = False
		else: 
			bot.reply_to(message,'Введите число')

bot.infinity_polling()
