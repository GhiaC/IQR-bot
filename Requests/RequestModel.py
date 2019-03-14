class RequestModel:
    def get_nearest_stores(mode, lat, long):
        return {'mode': int(mode), 'lat': str(lat), 'long': str(long)}
