from tkinter import *

root = Tk()
root.geometry("250x250")

w = Label(root,text="Chocolates and Ice cream")
w.pack()

frame = Frame(root)
frame.pack()

frame_bottom = Frame(root)
frame_bottom.pack(side=BOTTOM)

b1 = Button(frame,text="White chocolate",fg="grey",bg="black")
b1.pack(side=TOP)

b2 = Button(frame,text="Dark chocolate",fg="black",bg="grey")
b2.pack(side=TOP)

b3 = Button(frame,text="Normal chocolate",fg="brown",bg="white")
b3.pack(side=TOP)

b4 = Button(frame_bottom,text="Strawberry Ice cream",fg="red",bg="pink")
b4.pack(side=BOTTOM)

b5 = Button(frame_bottom,text="Vanilla Ice cream",fg="white",bg="black")
b5.pack(side=BOTTOM)

b6 = Button(frame_bottom,text="Blueberry Ice cream",fg="blue",bg="white")
b6.pack(side=BOTTOM)

root.mainloop()