import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    api_key = "8a52e1c95657c427fe7d7c834cecba52"
    city = city_entry.get()
    
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        weather_data = response.json()
        
        if weather_data["cod"] != "404":
            city_name = weather_data["name"]
            temperature = weather_data["main"]["temp"]
            weather_desc = weather_data["weather"][0]["description"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            result_label.config(text=f"City: {city_name}\nTemperature: {temperature}°C\nWeather: {weather_desc.title()}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found. Please enter a valid city name.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve data. Check your internet connection or try again later.")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#1C1C1C")

title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), fg="white", bg="#1C1C1C")
title_label.pack(pady=20)

city_entry = tk.Entry(root, width=20, font=("Arial", 14), bg="#2C2C2C", fg="white", insertbackground="white", relief="solid", bd=1)
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), bg="#00BFFF", fg="white", activebackground="#1E90FF", relief="flat", command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="Enter a city and press 'Get Weather'.", font=("Arial", 14), fg="#F0F0F0", bg="#1C1C1C", justify="left")
result_label.pack(pady=20)

root.mainloop()
