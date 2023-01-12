from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler


def start(update, _):

    keyboard = [
        [InlineKeyboardButton(text="Вперед", callback_data='A'), ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text='А', reply_markup=reply_markup)


def button(update, _):
    query = update.callback_query
    variant = query.data

    query.answer()
    query.edit_message_text(text='B')


if __name__ == '__main__':
    updater = Updater(token='5871619023:AAHHF2nCVLj5zHezoxSfWDXJQ9vN4f1jiCM')
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()
