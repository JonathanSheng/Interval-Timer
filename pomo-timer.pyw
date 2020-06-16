import time
import datetime as dt
import tkinter
from tkinter import messagebox
import winsound

current_time = dt.datetime.now()
pomo_time = 25 * 60
time_change = dt.timedelta(0, pomo_time) #Time after 25 minutes
future_time = current_time + time_change #Time when break starts
break_time = 5 * 60
break_over = current_time + dt.timedelta(0, pomo_time + break_time) #Time after 30 minutes

#Hide window
root = tkinter.Tk() #Starts new window
root.withdraw() #Hides startup window

#Show program started window
messagebox.showinfo('Pomodoro Started', 'It is ' + current_time.strftime('%H:%M') + '\n You have 25 minutes of focus.')

#Keep track of pomodoro sessions completed
total_pomo_done = 0
breaks = True

while True:
    if current_time < future_time:
        pass
    elif future_time <= current_time < break_over:
        if breaks:
            for i in range(3):
                winsound.Beep(800, 700)
            messagebox.showinfo('Break Time', 'It is currently ' + current_time.strftime('%H:%M') + '\nYou have 5 minutes to take a break.')
            breaks = False
    else:
        breaks = True
        for i in range(3):
            winsound.Beep(800, 700)
        user_ans = messagebox.askyesno('Pomodoro Finished', 'Wanna go another session?')
        total_pomo_done += 1
        if user_ans:
            current_time = dt.datetime.now()
            future_time = current_time + time_change
            break_over = current_time + dt.timedelta(0, pomo_time + break_time)
        else:
            messagebox.showinfo('Pomodoro Finished', '\nYou have completed ' + str(total_pomo_done) + ' pomodoro session(s)!')
            break
    time.sleep(5 * 60) #Factor of 5
    current_time = dt.datetime.now()
