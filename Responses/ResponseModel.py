import json


class Shop(object):
    id = 0
    username = ''
    phoneNumber = ''
    shopName = ''
    description = ''
    startTime = ''
    endTime = ''
    stars = 0
    lat = ''
    long = ''
    categoryId = 0
    created_at = ''


def as_shop(d):
    p = Shop()
    p.__dict__.update(d)
    return p


class GetShopsResponse(object):
    result = False
    shops = Shop()


def as_get_shops_response(d):
    p = GetShopsResponse()
    p.__dict__.update(d)
    return p
