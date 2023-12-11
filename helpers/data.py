import numpy as np
import pandas as pd
import xarray as xr

from helpers.coordinates import longitude_to_index, latitude_to_index


def init_waves_data():
    waves_ds = xr.open_dataset("data/waves_2019-01-01.nc")  # valid when called from main.py
    return waves_ds["hmax"].isel(time=0)


def get_hmax_from_coordinates(waves_data, long, lat):
    return waves_data.isel(
        longitude=longitude_to_index(long), latitude=latitude_to_index(lat)
    ).values
