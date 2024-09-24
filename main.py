from tkinter import *
import tkintermapview as tkm

window = Tk()
window.title('TheMonuments of Domodedovo')
window.geometry('1280x720')
map_widget = tkm.TkinterMapView(window, width=1280, height=720, corner_radius=0)
map_widget.place(x=0, y=0)
map_widget.set_position(55.4407981, 37.7516731)
map_widget.set_zoom(14)




window.mainloop()