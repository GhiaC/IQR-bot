from telegram import ReplyKeyboardMarkup

from Constants.button_messages import ButtonMessage
from Constants.bot_messages import BotMessage
from Utils.logger import iqr_bot_logger


def start(bot, update):
    general_message = BotMessage.start
    reply_keyboard = [[ButtonMessage.start]]
    update.message.reply_text(general_message, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


def help(bot, update):
    update.message.reply_text(BotMessage.quide)


def error(bot, update):
    iqr_bot_logger.warning('Update "%s" caused error "%s"', update, update.message)

