from telegram.ext import Updater
from Config.bot_config import BotConfig
from Utils.bot_handlers import bot_handlers

if __name__ == '__main__':
    updater = Updater(token=BotConfig.bot_token, base_url=BotConfig.base_url)
    dp = updater.dispatcher
    bot_handlers(dp=dp)
    updater.start_polling(BotConfig.poll_interval)
    updater.idle()
