from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging


updater = Updater(token='token:xxxx')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def hello(update, context):
    msg = 'Hello, World!'
    if len(context.args):
        msg = '{} {}'.format(msg, context.args[0].upper())

    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, I don\'t understand this command QwQ')


def main():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    hello_handler = CommandHandler('hello', hello)
    dispatcher.add_handler(hello_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # should be added at last
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # non-block
    updater.start_polling()

    # block
    updater.idle()


if __name__ == '__main__':
    main()
