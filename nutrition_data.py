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