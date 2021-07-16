import requests
from bs4 import BeautifulSoup
from tkinter import Label, mainloop
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/weather/today/l/af60f113ba123ce93774fed531be2e1e51a1666be5d6012f129cfa27bae1ee6c" 

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open("/Users/aliasger/Desktop/weather.jpg")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_= "CurrentConditions--location--2_osB").text
    temperature = soup.find("span", class_= "CurrentConditions--tempValue--1RYJJ").text
    weatherPrediction = soup.find("div", class_="CurrentConditions--phraseValue--17s79").text
    
    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPrediction)

    temperatureLabel.after(60000, getWeather)
    master.update()


locationLabel = Label(master, font =("Calibri bold", 20),bg="white")
locationLabel.grid(row =0, sticky="N",padx=100)
temperatureLabel = Label(master, font =("Calibri bold", 70),bg="white")
temperatureLabel.grid(row =1, sticky="W",padx=100)
Label(master, image=img, bg = "white").grid(row =1, sticky="E")
weatherPredictionLabel = Label(master, font =("Calibri bold", 15),bg = "white")
weatherPredictionLabel.grid(row =2, sticky="W",padx=40)
getWeather()

master.mainloop()


