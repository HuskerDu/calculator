###############################
# Created by HuskerDu (Pixie) #
###############################

from tkinter import *
from tkinter import ttk
import gui

#Creating basic framework for the GUI

root = Tk()
root.title('Calculator')  # Setting GUI Title

window = ttk.Frame(root, padding='10 10 10 10')
window.grid(row=0, column=0, sticky=(N, W, E, S))

gui.graphics(ttk, window, root) #calling graphics function from gui file for the entire Calculator framework

root.mainloop()
