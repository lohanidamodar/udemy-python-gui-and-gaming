 #!/usr/bin/env python
__author__ = 'dlohani'


from tkinter import *




root = Tk()

def clickButton():
    print("Hello damodar")

label1 = Label(root, text = "Name: ")
label1.grid(row=0,column = 0, sticky = "E")

entryName = Entry(root)
entryName.grid(row = 0, column = 1)

label2 = Label(root, text = "Password: ")
label2.grid(row = 1, column = 0, sticky = "E")

entryPassword = Entry(root)
entryPassword.grid(row = 1, column = 1)

button1 = Button(root, text = "Save", command=clickButton)
button1.grid(row=3, column = 0, columnspan = 2)

checkButton = Checkbutton(root, text = "Keep me logged in")
checkButton.grid(row = 2, column = 0, columnspan = 2)

root.mainloop()
