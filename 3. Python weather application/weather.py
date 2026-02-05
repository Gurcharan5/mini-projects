import os
from dotenv import load_dotenv
import openmeteo_requests
import pandas as pd
import tkinter
from tkinter import ttk
import sv_ttk

load_dotenv()

LAT  = os.getenv("LAT")
LON = os.getenv("LON")
CITY = os.getenv("CITY")

url = "https://api.open-meteo.com/v1/forecast"
openmeteo = openmeteo_requests.Client()

params = {
    "latitude": LAT,
    "longitude": LON,
    "hourly": ["uv_index", "temperature_2m", "relative_humidity_2m", "rain"],
    "current": ["temperature_2m", "rain"],
}

responses = openmeteo.weather_api(url, params=params)
response = responses[0]

current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_rain = current.Variables(1).Value()

print(f"\nCurrent time: {current.Time()}")
print(f"Current temperature_2m: {current_temperature_2m}")
print(f"Current rain: {current_rain}")

hourly = response.Hourly()
hourly_uv_index = hourly.Variables(0).ValuesAsNumpy()
hourly_temperature_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(2).ValuesAsNumpy()
hourly_rain = hourly.Variables(3).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = hourly.Interval()),
inclusive = "left"
)}

hourly_data["uv_index"] = hourly_uv_index
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["rain"] = hourly_rain

hourly_dataframe = pd.DataFrame(data = hourly_data)
print("\nHourly data\n", hourly_dataframe)

'''
root = tkinter.Tk()
title = ttk.Label(root, text="Current weather").pack()
current_frame = ttk.Frame(root).pack()


sv_ttk.set_theme("dark")
root.mainloop()

'''