import zipfile
from tkinter import *

import os
import tkintermapview as tkm

window = Tk()
window.title('TheMonuments of Domodedovo')
window.geometry('960x600')

script_directory = os.path.dirname(os.path.abspath(__file__))
with zipfile.ZipFile('offline_tiles.zip') as file:
    file.extractall()
database_path = os.path.join(script_directory, "offline_tiles.db")


map_widget = tkm.TkinterMapView(window, width=960, height=600, corner_radius=0, use_database_only=True,
                                database_path=str(database_path), max_zoom=20)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)


map_widget.place(x=0, y=0)
map_widget.set_position(55.4407981, 37.7516731)

map_widget.set_zoom(14)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=19)


window.mainloop()
