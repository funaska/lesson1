# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
	print('Привет!')

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
	mybot = Updater("587083051:AAEjr2LTJc224qZjRyuFTED059vnYHJ0Qt8", request_kwargs=PROXY)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	mybot.start_polling()
	mybot.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
