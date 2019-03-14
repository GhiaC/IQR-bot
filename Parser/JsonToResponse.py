from Constants.message_component import *


class Conversation:
    def shop_response(json_message):
        result = ''
        for shop in json_message['GetShopsResponse']['shops']:
            result += MessageComponent.shop_name + \
                      shop['shopName'] + ' ' + MessageComponent.see_shop + '(send:/s' + str(shop['id']) + ')\n'
        return result
