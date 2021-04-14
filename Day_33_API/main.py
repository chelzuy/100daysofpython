import requests 
from datetime import datetime as dt



# #========================= API ENDPOINTS ========================= #

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["latitude"]
# latitude = data["iss_position"]["longitude"]

# iss_position = (latitude, longitude)
# print(iss_position)


#========================= API PARAMETERS ========================= #
MY_LAT = 14.501126
MY_LONG = 121.023781

parameters = {
    "lat" : MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


time_now = dt.now()
print(time_now.hour)
