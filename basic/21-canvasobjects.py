__author__ = 'dlohani'

from tkinter import *

root = Tk()
canvas = Canvas(root,width = 300, height=300)
canvas.pack()

rectangle = canvas.create_rectangle(2,2,50,298)
canvas.create_line(2,2,50, 298)

canvas.create_polygon(2,2, 5, 20, 50, 30, 40, 15)

root.mainloop()