# find-recipes

## How to REQUEST data:
Send request through HTTP POST call. Call must contain:
- The URL that is hosting the microservice, with the end-point "/get-recipes". For example, if the microservice is being run on http://localhost:8000, request MUST be sent to http://localhost:8000/get-recipes.
- A JSON object with "ingredients" as the key and an array of ingredients as the value. Here is an example object: {"ingredients": ["soy sauce", "butter"]}.

### Example call:
**Note:** Uses Python's <ins>requests</ins> and <ins>json</ins> module
```
ingredients_list = {"ingredients": ["soy sauce", "butter"]}
ingredients_json = json.dumps(ingredients_list)
url = "http://localhost:8000/get_recipes"
response = requests.post(url, ingredients_json)
```

## How to RECEIVE data:
The microservice will send an array of recipes in the response body. Each element of the array will include a dictionary that includes the name of the recipe, the ingredients in the recipe, and recipe instructions. The response will be in JSON _text_ format; it can easily be converted to a JSON object through any modules that handle JSON objects. For example, to convert the response to a JSON in Python, simply import the <ins>json</ins> module, then save the JSON object as demonstrated in the example call.

### Example call:
**Note:** Uses Python's <ins>requests</ins> and <ins>json</ins> module
```
response = requests.post(url, ingredients_json)
print(response.json()) #Adding the json method will convert the response into JSON
```

### Example response object:
[{"name": "Stir-Fried Vegetables Recipe", "ingredients": ["mixed vegetables", "soy sauce", "olive oil", "garlic"], "instructions": "Ingredients: - 2 cups of mixed vegetables (e.g.,
 carrots, broccoli, bell peppers) - 2 tablespoons of soy sauce - 1 tablespoon of olive oil - 1 teaspoon of minced garlic Instructions: 1. Heat the olive oil in a skillet over high 
heat. 2. Add the garlic and stir-fry for 30 seconds. 3. Add the vegetables and stir-fry for 4-5 minutes until tender-crisp. 4. Drizzle with soy sauce and toss to coat. 5. Serve hot. Enjoy your stir-fried vegetables!"}]
