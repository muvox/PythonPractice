from tkinter import (StringVar, Tk, Message, Label, Button, RAISED, BOTTOM)
import sys

testStrinng = """ Loads of text
-works
-like a
-trains
*toilet*
"""


def endme():
    window.destroy()
    sys.exit(0)


window = Tk()
window.geometry("500x200")


var = StringVar()
w = Message(window, textvariable=var, bg='purple', relief=RAISED)
var.set(testStrinng)
w.pack()

text_window = Label(window, text="Tkinter in action")
text_window.pack()
button = Button(window, bg='blue', text="Button")
button.pack()
endme_button = Button(window, text="Quit", command=endme)
endme_button.pack(side=BOTTOM)

window.mainloop()
