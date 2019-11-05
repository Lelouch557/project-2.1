import shutter
import network
from string import *
from tkinter import *
from ctypes import windll

root = Tk()
n = network.network()

def addShutterSettings():
    shutter = Tk()
    shutter.geometry("500x300")
    shutter_name = Label(shutter, text="shutter name")
    shutter_position = Label(shutter, text="description of the shutter position")
    shutter_com = Label(shutter, text="enter the number of the COM port")
    shutter_name_entry = Entry(shutter)
    shutter_position_entry = Entry(shutter)
    shutter_com_entry = Entry(shutter)
    shutter_name.pack()
    shutter_name_entry.pack()
    shutter_position.pack()
    shutter_position_entry.pack()
    shutter_com.pack()
    shutter_com_entry.pack()
    Button(shutter, text="add shutter",
           command=lambda: addShutter(shutter, shutter_name_entry.get(), shutter_position_entry.get(),
                                      shutter_com_entry.get())).pack()


def addShutter(window, name, position, com):
    for char in name:
        if char not in ascii_letters:
            return windll.user32.MessageBoxW(0, "Please only use letters in the name", "Invalid name", 0)
    if name == "":
        return windll.user32.MessageBoxW(0, "Please enter a name.", "name field is empty", 0)
    for char in position:
        if char not in ascii_letters and char not in punctuation:
            return windll.user32.MessageBoxW(0, "Please Only use letters and punctuation marks  for the position",
                                             "Invalid position", 0)
    if position == "":
        return windll.user32.MessageBoxW(0, "Please enter a position.", "position field is empty", 0)
    for char in com:
        if char in ascii_letters:
            return windll.user32.MessageBoxW(0, "Please enter a valid number in COM", "Invalid COM", 0)
    if com == "":
        return windll.user32.MessageBoxW(0, "Please enter a number.", "COM field is empty", 0)
    else:
        if int(com) > 0:
            for shutter in n.get_shutter_list():
                if name == shutter.get_name():
                    n.remove_shutter(shutter.get_name())
                if com == shutter.get_com():
                    return windll.user32.MessageBoxW(0, "This COM port is already in use please use a diffrent one", "COM field already in use", 0)
            n.add_shutter(shutter.shutter(name, position, com))
            n.printlist()
            window.destroy()
        else:
            return windll.user32.MessageBoxW(0, "Please enter a positive number in COM.", "Invalid length", 0)


settings = Button(root, text="Settings...", command=lambda: addShutterSettings())
settings.place(x=1225, y=400)
root.mainloop()
