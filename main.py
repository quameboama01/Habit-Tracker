import requests
import datetime as dt

TOKEN = "jadjfhkjafahjajajjafk"
USERNAME = "andrews"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    }
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

now = dt.datetime.now()
date = now.strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_details = {
    "date": date,
    "quantity": input("How many Kilometers did you Cycle today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_details, headers=headers)
response.raise_for_status
print(response.text)