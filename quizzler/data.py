import requests

request_params = {
    "amount": 10,
    "category": 11,
    "difficulty": "easy",
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=request_params)
response.raise_for_status()
data = response.json()
question_data = data["results"]
