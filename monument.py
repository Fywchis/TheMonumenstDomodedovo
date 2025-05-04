from os import *
from PIL import Image, ImageTk

script_directory = path.dirname(path.abspath(__file__))
source_directory = path.join(script_directory, "info_img")


class TheMonument:
    def __init__(self, deg_x, deg_y, name, link):
        self.deg_x = deg_x
        self.deg_y = deg_y
        self.name = name

        if link:
            self.link = link
        else:
            self.link = None
        try:
            self.image_path = path.join(source_directory, f"{name.lower()}.jpg")
            self.image = ImageTk.PhotoImage(Image.open(path.join(self.image_path)).resize((200, 100)))
        except FileNotFoundError:
            self.image = None

