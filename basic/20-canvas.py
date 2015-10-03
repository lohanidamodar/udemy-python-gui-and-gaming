__author__ = 'dlohani'

from tkinter import *

root = Tk()
canvas = Canvas(root,width = 300, height=300)
canvas.pack()

rectangle = canvas.create_rectangle(2,2,50,298)

root.mainloop()