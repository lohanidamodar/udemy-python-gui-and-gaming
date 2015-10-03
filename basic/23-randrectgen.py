__author__ = 'dlohani'

from tkinter import *
import random

root = Tk()
canvas = Canvas(root,width = 300, height=300)
canvas.pack()

colors = ["red","blue","gold","green","grey","black"]

def randomRects(total):
    for i in range(total):
        x1 = random.randrange(300)
        y1 = random.randrange(300)
        x2 = random.randrange(300)
        y2 = random.randrange(300)
        canvas.create_rectangle(x1, x2, y1, y2)


randomRects(10)
root.mainloop()