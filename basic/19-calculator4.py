# !/usr/bin/env python
__author__ = 'dlohani'

from tkinter import *

root = Tk()

currentEquation = ""

equation = StringVar()

calculation = Label(root, textvariable = equation)

equation.set("0")
calculation.grid(columnspan = 4)

def btnPress(num):
    global currentEquation
    currentEquation += str(num)
    equation.set(currentEquation)

def btnEqual():
    global currentEquation
    currentEquation = str(eval(currentEquation))
    equation.set(currentEquation)

def btnClear():
    global currentEquation
    currentEquation = "0"
    equation.set(currentEquation)

button0 = Button(root, text = "0", command = lambda: btnPress(0))
button0.grid(row = 4, column = 1)
button1 = Button(root, text = "1", command = lambda: btnPress(1))
button1.grid(row = 1, column = 0)
button2 = Button(root, text = "2", command = lambda: btnPress(2))
button2.grid(row = 1, column = 1)
button3 = Button(root, text = "3", command = lambda: btnPress(3))
button3.grid(row = 1, column = 2)
button4 = Button(root, text = "4", command = lambda: btnPress(4))
button4.grid(row = 2, column = 0)
button5 = Button(root, text = "5", command = lambda: btnPress(5))
button5.grid(row = 2, column = 1)
button6 = Button(root, text = "6", command = lambda: btnPress(6))
button6.grid(row = 2, column = 2)
button7 = Button(root, text = "7", command = lambda: btnPress(7))
button7.grid(row = 3, column = 0)
button8 = Button(root, text = "8", command = lambda: btnPress(8))
button8.grid(row = 3, column = 1)
button9 = Button(root, text = "9", command = lambda: btnPress(9))
button9.grid(row = 3, column = 2)

button10 = Button(root, text = "+", command = lambda: btnPress("+"))
button10.grid(row = 1, column = 3)
button11 = Button(root, text = "-", command = lambda: btnPress("-"))
button11.grid(row = 2, column = 3)
button12 = Button(root, text = "*", command = lambda: btnPress("*"))
button12.grid(row = 3, column = 3)
button13 = Button(root, text = "/", command = lambda: btnPress("/"))
button13.grid(row = 4, column = 3)

button14 = Button(root, text = "=", command = btnEqual)
button14.grid(row=4,column=2)

buttonClear = Button(root, text = "C", command = btnClear)
buttonClear.grid(row=4, column = 0)

root.mainloop()
