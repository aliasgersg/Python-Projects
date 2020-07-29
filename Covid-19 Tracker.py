from covid import Covid
from tkinter import *

root = Tk()
covid = Covid()

# Get data by country name
user = str(input("Enter country"))
country = covid.get_status_by_country_name(user)

print(country)
