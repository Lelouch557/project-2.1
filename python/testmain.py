from time import sleep
from tkinter.ttk import Notebook
from random import randint
from string import *
from tkinter import *
from ctypes import windll
import network, shutter
from serial import *

from network import network

slave_state = True;
class Plot:

    def __init__(self, tag):
        self.tempd = []
        self.gem_temp = []
        self.lightd = []
        self.gem_light = []
        self.s = 0
        self.max = 100
        self.min = 0
        self.x2 = 50
        self.y2 = 550 - 5*90
        self.set = True
        self.tl = True # termperature of brightness. True == temperature
        self.color = 'red'
        self.tag = tag
        self.n = network()
        self.activeTab = 0

    def reset_plot(self, canvas):
        self.s = 0
        self.x2 = 50
        canvas.delete(self.tag)

    def itterate_shutters(self):
        temp = self.n.get_shutter_list()
        for i in range(len(temp)):
            temp[i].step()

    def main(self, canvas):
        sleep(0.1)
        self.itterate_shutters()
        self.temp()
        #self.calc_gem_temp()
        self.bright()
        self.reset_plot(canvas)
        if self.tl:
            for i in range(len(self.tempd) - 1 ):
                if i < 23:
                    self.graph(self.tempd)
        else:
            for i in range(len(self.lightd) - 1 ):
                if i < 23:
                    self.graph(self.lightd)
        self.s=0

        canvas.after(300, self.main, canvas)

    def calc_gem_temp(self):
        temp = []
        list = self.n.get_shutter_list()
        for i, n in enumerate(list):
            print(i)
            if(i==0):
                temp = n.get_temp_array()
            else:
                for l in range(len(n.get_temp_array())):
                    temp[(len(temp) - l - 1)] = temp[(len(temp) - l - 1)] + n.get_temp_array()[(len(n.get_temp_array )- l - 1)]

        for i, val in enumerate(temp):
            temp[i] = temp[i] / len(list)
        self.gem_temp = temp
        print(self.gem_temp)

    def temp(self):
        temp = self.n.get_shutter_list()
        if self.activeTab == 0:
            self.tempd = self.gem_temp
        else:
            self.tempd = temp[self.activeTab-1].get_temp_array()

    def bright(self):
        temp = self.n.get_shutter_list()
        if self.activeTab == 0:
            if(len(temp) > 0):
                self.lightd = temp[0].get_light_array()
        else:
            self.lightd = temp[self.activeTab-1].get_light_array()

    def change_graph_source(self, num):
        self.activeTab=num

    def change_slave_state(self):
        if(self.slave):
            self.slave = False
        else:
            self.slave = True

    def change_graph_state(self, bool):
        self.tl = bool
        if(self.tl):
            self.color = "red"
        else:
            self.color = "yellow"

    def graph(self, dataset):
        i = 0
        if(len(dataset) < 23):
            i = self.s
        else:
            i = len(dataset) - (23 - self.s)
        x1 = self.x2
        y1 = self.y2
        self.x2 = 50 + self.s* 50
        self.y2 = 550 - 5 * dataset[i]
        canvas.create_line(x1, y1, self.x2, self.y2, fill=self.color, tags=self.tag)
        self.s += 1

    def addShutter(self, window, name, position, com):
        for char in name:
            if char not in ascii_letters:
                return windll.user32.MessageBoxW(0, "Please only use letters in the name", "Invalid name", 0)
        if name == "":
            return windll.user32.MessageBoxW(0, "Please enter a name.", "name field is empty", 0)
        for char in position:
            if char not in ascii_letters and char not in punctuation and char not in whitespace:
                return windll.user32.MessageBoxW(0, "Please Only use letters and punctuation marks  for the position",
                                                 "Invalid position", 0)
        if position == "":
            return windll.user32.MessageBoxW(0, "Please enter a position.", "position field is empty", 0)
        for char in com:
            if char in ascii_letters or char in whitespace:
                return windll.user32.MessageBoxW(0, "Please enter a valid number in COM", "Invalid COM", 0)
        if com == "":
            return windll.user32.MessageBoxW(0, "Please enter a number.", "COM field is empty", 0)
        else:
            if int(com) > 0:
                for shut in self.n.get_shutter_list():
                    if name == shut.get_name():
                        return windll.user32.MessageBoxW(0, "This name is already in use please use a diffrent one",
                                                         "Name already in use", 0)
                    if int(com) == shut.get_com():
                        return windll.user32.MessageBoxW(0, "This COM port is already in use please use a diffrent one",
                                                         "COM already in use", 0)
                self.n.add_shutter(shutter.shutter(name, position, int(com)))
                self.n.printlist()
                window.destroy()
                windll.user32.MessageBoxW(0, "shutter " + name + " has been added", "added shutter", 0)
                add_tab()
                self.n.printlist()
            else:
                return windll.user32.MessageBoxW(0, "Please enter a positive number in COM.", "Invalid length", 0)


max_length = 150
programmed_length = 150


def open_settings():
    settings = Tk()
    settings.geometry("300x100")
    max_label = Label(settings, text="Max length of sunshade in centimeters:", fg="black")
    max_label.pack()
    max_length_entry = Entry(settings, width=20)
    max_length_entry.pack()
    print(max_length)
    Button(settings, text="OK", command=lambda:set_length(settings, max_length_entry.get())).pack()

def set_length(window, val):
    global max_length, programmed_length
    for char in val:
        if char in ascii_letters or char in punctuation or char in whitespace:
            return windll.user32.MessageBoxW(0, "Please enter a valid length", "Invalid length", 0)
    if val == "":
        return windll.user32.MessageBoxW(0, "Please enter a length.", "Length field is empty", 0)
    else:
        val = int(val)
        if val <= 0:
            return windll.user32.MessageBoxW(0, "Please enter a positive length.", "Invalid length", 0)
        elif val >= programmed_length:
            return windll.user32.MessageBoxW(0, "The maximum length cannot be set higher than %d." % programmed_length, "Invalid length", 0)
        else:
            max_length = val
            window.destroy()

def change_slave_state(button, temp):
    global slave_state
    temp.change_slave_state(slave_state)
    if(slave_state):
        slave_state = False
        button.config(bg="black", foreground="white", text="Manual")
    else:
        slave_state = True
        button.config(bg="lightgray", foreground="black", text="Automatic")

def change_tab(tabi):
    for i, tab in enumerate(tabs):
        if tabi == tab:
            temp_plot.change_graph_source(i)
            tab.config(bg="black", foreground="white")
        else:
            tab.config(bg="lightgray", foreground="black")

def add_tab():
    txt = "Tab" + str(len(tabs))
    tab1 = Button(canvas, text=txt)
    tab1.config(command=lambda: change_tab(tab1))
    tabs.append(tab1)
    xas = 10 + (50 * (len(tabs)))
    tab1.place(x=xas, y=0)

temp_plot = Plot('temp1')

root = Tk()
root.geometry("1200x800")
root.title('SunShade by HanzeTech')
slave = True


canvas = Canvas(root, width=1200, height=800, bg='white')  # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)
settings = Button(canvas, text="Settings...", command=open_settings)
settings.place(x=800, y=600)

canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
canvas.create_line(50, 550, 50, 50, width=2)  # y-axis

temp_button = Button(canvas, text="Show Temperature", command=lambda: temp_plot.change_graph_state(True)).place(x=400, y=600)
bright_button = Button(canvas, text="Show Brightness", command=lambda: temp_plot.change_graph_state(False)).place(x=600, y=600)
manual_button = Button(canvas, text="Automatic")
manual_button.config(command=lambda: change_slave_state(manual_button,temp_plot))
manual_button.place(x=400, y=650)

general_tab = Button(canvas, text="General")
general_tab.config(bg="black", foreground="white")

general_tab.config(command=lambda: change_tab(general_tab))
general_tab.place(x=50,y=0)
tabs = [general_tab]
# x-axis
for i in range(23):
    x = 50 + (i * 50)
    canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
    canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)
xlabel = Label(canvas, text="Step", fg='black', bg='white')
xlabel.pack()
canvas.create_window(1150, 575, window=xlabel)
# y-axis
for i in range(11):
    y = 550 - (i * 50)
    canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
    canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)
ylabel = Label(canvas, text="Value", fg="black", bg="white")
ylabel.pack()
canvas.create_window(25, 25, window=ylabel)

# add arduino screen

def addShutterSettings():
    shutter = Tk()
    shutter.geometry("500x300")
    shutter.title("Add shutter")
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
           command=lambda: temp_plot.addShutter(shutter, shutter_name_entry.get(), shutter_position_entry.get(),
                                      shutter_com_entry.get())).pack()

add_shut = Button(canvas, text="Add Shutter", command=lambda: addShutterSettings())
add_shut.place(x=825, y=650)


canvas.after(300, temp_plot.main, canvas)

root.mainloop()