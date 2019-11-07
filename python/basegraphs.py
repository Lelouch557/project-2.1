from tkinter import *
from random import randint
import time
from tkinter import simpledialog


class Plot:
    def __init__(self):
        self.s = 1
        self.x2 = 50
        self.y2 = self.value_to_y(randint(0, 100))
        self.root = Tk()
        self.root.title('simple plot')
        self.canvas = Canvas(self.root, width=1200, height=600, bg='white')  # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)
        Button(self.root, text='Quit', command=self.root.quit).pack()
        Button(self.root, text='Pause', command=self.pause).pack()

        self.frame = Frame(self.root).pack()
        Label(self.frame, text="Min").pack(side=LEFT)
        self.minEntryVal = StringVar()
        self.minEntry = Entry(self.frame, textvariable=self.minEntryVal).pack(side=LEFT)
        Label(self.frame, text="Max").pack(side=LEFT)
        self.maxEntryVal = StringVar()
        self.maxEntry = Entry(self.frame, textvariable=self.maxEntryVal).pack(side=LEFT)
        Button(self.frame, text='Set', command=self.set).pack(side=LEFT)

        self.min = 0
        self.max = 100

        self.canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
        self.canvas.create_line(50, 550, 50, 50, width=2)  # y-axis

        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            self.canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)
        self.canvas.create_text(600, 570, text='Step', anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)
        self.canvas.create_text(20, 315, text='Value', anchor=N)

        self.paused = False
        self.canvas.after(300, self.step, self.canvas)
        self.root.mainloop()

    def step(self, canvas):
        if not self.paused:
            if self.s == 23:
                # new frame
                self.s = 1
                self.x2 = 50
                canvas.delete('temp')  # only delete items tagged as temp
            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s * 50
            self.y2 = self.value_to_y(randint(self.min, self.max))
            canvas.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')
            # print(s, x1, y1, x2, y2)
            self.s = self.s + 1
        canvas.after(300, self.step, canvas)

    def pause(self):
        self.paused = not self.paused

    def value_to_y(self, val):
        return 550 - 5 * val

    def set(self):
        self.min = int(self.minEntryVal.get())
        self.max = int(self.maxEntryVal.get())

        yMin = 550 - self.min * 5
        yMax = 550 - self.max * 5
        self.canvas.create_line(50, yMin, 1150, yMin, width=2, fill="red")  # x-axis
        self.canvas.create_line(50, yMax, 1150, yMax, width=2, fill="red")  # y-axis

if __name__ == '__main__':
    plot = Plot()
    print("second push")

