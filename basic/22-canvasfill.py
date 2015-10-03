__author__ = 'dlohani'

from tkinter import *

root = Tk()
canvas = Canvas(root,width = 300, height=300)
canvas.pack()

def createRect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

createRect(5,5,200,20)
createRect(5,70,200,200)

root.mainloop()