class RequestModel:
    def get_nearest_stores(mode, lat, long):
        return {'mode': int(mode), 'lat': str(lat), 'long': str(long)}

    def success_payment(chat_id, product_id):
        return {'chat_id': str(chat_id), 'product_id': str(product_id)}
