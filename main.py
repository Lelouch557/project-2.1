from string import *
from tkinter import *
from random import randint
from tkinter.ttk import Notebook
from ctypes import *
from serial import *

class Plot:

    def __init__(self, color):
        self.s = 1
        self.max = 100
        self.min = 0
        self.x2 = 50
        self.y2 = 550 - 5*randint(self.min, self.max)
        self.set = True
        self.color = color

    def step(self, canvas):
        pass

    def reset_plot(self, canvas):
        pass

class TemperaturePlot(Plot):

    def __init__(self, color):
        super().__init__(color)

    def step(self, canvas):
        if self.set:
            if self.s == 23:
                self.reset_plot(canvas)
            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s * 50
            self.y2 = 550-5*randint(self.min, self.max)
            canvas.create_line(x1, y1, self.x2, self.y2, fill=self.color, tags='temp1')
            self.s += 1
        else:
            self.reset_plot(canvas)
        canvas.after(300, self.step, canvas)

    def reset_plot(self, canvas):
        self.s = 1
        self.x2 = 50
        canvas.delete('temp1')

class BrightnessPlot(Plot):

    def __init__(self, color):
        super().__init__(color)

    def step(self, canvas):
        if self.set:
            if self.s == 23:
                self.reset_plot(canvas)
            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s * 50
            self.y2 = 550-5*randint(self.min, self.max)
            canvas.create_line(x1, y1, self.x2, self.y2, fill=self.color, tags='temp2')
            self.s += 1
        else:
            self.reset_plot(canvas)
        canvas.after(300, self.step, canvas)

    def reset_plot(self, canvas):
        self.s = 1
        self.x2 = 50
        canvas.delete('temp2')

max_length = 150
programmed_length = 150

def open_settings():
    settings = Tk()
    settings.geometry("300x100")
    max_label = Label(settings, text="Max length of sunshade:", fg="black", bg="white")
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

def show_plot(plot1, plot2):
    temp_plot.set = plot1
    bright_plot.set = plot2


temp_plot = TemperaturePlot('blue')
bright_plot = BrightnessPlot('red')
show_plot(True, False)
root = Tk()
root.geometry("1200x700")
root.title('SunShade by HanzeTech')

tab_master = Notebook(root)
general_tab = Frame(tab_master)
tab_master.add(general_tab, text="General")
canvas = Canvas(general_tab, width=1600, height=600, bg='white')  # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)
settings = Button(canvas, text="Settings...", command=open_settings)
settings.place(x=800, y=600)

canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
canvas.create_line(50, 550, 50, 50, width=2)  # y-axis

temp_button = Button(canvas, text="Show Temperature", command=lambda: show_plot(True, False)).place(x=400, y=600)
bright_button = Button(canvas, text="Show Brightness", command=lambda: show_plot(False, True)).place(x=600, y=600)
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
canvas.after(300, temp_plot.step, canvas)
canvas.after(300, bright_plot.step, canvas)
tab_master.pack(expand=1, fill="both")
print("commit") # pls remove this
root.mainloop()
