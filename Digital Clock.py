# Import Libraries
import sys # Use system services
from  tkinter import * # Tkinter is for GUI 
import time # Match system time

# Function for time format 
def times(): 
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time)
	clock.after(1000,times)

# Initialize Tkinter and create format
root=Tk()
root.geometry("500x200") # Size of GUI
clock=Label(root,font=("helvetica",50,"bold"),bg="gold") # Label() = the name for the GUI along with design.
clock.grid(row=2,column=2,pady=25,padx=100) # Grid() allows for the layout of the time format
times() # Calling the times() function

digi=Label(root,text="Digital Clock",font="helvetica 24 bold") # Label() = the name for the GUI along with design.
digi.grid(row=0,column=2) # Grid() allows for the layout of the time format

nota=Label(root,text="Hours   Minutes   Seconds   ",font="helvetica 15 bold") # Label() = the name for the GUI along with design.
nota.grid(row=3,column=2) # Grid() allows for the layout of the time format

root.mainloop() # Mainloop() is the end function for Tk()