# !/usr/bin/env python
__author__ = 'dlohani'

from tkinter import *
from tkinter import messagebox

root = Tk()

messagebox.showinfo("Information",message="Did you know Nepal is improving?")
answer = messagebox.askquestion("Name","Are you damodar?")
if answer == "yes":
    messagebox.showinfo("Human!!!",message="Thank god!")
if answer == "no":
    messagebox.showinfo("Alien",message="What the fun !!!")
root.mainloop()
