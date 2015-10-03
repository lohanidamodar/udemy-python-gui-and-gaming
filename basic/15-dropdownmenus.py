# !/usr/bin/env python
__author__ = 'dlohani'

from tkinter import *
from tkinter import messagebox

root = Tk()


def onNew():
    print("New clicked ")

def onExit():
    print("Exit clicked")

mainMenu = Menu(root)
root.configure(menu = mainMenu)
subMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu = subMenu1)

subMenu1.add_command(label="New", command = onNew)
subMenu1.add_separator()
subMenu1.add_command(label="Exit", command = onExit)
root.mainloop()
