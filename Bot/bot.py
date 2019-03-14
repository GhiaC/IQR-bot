from telegram import ReplyKeyboardMarkup, LabeledPrice
import requests

from Bot.bot_config import BotConfig
from Constants.bot_messages import BotMessage
from Constants.button_messages import ButtonMessage
from Constants.common import BotState, UserData, Mode, ApiData, Pattern, Product, LogMessage
from Parser.JsonToResponse import *
from Requests.RequestModel import *
from Utils.general_handlers import getting_user_info, getting_message_to_dict, getting_message_info
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
    reply_keyboard = [[ButtonMessage.show_stores, ButtonMessage.show_discounts]]
    bot.send_message(getting_user_info(update), BotMessage.customer_menu, reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))
    return BotState.customer_menu


def send_location_for_stores(bot, update, user_data):
    user_data[UserData.show_stores] = Mode.stores_mode
    bot.send_message(getting_user_info(update), BotMessage.give_location)
    return BotState.give_location


def send_location_for_discount(bot, update, user_data):
    user_data[UserData.show_discounts] = Mode.discounts_mode
    bot.send_message(getting_user_info(update), BotMessage.give_location)
    return BotState.give_location


def get_near_stores(bot, update, user_data):
    # TODO handle get location info
    user_data[UserData.show_stores] = Mode.stores_mode
    lat = 50
    long = 50

    request_model = RequestModel.get_nearest_stores(user_data[UserData.show_stores], lat, long)
    request = requests.post(BotConfig.server_address + ApiData.api_shops, json=request_model)
    bot_response = Conversation.shop_response(request.json())
    bot.send_message(getting_user_info(update), bot_response)
    return BotState.get_nearest_stores


def show_shop(bot, update, user_data):
    result = getting_message_to_dict

    request = requests.post(BotConfig.server_address + ApiData.api_shop + result.get(ApiData.text))
    json_message = request.json()
    bot_response = Conversation.show_shop_response(json_message)
    bot.send_message(getting_user_info(update), bot_response)

    bot.send_location(getting_user_info(update), json_message[ApiData.get_shop_response][ApiData.shop]['lat'],
                      json_message[ApiData.get_shop_response][ApiData.shop]['long'])

    bot_response = Conversation.show_product_response(json_message)
    bot.send_message(getting_user_info(update), bot_response)

    return BotState.show_shop


def show_product(bot, update, user_data):
    result = update.message.to_dict()

    request = requests.post(BotConfig.server_address + ApiData.api_product + result.get(ApiData.text))

    product = request.json()[ApiData.get_product_response][ApiData.product][Pattern.zero]
    # picture = product[Product.picture]

    bot.send_invoice(getting_user_info(update), product[Product.title], product[Product.text], Product.payload,
                     Product.card_number, Product.start_parameter, Product.currency,
                     prices=[
                         LabeledPrice(product[Product.title],
                                      int(int(product[Product.price]) * 1.0 - (int(product[Product.discount]) / 100.0)
                                          * int(product[Product.price])))
                     ])  # , photo_url=BotConfig.server_address + 'images/' + bot_response.picture)

    return BotState.show_shop


def error(bot, update):
    iqr_bot_logger.warning(LogMessage.warrning, update, update.message)
