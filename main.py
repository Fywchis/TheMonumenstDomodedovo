import builtins
import os
from tkinter import *
import tkintermapview as tkm
from monument import *
import webbrowser
from osmfix import _build_headers
from geocoder.osm import OsmQuery


MIN_ZOOM_LEVEL = 15
upper_lat = 55.45453725452048
down_lat = 55.40167158988299
west_lng = 37.699313912200495
east_lng = 37.79927875353329


OsmQuery._build_headers = _build_headers


def enforce_min_zoom():
    position_x, position_y = map_widget.get_position()
    current_zoom = map_widget.zoom
    if current_zoom < MIN_ZOOM_LEVEL:
        map_widget.set_zoom(MIN_ZOOM_LEVEL)
        map_widget.set_position(position_x, position_y)
    window.after(250, enforce_min_zoom)


def enforce_position():
    map_pos_lat, map_pos_lng = map_widget.get_position()
    if (map_pos_lat >= upper_lat or map_pos_lat <= down_lat or map_pos_lng >= east_lng
            or map_pos_lng <= west_lng):
        map_widget.set_position(55.4407981, 37.7516731)
    window.after(1000, enforce_position)


def marker_event(marker: tkm.map_widget.CanvasPositionMarker):
    x, y = marker.position
    address = tkm.convert_coordinates_to_address(x, y)
    coords = StringVar()
    coordinates = f"и на координатах {address.latlng}"

    with builtins.open(os.path.join(source_directory, f"{marker.text.lower()}.txt"), 'r', encoding='utf-8') as file:
        contents = file.read()

    info_window = Toplevel(window)
    info_window.title(f"Информация: {marker.text}")

    frame = Frame(info_window)

    Label(frame, text=f"Достопримечательность: {marker.text}").pack(anchor='w')

    Label(frame, text=f"Находится по адресу {address.state} {address.city}"
                      f" {address.street}").pack(anchor='w')
    coords.set(coordinates)
    Entry(frame, textvariable=coords, width=len(coordinates), state="readonly").pack(anchor='w')
    Label(frame, text=contents, justify="left").pack(anchor='w')

    if marker.data is not None:
        Label(frame, text="Больше можно узнать на").pack(side=LEFT)
        url = Label(frame, text="сайте", fg='blue', cursor='hand2')
        url.pack(side=LEFT)
        url.bind('<Button-1>', lambda e: webbrowser.open(marker.data))

    frame.pack(anchor=CENTER)
    info_window.update()

    width = frame.winfo_width() + 20
    height = frame.winfo_height() + 20
    info_window.geometry(f"{width}x{height}")

def marker_creation(marker_set):
    for monument in marker_set:
        if monument.image:
            map_widget.set_marker(monument.deg_x, monument.deg_y, monument.name, text_color="white",
                                  image=monument.image, data=monument.link, command=marker_event)
        else:
            map_widget.set_marker(monument.deg_x, monument.deg_y, monument.name, text_color="white",
                                  data=monument.link, command=marker_event)


window = Tk()
window.title('Достопримечательности Домодедово')
window.geometry('960x600')

monuments = {
    TheMonument(55.440687, 37.766823, "Обелиск славы"),
    TheMonument(55.409595, 37.739189, "Стена скорби"),
    # TheMonument(55.420316, 37.743705, "Курганы вятичей"),
    TheMonument(55.437095, 37.767415, "В.И. Ленин"),
    TheMonument(55.433077, 37.766199, "Богиня победы Ника", "http://zhuravli.uonb.ru/?page_id=1979"),
    TheMonument(55.444081, 37.741007, "аллея 60-летия Победы", "https://new.domod.ru/novosti/domodedovskiy-arkhiv-alleya-60-letiya-pobedy-v-domodedovo/"),
    TheMonument(55.422472, 37.769102, "Виктор Васильевич Талалихин")
}


script_directory = os.getcwd()
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

enforce_min_zoom()
enforce_position()
marker_creation(monuments)

window.mainloop()
