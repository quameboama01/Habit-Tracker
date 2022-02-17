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
    #"quantity": input("How many Kilometers did you Cycle today? ")
}
update_endpoint = f"{pixel_endpoint}/{date}"
update_data = {
    "quantity": "40.00"
}

response = requests.delete(url=update_endpoint, headers=headers)
response.raise_for_status
print(response.text)