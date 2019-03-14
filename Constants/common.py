class UserData:
    stores_list = "stores_list"
    show_stores = "show_stores"
    show_discounts = "show_discounts"
    payment_product_id = "payment_product_id"


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
    show_shop = "GET_SHOP"
    show_product = "GET_PRODUCT"
    success_payment = "SUCCESS_PAYMENT"


class Pattern:
    absolute = "^{}$"
    zero = 0


class Mode:
    stores_mode = 1
    discounts_mode = 2


class ApiData:
    api_shops = "api/shops"
    api_shop = "api/shop/"
    api_product = "api/product/"
    success_payment = "api/successpayment"
    text = "text"
    get_shop_response = "GetShopResponse"
    get_product_response = "GetProductResponse"
    shop = "shop"
    product = "product"


class Product:
    id = 'id'
    title = 'title'
    text = 'text'
    payload = ""
    card_number = "5022291034483444"
    start_parameter = ""
    currency = "USD"
    picture = 'picture'
    price = 'price'
    discount = 'discount'


class LogMessage:
    warrning = 'Update "%s" caused error "%s"'
