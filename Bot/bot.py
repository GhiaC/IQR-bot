from telegram import ReplyKeyboardMarkup

from Constants.button_messages import ButtonMessage
from Constants.bot_messages import BotMessage
from Constants.common import BotState
from Utils.logger import iqr_bot_logger
from Utils.general_handlers import getting_user_info


def start(bot, update):
    general_message = BotMessage.start
    reply_keyboard = [[ButtonMessage.start]]
    update.message.reply_text(general_message, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return BotState.start


def help(bot, update):
    general_message = BotMessage.quide
    reply_keyboard = [[ButtonMessage.start, ButtonMessage.return_to_main_menu]]
    update.message.reply_text(general_message, reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return BotState.help


def customer_menu(bot, update):
    chat_id = getting_user_info(update)
    reply_keyboard = [[ButtonMessage.show_stores, ButtonMessage.show_discounts]]
    bot.send_message(chat_id, BotMessage.customer_menu, reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))
    return BotState.customer_menu


def send_location_for_stores(bot, update, user_data):
    user_data['mode'] = 1
    chat_id = getting_user_info(update)
    bot.send_message(chat_id, BotMessage.give_location)
    return BotState.give_location


def send_location_for_discount(bot, update, user_data):
    user_data['mode'] = 2
    chat_id = getting_user_info(update)
    bot.send_message(chat_id, BotMessage.give_location)
    return BotState.give_location


def get_near_stores(bot, update, user_data):
    if user_data['mode'] == 1:
        general_message = 'mode 1'
    else :
        general_message = 'mode 2'

    chat_id = getting_user_info(update)
    bot.send_message(chat_id, general_message)
    return BotState.customer_menu


def error(bot, update):
    iqr_bot_logger.warning('Update "%s" caused error "%s"', update, update.message)
