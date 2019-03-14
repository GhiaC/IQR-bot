from States.costumer_state import *
from States.admin_state import *
from Constants.bot_command import Command
from Constants.common import Pattern, BotState
from Constants.button_messages import ButtonMessage
from telegram.ext import *


def bot_handlers(dp):
    dp.add_error_handler(error)
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler(Command.start, start, pass_user_data=True)], states={

            BotState.start: [RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.start),
                                          callback=customer_menu, pass_user_data=True)],

            BotState.customer_menu: [CommandHandler(Command.start, start),
                                     RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_stores),
                                                  callback=send_location_for_stores, pass_user_data=True),
                                     RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_discounts),
                                                  callback=send_location_for_discount, pass_user_data=True)],

            BotState.give_location: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.location, callback=get_near_stores, pass_user_data=True)
            ],

            BotState.get_nearest_stores: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=show_shop, pass_user_data=True)
            ],

            BotState.show_shop: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=show_product, pass_user_data=True)

            ],
            BotState.show_product: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=success_payment, pass_user_data=True)
            ],
            BotState.success_payment: [
                CommandHandler(Command.start, start, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_stores),
                             callback=show_product, pass_user_data=True)
            ],

            BotState.admin_menu: [
                CommandHandler(Command.start, start, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.add_file),
                             callback=change_state_to_upload, pass_user_data=True),
            ],
            BotState.admin_file_upload : [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.photo, callback=add_file, pass_user_data=True)
            ]

        },

        fallbacks=[CommandHandler(Command.cancel, customer_menu)]
    )
    dp.add_handler(conversation_handler)
