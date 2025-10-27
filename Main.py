from tkinter import *
from tkinter import ttk
import sv_ttk

# All functions I create will be added up here







window = Tk("Calculator")
mainframe = ttk.Frame(window, padding = (3,3,12,12))
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

# Creates the label where the calculations will be outputted
calc_label = ttk.Label(window, text="Placeholder", padding = (15,15,15,15))
calc_label.grid(column = 1, columnspan = 4, row =1, sticky = (E))

# Creates the 0 button and adds it to the window
button0 = ttk.Button(window, width = 5, text = "0")
button0.grid(column = 1, row = 5, sticky = (W, E))

# Creates the 1 button and adds it to the window
button1 = ttk.Button(window, width = 5, text = "1")
button1.grid(column = 2, row = 5, sticky = (W, E))

# Creates the 2 button and adds it to the window
button2 = ttk.Button(window, width = 5, text = "2")
button2.grid(column = 3, row = 5, sticky = (W, E))

# Creates the 3 button and adds it to the window
button3 = ttk.Button(window, width = 5, text = "3")
button3.grid(column = 1, row = 4, sticky = (W, E))

# Creates the 4 button and adds it to the window
button4 = ttk.Button(window, width = 5, text = "4")
button4.grid(column = 2, row = 4, sticky = (W, E))

# Creates the 5 button and adds it to the window
button5 = ttk.Button(window, width = 5, text = "5")
button5.grid(column = 3, row = 4, sticky = (W, E))

# Creates the 6 button and adds it to the window
button6 = ttk.Button(window, width = 5, text = "6")
button6.grid(column = 1, row = 3, sticky = (W, E))

# Creates the 7 button and adds it to the window
button7 = ttk.Button(window, width = 5, text = "7")
button7.grid(column = 2, row = 3, sticky = (W, E))

# Creates the 8 button and adds it to the window
button8 = ttk.Button(window, width = 5, text = "8")
button8.grid(column = 3, row = 3, sticky = (W, E))

# Creates the 9 button and adds it to the window
button9 = ttk.Button(window, width = 5, text = "9")
button9.grid(column = 1, row = 2, sticky = (W, E))

# Creates the buttons for the operands
button_div = ttk.Button(window, width = 5, text = "/")
button_div.grid(column = 4, row = 2, sticky = (W, E))

button_mul = ttk.Button(window, width = 5, text = "x")
button_mul.grid(column = 4, row = 3, sticky = (W, E))

button_sub = ttk.Button(window, width = 5, text = "-")
button_sub.grid(column = 4, row = 4, sticky = (W, E))

button_add = ttk.Button(window, width = 5, text = "+")
button_add.grid(column = 4, row = 5, sticky = (W, E))

# Creates the clear and equals buttons
button_clear = ttk.Button(window, width = 5, text = "AC")
button_clear.grid(column = 2, row = 2, sticky = (W, E))

button_equal = ttk.Button(window, width = 5, text = "=")
button_equal.grid(column = 3, row = 2, sticky = (W, E))
# This is where the magic happens
sv_ttk.set_theme("dark")

window.mainloop()


