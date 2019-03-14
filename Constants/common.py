class UserData:
    stores_list = "stores_list"


class UserState:
    start = "start"
    help = "help"
    customer_menu = "customer_menu"
    send_location = "send_location"
    show_stores = "show_stores"


class BotState:
    start = "START"
    help = "HELP"
    menu = "MENU"
    customer_menu = "CUSTOMER_MENU"
    give_location = "GIVE_LOCATION"
    get_nearest_stores = "GET_NEAREST_STORE"


class Pattern:
    absolute = "^{}$"
