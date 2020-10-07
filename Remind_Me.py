import tkinter as tk
import time
import os


from tkinter import *

window = Tk()

window.title("Reminder")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10,text="Amount of Seconds")

txt.grid(column=1, row=0)

def clicked():

    time.sleep(int(txt.get()))
    os.startfile("C:\\Users\stavr\PycharmProjects\Artificial Intelligence Human\dist\\Notification.exe")
    print('finished')

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()