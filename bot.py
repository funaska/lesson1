from telegram.ext import Updater

def main():
    mybot = Updater("587083051:AAEjr2LTJc224qZjRyuFTED059vnYHJ0Qt8")
    mybot.start_polling()
    mybot.idle()
