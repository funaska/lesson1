# Импортируем нужные компоненты
from telegram.ext import Updater

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
	mybot = Updater("587083051:AAEjr2LTJc224qZjRyuFTED059vnYHJ0Qt8")
	mybot.start_polling()
	mybot.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
