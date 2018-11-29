from tkinter import *


def onclick():
    print("Double Click To Exit")

root = Tk()
frame = Frame(root).pack()

user_l = Label(frame,text = 'Username').pack(fill = X,expand = 1)
pass_l = Label(frame,text = 'Password').pack(fill = X,expand = 1)
user_e = Entry(frame).pack(fill = X,expand = 1)
pass_e = Entry(frame).pack(fill = X,expand = 1)
submit_b = Button(frame,text = 'Submit').pack()

root.mainloop()



