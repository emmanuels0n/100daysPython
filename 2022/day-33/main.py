import requests
from datetime import datetime

MY_LAT = 45.050209
MY_LONG = 7.640604

# response = requests.get(url="http://api.open-notify.org/iss-now.json")    # Help us get data from the endpoint
# response.raise_for_status()  # To know whats the problem in case of error
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)


