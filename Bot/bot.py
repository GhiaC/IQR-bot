from telegram import ReplyKeyboardMarkup

from Constants.button_messages import ButtonMessage
from Constants.bot_messages import BotMessage
from Constants.common import BotState
from Utils.logger import iqr_bot_logger
from Utils.general_handlers import getting_user_info
import requests
from Bot.bot_config import BotConfig
from Requests.RequestModel import *
from Responses.ResponseModel import *
import json
from Parser.JsonToResponse import *


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
    # TODO handle get location info
    user_data['mode'] = 1
    lat = 50
    long = 50

    request_model = RequestModel.get_nearest_stores(user_data['mode'], lat, long)

    request = requests.post(BotConfig.server_address + 'api/shops', json=request_model)

    bot_response = Conversation.shop_response(request.json())

    chat_id = getting_user_info(update)
    bot.send_message(chat_id, bot_response)
    return BotState.customer_menu


def error(bot, update):
    iqr_bot_logger.warning('Update "%s" caused error "%s"', update, update.message)
