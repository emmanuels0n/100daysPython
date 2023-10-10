# # https://pixe.la/v1/users/emmanuels0n/graphs/graph1.html ; https://pixe.la/@emmanuels0n
import requests
from datetime import datetime

USERNAME = "emmanuels0n"
TOKEN = "DioBrando69"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"  # Green
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text) # Create a graph

new_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2022, month=5, day=23)
# print(today.strftime("%Y%m%d"))

new_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much hours did you study today? ")
}

response = requests.post(url=new_pixel_endpoint, json=new_pixel_config, headers=headers)  # New pixel
print(response.text)

# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220527"
# update_pixel_conf = {
#     "quantity": "5"
# }

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_conf, headers=headers)  # Update a pixel
# print(response.text)
