# !/usr/bin/env python
__author__ = 'dlohani'

from tkinter import *

root = Tk()

def evaluate(event):
    data = entry.get()
    result.configure(text="Answer: " + str(eval(data)))

label1 = Label(root, text = "Enter your expression: ")
label1.pack()

entry = Entry(root)
entry.bind("<Return>",evaluate)
entry.pack()

result = Label(root)
result.pack()

root.geometry("500x300")
root.mainloop()
