#!/usr/bin/env python
__author__ = 'dlohani'


from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

theButton = Button(topFrame, text="Click Me!", fg = "Blue")
theButton.pack(side=LEFT)

theButton = Button(topFrame, text="Don't Click Me!", fg = "Red")
theButton.pack(side=LEFT)
root.mainloop()
