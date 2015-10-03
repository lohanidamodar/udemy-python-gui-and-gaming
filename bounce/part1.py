__author__ = 'dlohani'

from tkinter import *
import random
import time

root = Tk()
root.title("Bounce!")
root.resizable(0,0)
root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()


root.update()



class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        self.canvas.move(self.id, 0, -1)


ball = Ball(canvas, "red")


while 1:
    ball.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()