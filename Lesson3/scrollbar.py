from tkinter import *

root = Tk()
root.geometry("100x200")

label  = Label(root,text="Hello",font="20")

label.pack()

scrollbar  = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

list = Listbox(root,yscrollcommand=scrollbar.set)

for i in range(1,100):
    list.insert(END,"Hi"+str(i))

list.pack(side=LEFT,fill=BOTH)

scrollbar.config(command=list.yview)

root.mainloop()