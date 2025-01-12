from tkinter import *

top  = Tk()
top.geometry("200x300")
top.title("List")

label = Label(top,height="1",width="15",bg="blue",text="Food list",fg="red")

list = Listbox(top,width="15",height="40",font="15",activestyle="dotbox",bg="red",fg="blue")

list.insert(1,"Banana")
list.insert(2,"Burger")
list.insert(3,"Pizza")
list.insert(4,"Sandwich")

label.pack()
list.pack()

top.mainloop()