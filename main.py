from tkinter import *
from random import randint

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

plot = Plot()
root = Tk()
root.title('SunScreen by HanzeTech')

canvas = Canvas(root, width=1200, height=600, bg='white')  # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)

Button(root, text='Quit', command=root.quit).pack()
Button(root, text='Pause', command=plot.pause).pack()

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
max_label = Label(canvas, text="Max value: ", fg="black", bg="white")
max_label.pack()
canvas.create_window(600, 580, window=max_label)
maximum = Entry(canvas, width=20)
maximum.insert(0, '100')
min_label = Label(canvas, text="Min value: ", fg="black", bg="white")
min_label.pack()
canvas.create_window(800, 580, window=min_label)
minimum = Entry(root, width=20)
minimum.insert(0,'0')
setButton = Button(root, text="Set", command=lambda : plot.setEntry(int(minimum.get()), int(maximum.get())))
minimum.pack()
canvas.create_window(900, 580, window=minimum)
maximum.pack()
canvas.create_window(700, 580, window=maximum)
setButton.pack()
canvas.create_window(1000, 580, window=setButton)
canvas.after(300, plot.step, canvas)
root.mainloop()
print('pushh2')