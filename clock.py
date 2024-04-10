from tkinter import *
from time import *
def clock():
    the_time=strftime("%I:%M:%S %p")
    time_label.config(text=the_time)

    the_date=strftime("%B %d,%Y")
    date_label.config(text=the_date)

    the_day = strftime("%A")
    day_label.config(text=the_day)

    time_label.after(1000,clock)

window=Tk()

time_label=Label(window,font=("Arial",55),fg="green",bg="white")
time_label.pack()

date_label=Label(window,font=("Ink Free",35),fg="green",bg="white")
date_label.pack()

day_label=Label(window,font=("Ink Free",35),fg="green",bg="white")
day_label.pack()

clock()
window.mainloop()







