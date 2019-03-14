class RequestModel:
    def get_nearest_stores(mode, lat, long):
        return {'mode': mode, 'lat': str(lat), 'long': str(long)}
