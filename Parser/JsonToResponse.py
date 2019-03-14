from Constants.message_component import *


class Conversation:
    def shop_response(json_message):
        result = ''
        for shop in json_message['GetShopsResponse']['shops']:
            result += MessageComponent.shop_name + \
                      shop['shopName'] + ' ' + MessageComponent.see_shop + '(send:' + str(shop['id']) + ')\n'
        return result



    def show_shop_response(json_message):
        result = ''
        shop = json_message['GetShopResponse']['shop']
        result += \
            MessageComponent.shop_name + shop['shopName'] + '\n' + \
            MessageComponent.username + shop['username'] + '\n' + \
            MessageComponent.description + shop['description'] + '\n' + \
            MessageComponent.startTime + shop['startTime'] + '\n' + \
            MessageComponent.endTime + shop['endTime'] + '\n'
        return result
