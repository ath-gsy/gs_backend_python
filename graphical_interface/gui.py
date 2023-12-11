import tkinter
from tkinter import *

from PIL import Image, ImageTk

from graphical_interface.helpers import create_grid

### temp ####
longitude_dim = 720
latitude_dim = 261
#############

side_panel_size = 400
map_length = 3813  # 1335
map_height = 1646  # 575


root = Tk()
root.geometry(f"{1335 + side_panel_size}x{575}")
root.title("Max wave height visualisation")

# Background map

canvas = Canvas(root, width=map_length, height=map_height)
canvas.pack(anchor=NW)

image1 = Image.open("../assets/world_map.jpg")
world_map = ImageTk.PhotoImage(image1)

canvas.create_image((map_length / 2, map_height / 2), image=world_map)


def do_zoom(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    factor = 1.001**event.delta
    canvas.scale(ALL, x, y, factor, factor)


canvas.bind("<MouseWheel>", do_zoom)
canvas.bind("<ButtonPress-1>", lambda event: canvas.scan_mark(event.x, event.y))
canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))


create_grid(canvas, map_length, map_height, longitude_dim, latitude_dim)


root.mainloop()
