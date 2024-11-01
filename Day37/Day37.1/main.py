import requests
from datetime import datetime

USERNAME = "xrlab"
USER_TOKEN = "<PIXELA TOKEN>"
GRAPH_ID =  "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(response.text)

GRPAH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": USER_TOKEN,
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

#response = requests.post(url=GRPAH_ENDPOINT, json=graph_params, headers=headers)
#print(response.json())

PIXELA_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime(year=2024, month=10, day=30)
pixel_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "24.1",

}

PIXELA_UPDATE_ENDPOINT = f"{PIXELA_CREATION_ENDPOINT}/{yesterday.strftime('%Y%m%d')}"
#requests.post(url=PIXELA_CREATION_ENDPOINT, headers=headers, json=pixel_params)
#requests.put(PIXELA_UPDATE_ENDPOINT, headers=headers, json=pixel_params)

PIXELA_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(PIXELA_DELETE_ENDPOINT, headers=headers)
print(response.text)


