import requests

from Config.bot_config import BotConfig
from Constants.common import BotState
from Utils.general_handlers import getting_user_info


def change_state_to_upload(bot, update, user_data):
    bot.send_message(getting_user_info(update), "Send your file")
    return BotState.admin_file_upload


def add_file(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("photo")) > 0:
        photo = result.get("photo")[0]
        image_url = photo.get("file_id")
        response = requests.post(BotConfig.server_address + "downloadfile/" + image_url)

    bot.send_message(getting_user_info(update), "UPLOAD FILE SUCCESSFUL!")
    return BotState.admin_menu
