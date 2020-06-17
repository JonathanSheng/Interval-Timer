import time
import datetime as dt
import tkinter
from tkinter import messagebox
from tkinter.simpledialog import askstring, askinteger
import winsound
from tkinter import simpledialog

root = tkinter.Tk() #Starts new window
root.withdraw() #Hides startup window
work = simpledialog.askinteger("Interval", "Please enter work length (minutes)",
                                 parent=root,
                                 minvalue=0, maxvalue=100)
break_length = simpledialog.askinteger("Interval", "Please enter break length (minutes)",
                                 parent=root,
                                 minvalue=0, maxvalue=100)
current_time = dt.datetime.now()
work_time = work * 60
time_change = dt.timedelta(0, work_time) #Time after work minutes
future_time = current_time + time_change #Time when break starts
break_time = break_length * 60
break_over = current_time + dt.timedelta(0, work_time + break_time) #Time after break time

#Hide window
root = tkinter.Tk() #Starts new window
root.withdraw() #Hides startup window

#Show program started window
messagebox.showinfo('Work Session Started', 'It is currently ' + current_time.strftime('%H:%M') + "\n Your break starts at " + future_time.strftime('%H:%M'))

#Keep track of work sessions completed
work_sessions_done = 0
breaks = True

while True:
    if current_time < future_time:
        pass
    elif future_time <= current_time < break_over:
        if breaks:
            for i in range(3):
                winsound.Beep(800, 700)
            messagebox.showinfo('Break Time', 'It is currently ' + current_time.strftime('%H:%M') + "\n Your work starts at " + break_over.strftime('%H:%M'))
            breaks = False
    else:
        breaks = True
        for i in range(3):
            winsound.Beep(800, 700)
        user_ans = messagebox.askyesno('Work Session Finished', 'Wanna go another session?')
        work_sessions_done += 1
        if user_ans:
            current_time = dt.datetime.now()
            future_time = current_time + time_change
            break_over = current_time + dt.timedelta(0, work_time + break_time)
        else:
            messagebox.showinfo('Work Finished', '\nYou have completed ' + str(work_sessions_done) + ' work session(s)!')
            break
    time.sleep(20) #Factor of 5
    current_time = dt.datetime.now()
