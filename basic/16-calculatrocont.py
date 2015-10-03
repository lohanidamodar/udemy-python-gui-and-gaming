# !/usr/bin/env python
__author__ = 'dlohani'

from tkinter import *

root = Tk()

equation = StringVar()

calculation = Label(root, textvariable = equation)

equation.set("23 + 54")
calculation.grid(columnspan = 4)

root.geometry("800x600")
root.mainloop()
