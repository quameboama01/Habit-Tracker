import requests

TOKEN = "jadjfhkjafahjajajjafk"
USERNAME = "andrews"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    }
graph_endpoint = f"{pixela_endpoint}{USERNAME}/graphs"
print(graph_endpoint)

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

response = requests.post(url=graph_endpoint, json=graph_config)
response.raise_for_status
print(response.text)

