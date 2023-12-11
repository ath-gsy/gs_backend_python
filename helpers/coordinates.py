import math


def longitude_to_index(longitude):
    if longitude < -180.0 or longitude > 179.5:
        raise ValueError("longitude is out of range")
    return math.floor((longitude + 180) * 2)


def latitude_to_index(latitude):
    if latitude < -60.0 or latitude > 70.0:
        raise ValueError("longitude is out of range")
    return math.floor((-latitude + 70) * 2)
