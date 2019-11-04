# deze code komt van https://www.python-course.eu/tkinter_entry_widgets.php
import tkinter as tk

list = []


def show_entry_fields():
    list.append(e1.get())
    list.append(e2.get())
    list.append(e3.get())
    print(list)


addShutter = tk.Tk()

tk.Label(addShutter,
         text="First Name").grid(row=0)
tk.Label(addShutter,
         text="Last Name").grid(row=1)
tk.Label(addShutter,
         text="Middel Name").grid(row=2)

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
