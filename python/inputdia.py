import tkinter as tk
from tkinter import simpledialog

#this code is not in use
ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Name",
                                  prompt="What's your Name?:")
USER_INP2 = simpledialog.askstring(title="Age",
                                  prompt="your age")

# check it out
print("Hello", USER_INP, "you are", USER_INP2, "years old")