import random
import json

# Sample JSON object storing recipes
recipes = {
    "cuisine": {
        "Italian": {
            "Spaghetti Carbonara": {
                "ingredients": {
                    "spaghetti": "200g",
                    "eggs": "2",
                    "parmesan cheese": "50g",
                    "pancetta": "100g",
                    "black pepper": "to taste",
                    "salt": "to taste"
                }
            },
            "Margherita Pizza": {
                "ingredients": {
                    "pizza dough": "1 ball",
                    "tomato sauce": "100g",
                    "mozzarella": "150g",
                    "basil": "a few leaves",
                    "olive oil": "1 tbsp",
                    "salt": "to taste"
                }
            }
        },
        "Mexican": {
            "Tacos": {
                "ingredients": {
                    "tortillas": "4",
                    "beef": "200g",
                    "onions": "1",
                    "cilantro": "a handful",
                    "lime": "1",
                    "salt": "to taste"
                }
            },
            "Guacamole": {
                "ingredients": {
                    "avocados": "2",
                    "onions": "1",
                    "tomatoes": "1",
                    "lime": "1",
                    "cilantro": "a handful",
                    "salt": "to taste"
                }
            }
        },
        "Indian": {
            "Butter Chicken": {
                "ingredients": {
                    "chicken": "500g",
                    "butter": "50g",
                    "tomato puree": "200g",
                    "cream": "100ml",
                    "garam masala": "1 tbsp",
                    "cumin": "1 tsp",
                    "coriander": "1 tsp"
                }
            },
            "Paneer Tikka": {
                "ingredients": {
                    "paneer": "250g",
                    "yogurt": "50g",
                    "lemon juice": "1 tbsp",
                    "cumin": "1 tsp",
                    "turmeric": "1/2 tsp",
                    "garam masala": "1 tsp",
                    "salt": "to taste"
                }
            }
        }
    }
}

# Function to get random recipes
def get_random_recipes(num=5):
    all_recipes = []
    for cuisine, recipes_dict in recipes['cuisine'].items():
        for recipe_name, recipe_data in recipes_dict.items():
            all_recipes.append((cuisine, recipe_name, recipe_data['ingredients']))
    
    # Get random recipes
    selected_recipes = random.sample(all_recipes, num)
    return selected_recipes

# Function to list all ingredients from the selected recipes
def get_ingredient_list(selected_recipes):
    ingredients_needed = {}
    
    for cuisine, recipe_name, ingredients in selected_recipes:
        for ingredient, quantity in ingredients.items():
            if ingredient in ingredients_needed:
                # Combine ingredients if they already exist
                ingredients_needed[ingredient].append((quantity, recipe_name))
            else:
                ingredients_needed[ingredient] = [(quantity, recipe_name)]
    
    return ingredients_needed

# Function to display ingredients list
def display_ingredients(ingredients_list):
    print("\nIngredients you need:\n")
    for ingredient, details in ingredients_list.items():
        quantities = ", ".join([f"{q} ({r})" for q, r in details])
        print(f"{ingredient}: {quantities}")

# Function to display selected recipes
def display_selected_recipes(selected_recipes):
    print("\nSelected Recipes:\n")
    for i, (cuisine, recipe_name, _) in enumerate(selected_recipes, start=1):
        print(f"{i}. {recipe_name} ({cuisine})")

# Main application loop
def recipe_selector():
    selected_recipes = get_random_recipes()

    while True:
        display_selected_recipes(selected_recipes)
        ingredients_list = get_ingredient_list(selected_recipes)
        display_ingredients(ingredients_list)
        
        print("\nOptions:")
        print("1. Re-roll all recipes")
        print("2. Re-roll specific recipes")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            selected_recipes = get_random_recipes()
        elif choice == "2":
            reroll_indices = input("Enter the recipe numbers you want to reroll (comma separated): ")
            reroll_indices = [int(i.strip()) - 1 for i in reroll_indices.split(',')]
            
            for idx in reroll_indices:
                new_recipe = random.choice(get_random_recipes(1))
                selected_recipes[idx] = new_recipe
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    recipe_selector()
