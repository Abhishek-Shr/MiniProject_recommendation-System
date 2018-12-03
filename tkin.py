from tkinter import *


def onclick():
    print("Double Click To Exit")

root = Tk()
frame = Frame(root).grid(row = 0, column  = 0)

user_l = Label(frame,text = 'Username').grid(row = 1, column  = 0,sticky = W)
pass_l = Label(frame,text = 'Password').grid(row = 2, column  = 0,sticky = W)
user_e = Entry(frame).grid(row = 1, column  = 1,sticky = W)
pass_e = Entry(frame).grid(row = 2, column  = 1n,sticky = W)
submit_b = Button(frame,text = 'Submit').grid(row = 3, column  = 1,sticky = W)

#root.grid_columnconfigure(0, weight=1)
root.mainloop()
    


