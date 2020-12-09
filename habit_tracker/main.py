import requests
import datetime as dt

PIXELA_USERNAME = "jackprogramador"
PIXELA_API_URL = "https://pixe.la/v1/users"
PIXELA_API_TOKEN = "j34lk32k4h4fgfgh"
PIXELA_GRAPH_ID = "graph1"

# user_params = {
#     "token": PIXELA_API_TOKEN,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(PIXELA_API_URL, json=user_params)

# graph_params = {
#     "id": PIXELA_GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": PIXELA_API_TOKEN
}
#
# response = requests.post(f"{PIXELA_API_URL}/{PIXELA_USERNAME}/graphs",
#                          json=graph_params, headers=headers)

now = dt.datetime.now()
# post_body = {
#     "date": now.strftime("%Y%m%d"),
#     "quantity": "98.50"
# }
#
# response = requests.post(f"{PIXELA_API_URL}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}", json=post_body, headers=headers)

# put_body = {
#     "quantity": "5.12"
# }
# response = requests.put(f"{PIXELA_API_URL}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{now.strftime('%Y%m%d')}",
#                         json=put_body, headers=headers)

# response = requests.delete(f"{PIXELA_API_URL}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{now.strftime('%Y%m%d')}",
#                            headers=headers)
# print(response.text)
