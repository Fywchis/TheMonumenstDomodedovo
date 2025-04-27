import os
from tkinter import *
import tkintermapview as tkm
from monument import *
import webbrowser


MIN_ZOOM_LEVEL = 16
CLICK_RADIUS = 0.001
markers = []


def enforce_min_zoom():
    position_x, position_y = map_widget.get_position()
    current_zoom = map_widget.zoom
    if current_zoom < MIN_ZOOM_LEVEL:
        map_widget.set_zoom(MIN_ZOOM_LEVEL)
        map_widget.set_position(position_x, position_y)
    window.after(100, enforce_min_zoom)

def enforce_position():
    map_pos_lat, map_pos_lng = map_widget.get_position()
    if (map_pos_lat >= 55.45818700530422 or map_pos_lat <= 55.41466320701811 or map_pos_lng >= 37.78950373603266
            or map_pos_lng <= 37.732855481638126):
        map_widget.set_position(55.4407981, 37.7516731)
    window.after(1000, enforce_position)


# def on_map_click(coordinates_tuple):
#     lat, lng = coordinates_tuple
#
#     for marker in markers:
#         marker_lat, marker_lng = marker.position
#         if abs(lat - marker_lat) < CLICK_RADIUS and abs(lng - marker_lng) < CLICK_RADIUS:
#             print(f"Marker at {marker.position} clicked!")

def marker_event(marker):
    file = open(os.path.join(source_directory, f"{marker.text.lower()}.txt"), os.O_RDONLY)
    contents = read(file, 100)
    info_window = Toplevel(window)
    info_window.title(f"Информация: {marker.text}")
    info_window.geometry("300x200")
    frame = Frame(info_window)
    Label(frame, text=f"Достопримечательность: {marker.text}").pack()
    Label(frame, text=f"Координаты: {marker.position}").pack()
    Label(frame, text=f"{contents}").pack()
    Label(frame, text="Больше можно узнать на").pack(side=LEFT)
    url = Label(frame, text="сайте", fg='blue', cursor='hand2')
    url.pack(side=LEFT, ipadx=0)
    url.bind('<Button-1>', lambda e: webbrowser.open(marker.data))
    frame.pack(anchor=CENTER)


def marker_creation(marker_set):
    for i in marker_set:
        map_widget.set_marker(i.deg_x, i.deg_y, i.name, text_color="white",
                              image=i.image, data=i.link, command=marker_event)


window = Tk()
window.title('Достопримечательности Домодедово')
window.geometry('960x600')

monuments = {
    TheMonument(deg_x=55.440687, deg_y=37.766823, name="Обелиск славы", link="google.com"),

}

script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, "offline_tiles.db")
source_directory = os.path.join(script_directory, "info_img")


map_widget = tkm.TkinterMapView(window, width=960, height=600, corner_radius=0,
                                database_path=str(database_path), use_database_only=True,
                                max_zoom=19)

map_widget.pack(fill="both", expand=True)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)
map_widget.set_position(55.4407981, 37.7516731)
map_widget.set_zoom(MIN_ZOOM_LEVEL)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=19)

# map_widget.add_left_click_map_command(on_map_click)


# Obelisk = TheMonument(deg_x=55.440687, deg_y=37.766823, name="Обелиск славы", info="В честь войны")
# Obelisk = TheMonument(deg_x=55.440687, deg_y=37.766823, name="Обелиск славы", info="В честь войны")
# create_marker(Obelisk.deg_x, Obelisk.deg_y, Obelisk.name)
# marker_1 = map_widget.set_marker(Obelisk.deg_x, Obelisk.deg_y, Obelisk.name, text_color="white",
#                                  image=Obelisk.image, data=Obelisk.info, command=marker_event)

enforce_min_zoom()
enforce_position()
marker_creation(monuments)

window.mainloop()
