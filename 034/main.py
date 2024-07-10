import os
import requests
from twilio.rest import Client
import twilio.http.http_client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("13f05f6039583f9f41484006a8a05259")
account_sid = "AC2fb0f8c5a70b07be6a7038096c521a7c"
auth_token = os.environ.get("553b0101210d306d5885ff604072dd9a")

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an ☔️", from_='+12512835213', to='+2348072104997')
    print(message.status)