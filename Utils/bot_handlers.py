from telegram.ext import CommandHandler, ConversationHandler, RegexHandler

from Bot.bot import start, error, customer_menu, send_location
from Constants.bot_command import Command
from Constants.common import Pattern, BotState
from Constants.button_messages import ButtonMessage


def bot_handlers(dp):
    dp.add_error_handler(error)
    conversation_handler = ConversationHandler(entry_points=[CommandHandler(Command.start, start)], states={

            BotState.start: [RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.start),
                                          callback=customer_menu)],

            BotState.help: [RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.return_to_main_menu),
                                         callback=customer_menu, pass_user_data=True)],

            BotState.customer_menu: [RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_stores),
                                                  callback=send_location, pass_user_data=True),
                                     RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_discounts),
                                                  callback=send_location, pass_user_data=True)]
        },

        fallbacks=[CommandHandler(Command.cansel, customer_menu)]
    )
    dp.add_handler(conversation_handler)
