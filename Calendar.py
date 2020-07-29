import calendar
from tkinter import *
year = int(input("Enter Year"))

root = Tk()
root.geometry("1000x1000")

root.title("My 2020 Calendar")

myCal = calendar.calendar(year)
calYear = Label(root, text = myCal, font = "gothic 15 bold")
calYear.pack()

root.mainloop()