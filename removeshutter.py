import shutter
import network
from string import *
from tkinter import *
from ctypes import windll

root = Tk()
n = network.network()

def removeShutter():
    shutter = Tk()
    shutter.geometry("500x300")
    shutter_name = Label(shutter, text="shutter name")
    shutter_com = Label(shutter, text="enter the number of the COM port")
    shutter_name_entry = Entry(shutter)
    shutter_com_entry = Entry(shutter)
    shutter_name.pack()
    shutter_name_entry.pack()
    shutter_com.pack()
    shutter_com_entry.pack()
    Button(shutter, text="remove shutter",
           command=lambda: removeShutterProces(shutter, shutter_name_entry.get(),
                                      shutter_com_entry.get())).pack()


def removeShutterProces(window, rname, rcom):
    for char in rname:
        if char not in ascii_letters:
            return windll.user32.MessageBoxW(0, "Please only use letters in the name", "Invalid name", 0)
    for char in rcom:
        if char in ascii_letters or char in whitespace or int(rcom) < 0:
            return windll.user32.MessageBoxW(0, "Please enter a valid number in COM", "Invalid COM", 0)
    if rcom == "" and rname == "":
        return windll.user32.MessageBoxW(0, "Please enter a COM or name", "COM and name field is empty", 0)
    if rcom != "" and rname != "":
        return windll.user32.MessageBoxW(0, "Please only fill in one of the fields", "COM and name field are both filled in", 0)
    if rname not in n.get_shutter_name_list() and rcom == "":
        return windll.user32.MessageBoxW(0, "This shutter doesn't exist please check again and resubmit", "This shutter doesn't exist",0)
    if int(rcom) not in n.get_shutter_com_list() and rname == "":
        print(n.get_shutter_com_list())
        return windll.user32.MessageBoxW(0, "This shutter doesn't exist please check again and resubmit", "This shutter doesn't exist",0)
    else:
        for shut in n.get_shutter_list():
            if rname == shut.get_name():
                n.remove_shutter(shut)
            if int(rcom) == shut.get_com():
                n.remove_shutter(shut)
        window.destroy()
        n.printlist()


settings = Button(root, text="Settings...", command=lambda: removeShutter())
settings.place(x=1225, y=400)

# test remove function
# n.add_shutter(shutter.shutter('a', 'b', 5))
# n.add_shutter(shutter.shutter('c', 'b', 6))
# n.add_shutter(shutter.shutter('g', 'b', 7))
root.mainloop()

