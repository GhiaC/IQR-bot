from telegram.ext import CommandHandler
from Bot.bot import start, error, help


def bot_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_error_handler(error)
