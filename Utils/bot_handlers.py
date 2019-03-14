from Bot.bot import *
from Constants.bot_command import Command
from Constants.common import Pattern, BotState
from Constants.button_messages import ButtonMessage
from telegram.ext import *


def bot_handlers(dp):
    dp.add_error_handler(error)
    conversation_handler = ConversationHandler(entry_points=[CommandHandler(Command.start, start)], states={

        BotState.start: [RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.start),
                                      callback=customer_menu)],

        BotState.customer_menu: [RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_stores),
                                              callback=send_location_for_stores, pass_user_data=True),
                                 RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_discounts),
                                              callback=send_location_for_discount, pass_user_data=True)],

        BotState.give_location: [
            MessageHandler(filters=Filters.location, callback=get_near_stores, pass_user_data=True)
        ],

        BotState.send_request: [RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_stores),
                                             callback=get_near_stores, pass_user_data=True)]
    },

                                               fallbacks=[CommandHandler(Command.cancel, customer_menu)]
                                               )
    dp.add_handler(conversation_handler)
