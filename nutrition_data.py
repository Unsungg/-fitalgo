import pandas as pd
import numpy as np

# Sample nutrition database inspired by USDA FoodData Central
FOOD_DATA = {
    'food': [
        'Chicken Breast', 'Salmon', 'Tuna', 'Eggs', 'Greek Yogurt',
        'Brown Rice', 'Oatmeal', 'Sweet Potato', 'Quinoa', 'Whole Wheat Bread',
        'Broccoli', 'Spinach', 'Banana', 'Apple', 'Orange',
        'Almonds', 'Olive Oil', 'Avocado', 'Cottage Cheese', 'Lentils'
    ],
    'category': [
        'protein', 'protein', 'protein', 'protein', 'protein',
        'carbs', 'carbs', 'carbs', 'carbs', 'carbs',
        'vegetable', 'vegetable', 'fruit', 'fruit', 'fruit',
        'fat', 'fat', 'fat', 'protein', 'protein'
    ],
    'calories_per_100g': [
        165, 208, 132, 155, 59,
        216, 389, 86, 368, 247,
        34, 23, 89, 52, 47,
        579, 884, 160, 98, 116
    ],
    'protein_g': [
        31, 20, 29, 13, 10,
        4.5, 17, 1.6, 14, 13,
        2.8, 2.9, 1.1, 0.3, 0.9,
        21, 0, 2, 11, 9
    ],
    'carbs_g': [
        0, 0, 0, 1.1, 3.6,
        45, 66, 20, 64, 41,
        7, 3.6, 23, 14, 12,
        22, 0, 9, 3.4, 20
    ],
    'fat_g': [
        3.6, 13, 1, 11, 0.4,
        1.8, 7, 0.1, 6, 3.4,
        0.4, 0.4, 0.3, 0.2, 0.1,
        50, 100, 15, 4.3, 0.4
    ]
}

# Convert to pandas DataFrame for easy processing
df_foods = pd.DataFrame(FOOD_DATA)

def get_meal_suggestions(target_calories, goal):
    # Calculate calories per meal (3 meals per day)
    calories_per_meal = target_calories / 3

    # Filter foods by goal priority
    if goal == 'gain_muscle':
        # Prioritize high protein foods
        priority_categories = ['protein', 'carbs', 'fat', 'vegetable', 'fruit']
    elif goal == 'lose_weight':
        # Prioritize low calorie, high volume foods
        priority_categories = ['vegetable', 'fruit', 'protein', 'carbs', 'fat']
    else:
        # Balanced approach for get_fit
        priority_categories = ['protein', 'vegetable', 'carbs', 'fruit', 'fat']

    meals = {}
    for meal_name, meal_calories in [('Breakfast', calories_per_meal * 0.3),
                                      ('Lunch', calories_per_meal * 0.4),
                                      ('Dinner', calories_per_meal * 0.3)]:
        meal_foods = []
        remaining_calories = meal_calories

        for category in priority_categories:
            if remaining_calories <= 0:
                break
            # Get foods from this category
            category_foods = df_foods[df_foods['category'] == category]
            if len(category_foods) == 0:
                continue

            # Pick a random food from category
            food = category_foods.sample(1).iloc[0]

            # Calculate portion size in grams
            portion_g = round((remaining_calories * 0.4) / (food['calories_per_100g'] / 100))
            portion_g = max(50, min(portion_g, 300))  # Between 50g and 300g
            food_calories = round(portion_g * food['calories_per_100g'] / 100)

            meal_foods.append({
                'food': food['food'],
                'portion_g': portion_g,
                'calories': food_calories,
                'protein_g': round(portion_g * food['protein_g'] / 100, 1),
                'carbs_g': round(portion_g * food['carbs_g'] / 100, 1),
                'fat_g': round(portion_g * food['fat_g'] / 100, 1)
            })
            remaining_calories -= food_calories

        meals[meal_name] = meal_foods

    return meals
def get_meal_recipes(goal):
    # Recipe suggestions based on fitness goal
    recipes = {
        'lose_weight': [
            {
                'meal': 'Breakfast',
                'name': 'Greek Yogurt Protein Bowl',
                'ingredients': ['200g Greek yogurt', '1 banana', '30g oats', '1 tbsp honey', '10g chia seeds'],
                'instructions': 'Mix oats into Greek yogurt. Slice banana on top. Drizzle honey and sprinkle chia seeds.',
                'prep_time': '5 min',
                'calories': 380,
                'protein': 22,
                'carbs': 58,
                'fat': 6
            },
            {
                'meal': 'Lunch',
                'name': 'Grilled Chicken & Quinoa Salad',
                'ingredients': ['150g chicken breast', '80g quinoa', '100g spinach', '50g cherry tomatoes', '1 tbsp olive oil', 'lemon juice'],
                'instructions': 'Cook quinoa. Grill chicken with salt and pepper. Combine with spinach and tomatoes. Dress with olive oil and lemon.',
                'prep_time': '20 min',
                'calories': 450,
                'protein': 45,
                'carbs': 38,
                'fat': 12
            },
            {
                'meal': 'Dinner',
                'name': 'Baked Salmon with Sweet Potato',
                'ingredients': ['180g salmon fillet', '150g sweet potato', '100g broccoli', '1 tbsp olive oil', 'garlic', 'herbs'],
                'instructions': 'Bake salmon at 200°C for 15 min. Roast sweet potato cubes. Steam broccoli. Season with garlic and herbs.',
                'prep_time': '25 min',
                'calories': 480,
                'protein': 38,
                'carbs': 42,
                'fat': 14
            }
        ],
        'gain_muscle': [
            {
                'meal': 'Breakfast',
                'name': 'Muscle Builder Omelette',
                'ingredients': ['4 whole eggs', '50g oats', '1 banana', '200ml whole milk', '30g cheese'],
                'instructions': 'Whisk eggs, cook omelette with cheese. Serve with oatmeal made with milk and topped with banana.',
                'prep_time': '10 min',
                'calories': 620,
                'protein': 42,
                'carbs': 65,
                'fat': 18
            },
            {
                'meal': 'Lunch',
                'name': 'Beef & Rice Power Bowl',
                'ingredients': ['200g lean beef mince', '150g brown rice', '100g broccoli', '2 tbsp soy sauce', '1 tbsp sesame oil', 'garlic'],
                'instructions': 'Cook rice. Brown beef with garlic. Steam broccoli. Combine in bowl, drizzle with soy sauce and sesame oil.',
                'prep_time': '25 min',
                'calories': 680,
                'protein': 52,
                'carbs': 72,
                'fat': 16
            },
            {
                'meal': 'Dinner',
                'name': 'Tuna Pasta with Avocado',
                'ingredients': ['150g whole wheat pasta', '120g tuna', '1 avocado', '50g cherry tomatoes', '1 tbsp olive oil', 'lemon', 'herbs'],
                'instructions': 'Cook pasta. Mix tuna with diced avocado, tomatoes and olive oil. Combine with pasta and squeeze lemon.',
                'prep_time': '15 min',
                'calories': 650,
                'protein': 45,
                'carbs': 68,
                'fat': 20
            }
        ],
        'get_fit': [
            {
                'meal': 'Breakfast',
                'name': 'Overnight Oats with Berries',
                'ingredients': ['80g oats', '200ml almond milk', '100g mixed berries', '1 tbsp almond butter', '1 tbsp maple syrup'],
                'instructions': 'Mix oats with almond milk the night before. In the morning top with berries, almond butter and maple syrup.',
                'prep_time': '5 min (+ overnight)',
                'calories': 420,
                'protein': 14,
                'carbs': 62,
                'fat': 14
            },
            {
                'meal': 'Lunch',
                'name': 'Turkey & Avocado Wrap',
                'ingredients': ['2 whole wheat wraps', '150g turkey breast', '1 avocado', '50g lettuce', '2 tbsp hummus', 'tomato'],
                'instructions': 'Spread hummus on wrap. Layer turkey, sliced avocado, lettuce and tomato. Roll tightly and slice.',
                'prep_time': '10 min',
                'calories': 520,
                'protein': 38,
                'carbs': 48,
                'fat': 18
            },
            {
                'meal': 'Dinner',
                'name': 'Lentil & Vegetable Curry',
                'ingredients': ['200g red lentils', '1 can coconut milk', '100g spinach', 'curry powder', 'garlic', 'ginger', '150g brown rice'],
                'instructions': 'Sauté garlic and ginger. Add lentils, coconut milk and curry powder. Simmer 20 min. Add spinach. Serve with rice.',
                'prep_time': '30 min',
                'calories': 580,
                'protein': 28,
                'carbs': 82,
                'fat': 12
            }
        ]
    }
    return recipes.get(goal, recipes['get_fit'])