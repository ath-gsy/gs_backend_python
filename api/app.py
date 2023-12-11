import math

from flask import Flask, request

from helpers.data import get_hmax_from_coordinates, init_waves_data

app = Flask(__name__)

waves_data = init_waves_data()


@app.route("/")
def main():
    return "Waves data API"


@app.route("/wave_data")
def get_wave_data():
    longitude = request.args.get("long")
    latitude = request.args.get("lat")

    if longitude is None or latitude is None:
        return "ERROR: longitude and latitude needed"

    longitude = float(longitude)
    latitude = float(latitude)

    try:
        wave_height = str(get_hmax_from_coordinates(waves_data, longitude, latitude))
    except ValueError:
        return "ERROR: coordinate value out of range"

    return wave_height
