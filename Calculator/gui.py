import display
from tkinter import *

def stu(ttk, window, root):

    eqn = StringVar()
    
    stuff = ttk.Frame(window)
    stuff.grid(row=0, column=0, columnspan=3, sticky=E)
    ttk.Label(stuff, textvariable=eqn).grid(row=0, column=1)

    ttk.Button(window, text='7', command=lambda: display.get_eqn('7', eqn)).grid(row=1, column=0, sticky=(N, W, E, S))
    ttk.Button(window, text='8', command=lambda: display.get_eqn('8', eqn)).grid(row=1, column=1, sticky=(N, W, E, S))
    ttk.Button(window, text='9', command=lambda: display.get_eqn('9', eqn)).grid(row=1, column=2, sticky=(N, W, E, S))
    ttk.Button(window, text='4', command=lambda: display.get_eqn('4', eqn)).grid(row=2, column=0, sticky=(N, W, E, S))
    ttk.Button(window, text='5', command=lambda: display.get_eqn('5', eqn)).grid(row=2, column=1, sticky=(N, W, E, S))
    ttk.Button(window, text='6', command=lambda: display.get_eqn('6', eqn)).grid(row=2, column=2, sticky=(N, W, E, S))
    ttk.Button(window, text='1', command=lambda: display.get_eqn('1', eqn)).grid(row=3, column=0, sticky=(N, W, E, S))
    ttk.Button(window, text='2', command=lambda: display.get_eqn('2', eqn)).grid(row=3, column=1, sticky=(N, W, E, S))
    ttk.Button(window, text='3', command=lambda: display.get_eqn('3', eqn)).grid(row=3, column=2, sticky=(N, W, E, S))
    ttk.Button(window, text='0', command=lambda: display.get_eqn('0', eqn)).grid(row=4, column=0, sticky=(N, W, E, S))
    ttk.Button(window, text='.', command=lambda: display.get_eqn('.', eqn)).grid(row=4, column=1, sticky=(N, W, E, S))
    ttk.Button(window, text='=', command=lambda: display.get_eqn('=', eqn)).grid(row=4, column=2, sticky=(N, W, E, S))
    ttk.Button(window, text='/', command=lambda: display.get_eqn('/', eqn)).grid(row=1, column=3, sticky=(N, W, E, S))
    ttk.Button(window, text='*', command=lambda: display.get_eqn('*', eqn)).grid(row=2, column=3, sticky=(N, W, E, S))
    ttk.Button(window, text='-', command=lambda: display.get_eqn('-', eqn)).grid(row=3, column=3, sticky=(N, W, E, S))
    ttk.Button(window, text='+', command=lambda: display.get_eqn('+', eqn)).grid(row=4, column=3, sticky=(N, W, E, S))
    ttk.Button(window, text='Del', command=lambda: display.get_eqn('Del', eqn)).grid(row=1, column=4, sticky=(N, W, E, S))
    
    
    stuff.rowconfigure(0, weight=1)
    stuff.columnconfigure(0, weight=1)
    for i in range(5):
        window.rowconfigure(i, weight=1, pad='80')  # newlines
        root.rowconfigure(i, weight=1, pad='80')
    for i in range(5):
        window.columnconfigure(i, weight=1, pad='80')
        root.columnconfigure(i, weight=1, pad='80')

   
    root.bind('7', lambda x: display.get_eqn('7', eqn))
    root.bind('8', lambda x: display.get_eqn('8', eqn))
    root.bind('9', lambda x: display.get_eqn('9', eqn))
    root.bind('4', lambda x: display.get_eqn('4', eqn))
    root.bind('5', lambda x: display.get_eqn('5', eqn))
    root.bind('6', lambda x: display.get_eqn('6', eqn))
    root.bind('1', lambda x: display.get_eqn('1', eqn))
    root.bind('2', lambda x: display.get_eqn('2', eqn))
    root.bind('3', lambda x: display.get_eqn('3', eqn))
    root.bind('0', lambda x: display.get_eqn('0', eqn))
    root.bind('.', lambda x: display.get_eqn('.', eqn))
    root.bind('/', lambda x: display.get_eqn('/', eqn))
    root.bind('*', lambda x: display.get_eqn('*', eqn))
    root.bind('-', lambda x: display.get_eqn('-', eqn))
    root.bind('+', lambda x: display.get_eqn('+', eqn))
    root.bind('=', lambda x: display.get_eqn('=', eqn))
    root.bind('<Return>', lambda x: display.get_eqn('=', eqn))
    root.bind('<BackSpace>', lambda x: display.get_eqn('Del', eqn))
