#------------------------------------------------------------------Library-------------------------------------------------------------------
import datetime
import pygame
import tkinter as tk

#------------------------------------------------------------------Function-----------------------------------------------------------------
    
def alarm():

    hour = int(hour_input.get())
    minute = int(minute_input.get())
   
    alarm_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0).strftime("%H:%M")
    
    current_time = datetime.datetime.now().strftime("%H:%M")
   
    while current_time < alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M")
       
    while current_time == alarm_time:
	    print("Wake up!")
	    pygame.mixer.music.load("rooster.wav") 
	    pygame.mixer.music.play()
	   
#--------------------------------------------------------------------GUI--------------------------------------------------------------------  
root = tk.Tk()
root.title("Alarm Clock")

tk.Label(root, text="Hour:").grid(row=0, column=0)

hour_input = tk.Entry(root)
hour_input.grid(row=0, column=1)

tk.Label(root, text="Minute:").grid(row=1, column=0)

minute_input = tk.Entry(root)
minute_input.grid(row=1, column=1)

tk.Button(root, text="Set Alarm", command=alarm).grid(row=2, column=0, columnspan=2)

root.mainloop()


