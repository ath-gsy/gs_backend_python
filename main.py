import xarray as xr

from api.app import app
from helpers.coordinates import latitude_to_index, longitude_to_index

waves_ds = xr.open_dataset("data/waves_2019-01-01.nc")

# Task 1
hmax_value = (
    waves_ds["hmax"]
    .isel(longitude=longitude_to_index(0), latitude=latitude_to_index(0), time=0)
    .values
)
print(hmax_value)  # 2.0808783


# Task 2
if __name__ == '__main__':
    app.run(host='0.0.0.0')


