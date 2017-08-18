##############################
# Created by HuskerDu (Pixie)#
##############################

from tkinter import *
from tkinter import ttk
import gui

root = Tk()
root.title('Calculator')  # Setting GUI Title

window = ttk.Frame(root, padding='10 10 10 10')
window.grid(row=0, column=0, sticky=(N, W, E, S))
gui.stu(ttk, window, root)

root.mainloop()
