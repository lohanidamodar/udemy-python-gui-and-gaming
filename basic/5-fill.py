 #!/usr/bin/env python
__author__ = 'dlohani'


from tkinter import *

root = Tk()



button1 = Button(None, text="Click Me!", fg = "Blue")
button1.pack()

button2 = Button(None, text="Don't Click Me!", fg = "Red")
button2.pack(fill=X)

button3 = Button(None, text="Click Me!", fg = "Blue")
button3.pack(side=RIGHT, fill = Y)

button4 = Button(None, text="Don't Click Me!", fg = "Red")
button4.pack()

root.mainloop()
