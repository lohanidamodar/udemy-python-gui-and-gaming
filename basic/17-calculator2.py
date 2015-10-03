# !/usr/bin/env python
__author__ = 'dlohani'

from tkinter import *

root = Tk()

currentEquation = ""

equation = StringVar()

calculation = Label(root, textvariable = equation)

equation.set("23 + 54")
calculation.grid(columnspan = 4)

def btnPress(num):
    global currentEquation
    currentEquation += str(num)
    equation.set(currentEquation)

button0 = Button(root, text = "0", command = lambda: btnPress(0))
button0.grid(row = 4, column = 2)
button1 = Button(root, text = "1", command = lambda: btnPress(1))
button1.grid(row = 1, column = 1)
button2 = Button(root, text = "2", command = lambda: btnPress(2))
button2.grid(row = 1, column = 2)

root.geometry("800x600")
root.mainloop()
