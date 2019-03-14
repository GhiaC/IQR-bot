import requests
from telegram import ReplyKeyboardMarkup, LabeledPrice

from Bot.bot_config import BotConfig
from Constants.bot_messages import BotMessage
from Constants.button_messages import ButtonMessage
from Constants.common import BotState
from Parser.JsonToResponse import *
from Requests.RequestModel import *
from Utils.general_handlers import getting_user_info
from Utils.logger import iqr_bot_logger


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


def customer_menu(bot, update, user_data):
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
    return BotState.get_nearest_stores


def show_shop(bot, update, user_data):
    result = update.message.to_dict()

    chat_id = getting_user_info(update)

    request = requests.post(BotConfig.server_address + 'api/shop/' + result.get("text"))
    json_message = request.json()
    bot_response = Conversation.show_shop_response(json_message)
    bot.send_message(chat_id, bot_response)

    bot.send_location(chat_id, json_message['GetShopResponse']['shop']['lat'],
                      json_message['GetShopResponse']['shop']['long'])

    bot_response = Conversation.show_product_response(json_message)
    bot.send_message(chat_id, bot_response)

    return BotState.show_shop

    bot_response = Conversation.show_shop_response(request.json())

    chat_id = getting_user_info(update)
    bot.send_message(chat_id, bot_response)
    return BotState.show_shop


def error(bot, update):
    iqr_bot_logger.warning('Update "%s" caused error "%s"', update, update.message)
