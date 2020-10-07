import tkinter as tk
import time


from tkinter import *

window = Tk()

window.title("Notification")

window.geometry('350x200')

lbl = Label(window, text="Reminder Wait Time Ended",fg= 'red',bg= 'black',width=30,height= 10)

lbl.grid(row=5, column=5)



window.mainloop()