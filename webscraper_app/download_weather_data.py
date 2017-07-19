import requests

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

# extracts and prints the name of the forecast item (period),
# the short description of the conditions (short_desc),
# and the temperature (temp)
period = tonight.find(class_="period-name").get_text()

short_desc = tonight.find(class_="short-desc").get_text()

temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)

# extracts the title attribute from the img tag, treating the BeautifulSoup
# object like a dictionary and passing the attribute we want as a key
img = tonight.find("img")
desc = img['title']

print(desc)
