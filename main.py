from tkinter import *
from random import randint
from tkinter.ttk import Notebook
from ctypes import *
from serial import *

class Plot:

    def __init__(self):
        self.s = 1
        self.max = 100
        self.min = 0
        self.x2 = 50
        self.y2 = 550 - 5*randint(self.min, self.max)
        self.paused = False

    def step(self, canvas):
        if not self.paused:
            if self.s == 23:
                # new frame
                self.s = 1
                self.x2 = 50
                canvas.delete('temp')  # only delete items tagged as temp
            canvas.delete('bounds')
            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s * 50
            self.y2 = 550-5*randint(self.min, self.max)
            canvas.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')
            min_line = canvas.create_line(50, 550, 1150, 550, width=3, fill='red',tags='bounds')
            max_line = canvas.create_line(50, 50, 1150, 50, width=3, fill='red',tags='bounds')
            canvas.coords(max_line, 50, 550 - 5 * self.max, 1150, 550 - 5 * self.max)
            canvas.coords(min_line, 50, 550 - 5 * self.min, 1150, 550 - 5 * self.min)
            self.s += 1
        canvas.after(300, self.step, canvas)


    def setEntry(self, mini, maxi):
        if mini >= 0 and maxi <= 100 and mini <= maxi:
            self.minEntry = mini
            self.maxEntry = maxi
            self.getrange()
        else:
            print("Invalid range")

    def getrange(self):
        self.min = self.minEntry
        self.max = self.maxEntry

    def pause(self):
        if self.paused:
            self.paused = False
        else:
            self.paused = True

max_length = 150
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
    global max_length
    if val == "":
        windll.user32.MessageBoxW(0, "Please enter a length.", "Length field is empty", 0)
    else:
        val = int(val)
        if val > 0:
            max_length = val
            window.destroy()
        else:
            windll.user32.MessageBoxW(0, "Please enter a positive length.", "Invalid length", 0)

plot = Plot()
root = Tk()
root.geometry("1350x700")
root.title('SunShade by HanzeTech')

tab_master = Notebook(root)
general_tab = Frame(tab_master)
tab_master.add(general_tab, text="General")
canvas = Canvas(general_tab, width=1600, height=600, bg='white')  # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)
pause_button = Button(canvas, text='Pause', command=plot.pause)
pause_button.place(x=1237, y=350)
settings = Button(canvas, text="Settings...", command=open_settings)
settings.place(x=1225, y=400)

canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
canvas.create_line(50, 550, 50, 50, width=2)  # y-axis

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
canvas.after(300, plot.step, canvas)
tab_master.pack(expand=1, fill="both")
root.mainloop()