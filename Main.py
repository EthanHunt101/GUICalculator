from tkinter import *
from tkinter import ttk
import sv_ttk

window = Tk("Calculator")
mainframe = ttk.Frame(window, padding = (3,3,12,12))
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))


# Creates the 0 button and adds it to the window
button = ttk.Button(window, width = 5, text = "0")
button.grid(column = 1, row = 5, sticky = (W, E))

# Creates the 1 button and adds it to the window
button = ttk.Button(window, width = 5, text = "1")
button.grid(column = 2, row = 5, sticky = (W, E))

# Creates the 2 button and adds it to the window
button = ttk.Button(window, width = 5, text = "2")
button.grid(column = 3, row = 5, sticky = (W, E))

# Creates the 3 button and adds it to the window
button = ttk.Button(window, width = 5, text = "3")
button.grid(column = 1, row = 4, sticky = (W, E))

# Creates the 4 button and adds it to the window
button = ttk.Button(window, width = 5, text = "4")
button.grid(column = 2, row = 4, sticky = (W, E))

# Creates the 5 button and adds it to the window
button = ttk.Button(window, width = 5, text = "5")
button.grid(column = 3, row = 4, sticky = (W, E))

# Creates the 6 button and adds it to the window
button = ttk.Button(window, width = 5, text = "6")
button.grid(column = 1, row = 3, sticky = (W, E))

# Creates the 7 button and adds it to the window
button = ttk.Button(window, width = 5, text = "7")
button.grid(column = 2, row = 3, sticky = (W, E))

# Creates the 8 button and adds it to the window
button = ttk.Button(window, width = 5, text = "8")
button.grid(column = 3, row = 3, sticky = (W, E))

# Creates the 9 button and adds it to the window
button = ttk.Button(window, width = 5, text = "9")
button.grid(column = 1, row = 2, sticky = (W, E))

# Creates the buttons for the operands
button = ttk.Button(window, width = 5, text = "/")
button.grid(column = 4, row = 2, sticky = (W, E))

button = ttk.Button(window, width = 5, text = "x")
button.grid(column = 4, row = 3, sticky = (W, E))

button = ttk.Button(window, width = 5, text = "-")
button.grid(column = 4, row = 4, sticky = (W, E))

button = ttk.Button(window, width = 5, text = "+")
button.grid(column = 4, row = 5, sticky = (W, E))

# Creates the clear and equals buttons
button = ttk.Button(window, width = 5, text = "AC")
button.grid(column = 2, row = 2, sticky = (W, E))

button = ttk.Button(window, width = 5, text = "=")
button.grid(column = 3, row = 2, sticky = (W, E))
# This is where the magic happens
sv_ttk.set_theme("dark")

window.mainloop()


