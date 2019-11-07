# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
    messagebox.showinfo("Say Hello", "Hello World")

def help():
    messagebox.askquestion("how are you", "dipshit you are")

B1 = Button(top, text = "Say Hello", command = hello)
b2 = Button(top, text = "help", command = help)
B1.place(x = 35,y = 50)
b2.place(x = 100, y = 50)

top.mainloop()