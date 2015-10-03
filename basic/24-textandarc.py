__author__ = 'dlohani'

from tkinter import *

root = Tk()
canvas = Canvas(root,width = 300, height=300)
canvas.pack()

canvas.create_arc(10, 10, 200, 80, extent = 180, style = ARC)
canvas.create_arc(10, 80, 200, 200, extent = 90, style = ARC)

canvas.create_text(120,10, text = "Canvas text is awesome", font = ("Times",15))

root.mainloop()