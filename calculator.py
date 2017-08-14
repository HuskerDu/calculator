from tkinter import *
from tkinter import ttk

equation = ''
def geteqn(s):
    global equation
    try:
        if s=='=':
            answer=eval(equation)
            eqn.set(answer)
            equation=''
        else:
            equation+= s
            eqn.set(equation)
    except:
        eqn.set('Error')
root = Tk()
root.title('Calculator')

window = ttk.Frame(root, padding='10 10 10 10')
window.grid(row=0, column=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

eqn = StringVar()

stuff = ttk.Frame(window)
stuff.grid(row=0, column=0, columnspan=3, sticky=(E))
ttk.Label(stuff, textvariable=eqn).grid(row=0, column=1)

ttk.Button(window, text='7', command=lambda: geteqn('7')).grid(row=1, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='8', command=lambda: geteqn('8')).grid(row=1, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='9', command=lambda: geteqn('9')).grid(row=1, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='4', command=lambda: geteqn('4')).grid(row=2, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='5', command=lambda: geteqn('5')).grid(row=2, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='6', command=lambda: geteqn('6')).grid(row=2, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='1', command=lambda: geteqn('1')).grid(row=3, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='2', command=lambda: geteqn('2')).grid(row=3, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='3', command=lambda: geteqn('3')).grid(row=3, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='0', command=lambda: geteqn('0')).grid(row=4, column=0, sticky=(N, W, E, S))
ttk.Button(window, text='.', command=lambda: geteqn('.')).grid(row=4, column=1, sticky=(N, W, E, S))
ttk.Button(window, text='=', command=lambda: geteqn('=')).grid(row=4, column=2, sticky=(N, W, E, S))
ttk.Button(window, text='/', command=lambda: geteqn('/')).grid(row=1, column=3, sticky=(N, W, E, S))
ttk.Button(window, text='*', command=lambda: geteqn('*')).grid(row=2, column=3, sticky=(N, W, E, S))
ttk.Button(window, text='-', command=lambda: geteqn('-')).grid(row=3, column=3, sticky=(N, W, E, S))
ttk.Button(window, text='+', command=lambda: geteqn('+')).grid(row=4, column=3, sticky=(N, W, E, S))

root.bind('7', lambda x: geteqn('7'))
root.bind('8', lambda x: geteqn('8'))
root.bind('9', lambda x: geteqn('9'))
root.bind('4', lambda x: geteqn('4'))
root.bind('5', lambda x: geteqn('5'))
root.bind('6', lambda x: geteqn('6'))
root.bind('1', lambda x: geteqn('1'))
root.bind('2', lambda x: geteqn('2'))
root.bind('3', lambda x: geteqn('3'))
root.bind('.', lambda x: geteqn('.'))
root.bind('/', lambda x: geteqn('/'))
root.bind('*', lambda x: geteqn('*'))
root.bind('-', lambda x: geteqn('-'))
root.bind('+', lambda x: geteqn('+'))
root.bind('=', lambda x: geteqn('='))
root.bind('<Return>', lambda x: geteqn('='))


root.mainloop()
