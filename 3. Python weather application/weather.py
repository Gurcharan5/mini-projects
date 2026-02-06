import os
from dotenv import load_dotenv
import openmeteo_requests
import pandas as pd
import tkinter
from tkinter import ttk
import sv_ttk
import numpy as np

# Getting information for variables using the .env file
load_dotenv()
LAT  = os.getenv("LAT")
LON = os.getenv("LON")
CITY = os.getenv("CITY")

# Link to open meteo weather api
url = "https://api.open-meteo.com/v1/forecast"
openmeteo = openmeteo_requests.Client()

# Setting parameters to get data from my api
params = {
    "latitude": LAT,
    "longitude": LON,
    "hourly": ["uv_index", "temperature_2m", "relative_humidity_2m", "rain"],
    "current": ["temperature_2m", "rain"],
}

responses = openmeteo.weather_api(url, params=params)
response = responses[0]

# Current weather conditions
current = response.Current()
current_temperature_2m = int(current.Variables(0).Value())
current_rain = current.Variables(1).Value()
current_rain = int(current_rain * 100)

# Hourly / future weather conditions
hourly = response.Hourly()
hourly_uv_index = hourly.Variables(0).ValuesAsNumpy()
hourly_temperature_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(2).ValuesAsNumpy()
hourly_rain = hourly.Variables(3).ValuesAsNumpy()

# Putting my hourly data in an hourly format
hourly_data = {"Time": pd.date_range(
start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = hourly.Interval()),
inclusive = "left"
)}

# Putting my hourly data into a more readable format
hourly_data["Temperature °C"] = np.round(hourly_temperature_2m).astype(int)
hourly_data["Rain Percentage %"] = np.round(hourly_rain * 100).astype(int)

hourly_dataframe = pd.DataFrame(data = hourly_data)

# Creating my tkinter GUI
root = tkinter.Tk()
root.title("Weather application")

# Creating my current weather variables
current_temp_var = tkinter.StringVar()
current_temp_var.set(current_temperature_2m)
current_rain_var = tkinter.StringVar()
current_rain_var.set(current_rain)

# GUI title
title = ttk.Label(root, text="Weather application").pack(padx=30)
current_frame = ttk.Frame(root)
current_frame.pack(pady=20)

# GUI current weather elements
current_title = ttk.Label(current_frame, text="Current weather conditions").grid(row=0, column=0)
current_temp_label = ttk.Label(current_frame, text="Current temperature: ").grid(row=1,column=0)
current_temp_value = ttk.Label(current_frame, textvariable=current_temp_var).grid(row=1,column=1)
current_degrees_sign = ttk.Label(current_frame, text="°C").grid(row=1, column=2)
current_rain_label = ttk.Label(current_frame, text="Current change of rain: ").grid(row=2, column=0)
current_rain_value = ttk.Label(current_frame, textvariable=current_rain_var).grid(row=2, column=1)
current_rain_sign = ttk.Label(current_frame, text="%").grid(row=2, column=2)

# Hourly frame
hourly_frame = ttk.Frame(root)
hourly_frame.pack()

# Tree view so users can scroll through the hourly weather forecast
tree = ttk.Treeview(hourly_frame, columns=list(hourly_dataframe.columns), show='headings')
for col in hourly_dataframe.columns:
        tree.heading(col, text=col)
        tree.column(col, width=125)

for index, row in hourly_dataframe.iterrows():
        values = list(row)
        values[0] = values[0].strftime('%H:%M') 
        tree.insert("", "end", values=values)

tree.pack()

# Setting GUI theme and mainloop
sv_ttk.set_theme("dark")
root.mainloop()
