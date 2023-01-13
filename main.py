from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, ConversationHandler, ApplicationBuilder
from telegram.ext import CommandHandler


FIRST, SECOND = range(2)


async def start(update, _):

    keyboard = [
        [InlineKeyboardButton(text="Вперед", callback_data='А'), ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text='А', reply_markup=reply_markup)
    return FIRST


async def button_forward(update, _):

    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton(text="Назад", callback_data='В'), ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text='В', reply_markup=reply_markup)
    return SECOND


async def button_back(update, _):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton(text="Вперед", callback_data='А'), ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text='А', reply_markup=reply_markup)
    return FIRST


if __name__ == '__main__':

    updater = ApplicationBuilder().token('5871619023:AAHHF2nCVLj5zHezoxSfWDXJQ9vN4f1jiCM').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(button_forward, pattern='А'),
            ],
            SECOND: [
                CallbackQueryHandler(button_back, pattern='В'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    updater.add_handler(conv_handler)

    updater.run_polling()
