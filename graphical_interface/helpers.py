def create_grid(canvas, map_length, map_height, longitude_dim, latitude_dim):
    div_length = map_length / longitude_dim
    div_height = map_height / latitude_dim

    for long in range(longitude_dim):
        for lat in range(latitude_dim):
            a = long * div_length
            b = lat * div_height
            c = long * div_length + div_length
            d = lat * div_height + div_height
            canvas.create_rectangle(a, b, c, d, fill="")
