from fastapi import FastAPI
from pydantic import BaseModel
import json

class IngredientList(BaseModel):
    """Represents a Pydantic model containing a list of strings with ingredient names"""
    ingredients: list = [str]

app = FastAPI()

#Will hold array of matching recipes
matching_recipes = []

#Holds database of recipes
recipes = {
    "grilled cheese sandwich": {
        "name": "Grilled Cheese Sandwich Recipe",
        "ingredients": ["bread", "cheese", "butter"],
        "instructions": """Ingredients: - 2 slices of bread - 2 slices of cheese - 1 tablespoon of butter Instructions: 1. Heat a skillet over medium heat. 2. Spread 1/2 tablespoon of butter on one side of each slice of bread. 3. Place one slice of bread, buttered side down, onto the skillet. 4. Lay the 2 slices of cheese on top of the bread in the skillet. 5. Place the second slice of bread on top, buttered side up. 6. Cook for 2-3 minutes until the bottom slice is golden brown and the cheese begins to melt. 7. Flip the sandwich carefully and cook for another 2-3 minutes until the other side is golden brown and the cheese is fully melted. 8. Remove the sandwich from the skillet, let it cool for a minute, then cut and serve. Enjoy your delicious grilled cheese sandwich!"""
    },
    "spinach and egg scramble": {
        "name": "Spinach and Egg Scramble Recipe",
        "ingredients": ["spinach", "eggs", "olive oil"],
        "instructions": """Ingredients: - 2 cups of fresh spinach - 2 large eggs - 1 tablespoon of olive oil - A pinch of salt - A pinch of pepper Instructions: 1. Heat the olive oil in a skillet over medium heat. 2. Add the spinach to the skillet and sauté for 1-2 minutes until wilted. 3. In a bowl, whisk the eggs with a pinch of salt and pepper. 4. Pour the eggs into the skillet with the spinach. 5. Cook while stirring gently until the eggs are fully set. 6. Remove from heat and serve immediately. Enjoy your simple spinach and egg scramble!"""
    },
    "spinach garlic pasta": {
        "name": "Spinach Garlic Pasta Recipe",
        "ingredients": ["spinach", "pasta", "olive oil", "garlic", "chili flakes"],
        "instructions": """Ingredients: - 2 cups of fresh spinach - 200g of pasta - 2 tablespoons of olive oil - 3 garlic cloves, minced - 1/4 teaspoon of chili flakes - Salt and pepper to taste - Grated Parmesan cheese for serving Instructions: 1. Cook the pasta according to the package instructions, then drain and set aside. 2. Heat the olive oil in a large skillet over medium heat. 3. Add the minced garlic and chili flakes, sautéing for 1 minute until fragrant. 4. Add the spinach and cook for 2-3 minutes until wilted. 5. Toss the cooked pasta with the spinach mixture, seasoning with salt and pepper. 6. Serve warm, topped with grated Parmesan cheese. Enjoy your delicious spinach garlic pasta!"""
    },
    "banana pancakes": {
        "name": "Banana Pancakes Recipe",
        "ingredients": ["banana", "egg", "rolled oats", "cinnamon", "butter"],
        "instructions": """Ingredients: - 1 ripe banana - 1 large egg - 1/4 cup of rolled oats - 1/2 teaspoon of cinnamon - Butter or oil for cooking Instructions: 1. Mash the banana in a bowl. 2. Mix in the egg, oats, and cinnamon until combined. 3. Heat butter or oil in a skillet over medium heat. 4. Scoop small portions of the batter onto the skillet. 5. Cook for 2-3 minutes on each side until golden brown. 6. Serve warm with your favorite toppings. Enjoy your banana pancakes!"""
    },
    "avocado toast": {
        "name": "Avocado Toast Recipe",
        "ingredients": ["bread", "avocado", "chili flakes"],
        "instructions": """Ingredients: - 1 slice of bread - 1/2 ripe avocado - A pinch of salt - A pinch of red chili flakes Instructions: 1. Toast the bread until golden brown. 2. Mash the avocado in a bowl and season with salt. 3. Spread the avocado on the toasted bread. 4. Sprinkle red chili flakes on top. 5. Serve immediately. Enjoy your avocado toast!"""
    },
    "peanut butter smoothie": {
        "name": "Peanut Butter Smoothie Recipe",
        "ingredients": ["banana", "peanut butter", "milk", "almond milk", "honey"],
        "instructions": """Ingredients: - 1 banana - 1 tablespoon of peanut butter - 1 cup of milk or almond milk - 1/2 teaspoon of honey (optional) - A handful of ice cubes Instructions: 1. Add the banana, peanut butter, milk, honey, and ice cubes to a blender. 2. Blend until smooth and creamy. 3. Pour into a glass and serve immediately. Enjoy your peanut butter smoothie!"""
    },
    "caprese salad": {
        "name": "Caprese Salad Recipe",
        "ingredients": ["tomato", "mozzarella", "basil", "olive oil"],
        "instructions": """Ingredients: - 2 tomatoes, sliced - 4 slices of fresh mozzarella - A handful of fresh basil leaves - 1 tablespoon of olive oil - A pinch of salt and pepper Instructions: 1. Arrange the tomato slices, mozzarella, and basil on a plate. 2. Drizzle with olive oil. 3. Sprinkle with salt and pepper. 4. Serve as a refreshing appetizer. Enjoy your Caprese salad!"""
    },
    "egg salad sandwich": {
        "name": "Egg Salad Sandwich Recipe",
        "ingredients": ["eggs", "mayonnaise", "mayo", "bread"],
        "instructions": """Ingredients: - 2 hard-boiled eggs, chopped - 2 tablespoons of mayonnaise - A pinch of salt and pepper - 2 slices of bread Instructions: 1. Mix the chopped eggs, mayonnaise, salt, and pepper in a bowl. 2. Spread the egg salad onto one slice of bread. 3. Top with the second slice of bread. 4. Cut and serve. Enjoy your egg salad sandwich!"""
    },
    "tomato soup": {
        "name": "Tomato Soup Recipe",
        "ingredients": ["diced tomatoes", "vegetable broth", "milk", "olive oil", "garlic"],
        "instructions": """Ingredients: - 1 can of diced tomatoes - 1 cup of vegetable broth - 1/2 cup of milk - 1 tablespoon of olive oil - 1 garlic clove, minced - A pinch of salt and pepper Instructions: 1. Heat the olive oil in a pot over medium heat. 2. Sauté the minced garlic for 1 minute. 3. Add the diced tomatoes, vegetable broth, and salt. 4. Simmer for 10 minutes. 5. Blend the soup until smooth, then stir in the milk. 6. Heat through and serve. Enjoy your creamy tomato soup!"""
    },
    "stir fried vegetables": {
        "name": "Stir-Fried Vegetables Recipe",
        "ingredients": ["mixed vegetables", "soy sauce", "olive oil", "garlic"],
        "instructions": """Ingredients: - 2 cups of mixed vegetables (e.g., carrots, broccoli, bell peppers) - 2 tablespoons of soy sauce - 1 tablespoon of olive oil - 1 teaspoon of minced garlic Instructions: 1. Heat the olive oil in a skillet over high heat. 2. Add the garlic and stir-fry for 30 seconds. 3. Add the vegetables and stir-fry for 4-5 minutes until tender-crisp. 4. Drizzle with soy sauce and toss to coat. 5. Serve hot. Enjoy your stir-fried vegetables!"""
    }
}



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get_recipes")
async def create_list(ingredient_list: IngredientList): #Async may not be needed

    #Compare ingredients in list to recipe dictionary
    for recipe in recipes: #Represents entries in recipe dictionary
        for ingredient in ingredient_list.ingredients: #For each ingredient in the ingredient_list list
            if ingredient in recipes[recipe]["ingredients"] and recipes[recipe] not in matching_recipes: #If ingredient is an ingredient in a recipe
                matching_recipes.append(recipes[recipe])
    array_to_return = matching_recipes.copy()
    matching_recipes.clear()
    print("array_to_return:", array_to_return)

    return json.dumps(array_to_return)

