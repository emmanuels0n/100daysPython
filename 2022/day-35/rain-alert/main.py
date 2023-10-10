import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "da271259723e621f5a65a03523639ff6"
account_sid = 'ACbf08fe722afbd98a50b16db5ac7808b5'
auth_token = '380843333f2f0617ccabba0922b09fec'

weather_params = {
    "lat": 45.068371,
    "lon": 7.683070,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 500:
        print("Bring an umbrella")
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today; remember to bring an Umbrella",
        from_='+13093883503',
        to='+393518379313'
    )

    print(message.status)
# print(weather_data["hourly"][0]["weather"][0]["id"])
