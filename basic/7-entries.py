 #!/usr/bin/env python
__author__ = 'dlohani'


from tkinter import *

root = Tk()


label1 = Label(root, text = "Name: ")
label1.grid(row=0,column = 0)

entryName = Entry(root)
entryName.grid(row = 0, column = 1)

button1 = Button(root, text = "Save")
button1.grid(row=0, column = 2)

root.mainloop()
