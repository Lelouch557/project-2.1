# deze code komt van https://www.python-course.eu/tkinter_entry_widgets.php
#deze code wordt niet gebruikt
import tkinter as tk
from ctypes import windll

list = []

def show_entry_fields():
    if e1 == type(str):
        if e2 == type(str):
            if e3 == type(int):
                list.append(e1.get())
                list.append(e2.get())
                list.append(e3.get())
                print(list)
            else: windll.user32.MessageBoxW(0, "COM can oly contain a number", 0)
        else: windll.user32.MessageBoxW(0, "position of the shuttor can only contain letters", 0)
    else: windll.user32.MessageBoxW(0, "name can only contain letters", 0)



addShutter = tk.Tk()

tk.Label(addShutter,
         text="add name shutter").grid(row=0)
tk.Label(addShutter,
         text="add position shutter").grid(row=1)
tk.Label(addShutter,
         text="Fill in the COM number \n for example: 5").grid(row=2)

e1 = tk.Entry(addShutter)
e2 = tk.Entry(addShutter)
e3 = tk.Entry(addShutter)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(addShutter,
          text='Cancel',
          command=addShutter.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(addShutter,
          text='Add shutter', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.mainloop()
