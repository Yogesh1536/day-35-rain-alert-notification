import requests
from twilio.rest import Client

api_key = 'df66c64960a184a3314f17eca5eb7e' # This is wrong authentication Key so create your own api key
MY_LAT = 9.925201
MY_LON = 78.119774
account_sid = "AC0a94f226912db29d1087ab9fe278634f"
auth_token = "2f1a87856d36637f11e3294b9de5b7" # This iis wrong token, create your own token to run code

parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
hourly_dict = weather_data["hourly"][0:12]

will_rain = False
for hourly_weather in hourly_dict:
    weather_id = hourly_weather["weather"][0]["id"]
    if int(weather_id) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today, Don't forget to take your umbrella☔",
        from_='+16206986017', # generate your twillio number
        to='+919080114615' # Enter your phone number, pls verify your number in twillio before running.
    )
print(message.status)