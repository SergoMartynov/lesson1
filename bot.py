#Bot for Telegram
#Bot name: oldSandman_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
	print('Вызван /start')
	print(update.message.chat_id)
	bot.sendMessage(update.message.chat_id, text='Здарова Братюня!')

def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, update.message.text)

def main():
    updater = Updater("287860128:AAEybMI56vAjXffDESjNNKhPM4Yi_4C3WuQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_error_handler(show_error)
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
	main()