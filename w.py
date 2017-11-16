from tkinter import *
from tkinter import messagebox

top = Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text ="Hello", command = helloCallBack)

B.pack()
B.place(bordermode=INSIDE, height=100, width=100)
top.mainloop()