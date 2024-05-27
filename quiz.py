import json
import requests


url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=multiple"
response = requests.get(url)

if response.status_code == 200:
    result = response.json()
    print(result['results'])
