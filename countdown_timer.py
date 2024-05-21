# Modules
import time
from tkinter import *
from tkinter import messagebox

# Interface
clock_window = Tk()
clock_window.geometry("500x500")
clock_window.title("Countdown Timer")
clock_window.configure(background='green')

# Variables
hour_string = StringVar()
minute_string = StringVar()
second_string = StringVar()

# Set string to default value
hour_string.set("00")
minute_string.set("00")
second_string.set("00")

# Getting input from user
hour_textbox = Entry(clock_window, width=3, font=('Calibri', 20, ''), textvariable=hour_string)
minute_textbox = Entry(clock_window, width=3, font=('Calibri', 20, ''), textvariable=minute_string)
second_textbox = Entry(clock_window, width=3, font=('Calibri', 20, ''), textvariable=second_string)

# Center textboxes
hour_textbox.place(x=170, y=180)
minute_textbox.place(x=220, y=180)
second_textbox.place(x=270, y=180)

# Function
def run_timer():
    ''''''
    try:
        clock_time = int(hour_string.get()) * 3600 + int(minute_string.get()) * 60 + int(second_string.get())
    except:
        print("Incorrect Values!")

    while(clock_time > -1):
        total_minutes, total_seconds = divmod(clock_time, 60)

        total_hours = 0
        if(total_minutes > 60):
            total_hours, total_minutes = divmod(total_minutes, 60)
        
        hour_string.set("{0:2d}".format(total_hours))
        minute_string.set("{0:2d}".format(total_minutes))
        second_string.set("{0:2d}".format(total_seconds))

        # Update the interface
        clock_window.update()
        time.sleep(1)

        # Let the user know if the timer has expired
        if(clock_time == 0):
            messagebox.showinfo('END', 'Your time is expired!') #birinci dirnaq isaresi titledi
        
        clock_time -= 1

set_time_button = Button(clock_window, text='Set Time', bd='5', command=run_timer)
set_time_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Keep looping
clock_window.mainloop()