from tkinter import *
import requests
import os
import tkintermapview as tkm
import Monument as Mn

MIN_ZOOM_LEVEL = 16
CLICK_RADIUS = 0.0001
markers = []


def on_marker_hover(event, marker):
    """Change cursor to 'hand2' when hovering over a marker."""
    window.config(cursor="hand2")  # Change cursor to hand2


def on_marker_leave(event):
    """Reset cursor when leaving the marker."""
    window.config(cursor="")  # Reset cursor to default


def main():
    # Example: Make an HTTP request
    response = requests.get("https://api.github.com")
    print("GitHub API Response:", response.json())


if __name__ == "__main__":
    main()



def create_marker(lat, lng, text="Marker"):
    marker = map_widget.set_marker(lat, lng, text=text, text_color="white")
    markers.append(marker)  # Store the marker
    return marker


def enforce_min_zoom():
    # print(map_widget.zoom)
    current_zoom = map_widget.zoom
    if current_zoom < MIN_ZOOM_LEVEL:
        map_widget.set_zoom(MIN_ZOOM_LEVEL)

    window.after(10, enforce_min_zoom)


def on_map_click(coordinates_tuple):
    lat, lng = coordinates_tuple
    # print(lat, lng)

    # Check if the click is within the defined radius of any marker
    for marker in markers:
        marker_lat, marker_lng = marker.position  # Get marker position
        if abs(lat - marker_lat) < CLICK_RADIUS and abs(lng - marker_lng) < CLICK_RADIUS:
            print(f"Marker at {marker.position} clicked!")



window = Tk()
window.title('Достопримечательности Домодедово')
window.geometry('960x600')

script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, "offline_tiles.db")

map_widget = tkm.TkinterMapView(window, width=960, height=600, corner_radius=0,
                                use_database_only=False, database_path=str(database_path),
                                max_zoom=19)
map_widget.pack(fill="both", expand=True)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)
map_widget.set_position(55.4407981, 37.7516731)
map_widget.set_zoom(MIN_ZOOM_LEVEL)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                           max_zoom=19)
map_widget.add_left_click_map_command(on_map_click)
canvas = map_widget.canvas
Obelisk = Mn.TheMonument(deg_x=55.440687, deg_y=37.766823, name="Обелиск славы",
                         address="", description="")
# lensa = Mn.TheMonument(deg_x=55.440300, deg_y=37.766400, name="Обелиск славы",
#                        address="", description="")

create_marker(Obelisk.deg_x, Obelisk.deg_y, Obelisk.name)
# create_marker(lensa.deg_x, lensa.deg_y, lensa.name)

enforce_min_zoom()

window.mainloop()
