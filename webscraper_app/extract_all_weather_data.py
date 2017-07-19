import requests
import pandas as pd

from bs4 import BeautifulSoup

# downloads the page containing the forecast
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

# create BeautifulSoup class to parse the page
soup = BeautifulSoup(page.content, 'html.parser')

# Finds the div with id "seven-day-forecast"
seven_day = soup.find(id="seven-day-forecast")

# inside seven_day, finds each individual forecast item
forecast_items = seven_day.find_all(class_="tombstone-container")

tonight = forecast_items[0]

# select all items with the class period-name inside an item with the
# class tombstone-container in seven_day
period_tags = seven_day.select(".tombstone-container .period-name")

# use list comprehension to call the get_text method on each
# BeautifulSoup object
periods = [pt.get_text() for pt in period_tags]

# use similar list comprehension for the short_descs, temps, and descs
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# combine the data into a Pandas dataframe and analyze it

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})

# use regex and the series.str.extract method to pull out the numeric
# temperature values

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)

weather["temp_num"] = temp_nums.astype('int')

# find the mean of all the high and low temps
print(weather["temp_num"].mean())

# select only the rows that happen at night
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night

print(is_night)

print(weather[is_night])
