import requests
import json

ingredients_list = {"ingredients": ["soy sauce"]}
ingredients_json = json.dumps(ingredients_list)
url = "http://localhost:8000/get_recipes"

#Send POST request with URL for microservice & JSON with a list of ingredients
response = requests.post(url, ingredients_json)
print(response.json())