from tkinter import *
import os
import tkintermapview as tkm
import Monument as Mn

def left_clicked():
    pass

window = Tk()
window.title('Достопримечательности Домодедово')
window.geometry('960x600')

script_directory = os.path.dirname(os.path.abspath(__file__))
# with zipfile.ZipFile('offline_tiles.zip') as file:
#     file.extractall()
database_path = os.path.join(script_directory, "offline_tiles.db")


map_widget = tkm.TkinterMapView(window, width=960, height=600, corner_radius=0, use_database_only=True,
                                database_path=str(database_path),
                                max_zoom=20)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)


map_widget.place(x=0, y=0)
map_widget.set_position(55.4407981, 37.7516731)

# map_widget.set_zoom(14)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=19)
Obelisk = Mn.TheMonument(deg_x=55.440687, deg_y=37.766823, name="Обелиск славы", address="", description="")
# adr = tkm.convert_coordinates_to_address(55.440687, 37.766823)
# print(adr.street, adr.housenumber, adr.postal, adr.city, adr.state, adr.country, adr.latlng)
map_widget.set_marker(Obelisk.deg_x, Obelisk.deg_y, Obelisk.name, text_color="white")


window.mainloop()
