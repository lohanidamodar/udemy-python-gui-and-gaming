#!/usr/bin/env python
__author__ = 'dlohani'


from tkinter import *

root = Tk()

theButton = Button(None, text="Click Me!", fg = "Blue")
theButton.pack()

theButton = Button(None, text="Don't Click Me!", fg = "Red")
theButton.pack()
root.mainloop()
