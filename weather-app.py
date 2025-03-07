import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk  # For background image support

# Replace with your OpenWeather API Key
API_KEY = "d5b090597b64fc10359fdb9f81bb9aa9"


# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url).json()

    if response.get("main"):
        temp = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        desc = response["weather"][0]["description"].capitalize()
        weather_label.config(text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nCondition: {desc}")
    else:
        weather_label.config(text="City not found!", fg="red")


# Creating GUI Window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")

# Background Image"
bg_image = Image.open("Background.jpeg")  # Add a background image file in the same folder
bg_image = bg_image.resize((400, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Cover full window

# Title Label
title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), fg="white", bg="#3b6978")
title_label.pack(pady=10)

# Entry Box for City
city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

# Get Weather Button
get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 14), width=15, bg="#ffcc00",
                            fg="black")
get_weather_btn.pack(pady=10)

# Weather Display Label
weather_label = tk.Label(root, font=("Arial", 14), bg="#3b6978", fg="white", width=30, height=5)
weather_label.pack(pady=20)

# Run the App
root.mainloop()
