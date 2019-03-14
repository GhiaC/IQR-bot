def getting_user_info(update):
    return update.message.chat_id


def getting_message_info(update):
    return update.message.text


def getting_message_to_dict(update):
    return update.message.to_dict()
