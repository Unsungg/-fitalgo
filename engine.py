import numpy as np
from nutrition_data import get_meal_suggestions
from ml_model import predict_calories, get_model_accuracy

# Activity level multipliers for TDEE calculation
ACTIVITY_MULTIPLIERS = {
    'sedentary': 1.2,
    'lightly_active': 1.375,
    'moderate': 1.55,
    'active': 1.725,
    'very_active': 1.9
}

# Goal-based calorie adjustments
GOAL_ADJUSTMENTS = {
    'lose_weight': -500,
    'gain_muscle': +300,
    'get_fit':     0
}

def calculate_bmr(weight, height, age, gender):
    # Mifflin-St Jeor formula to calculate base metabolic rate
    if gender == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr, activity_level):
    # Total Daily Energy Expenditure = BMR x activity multiplier
    multiplier = ACTIVITY_MULTIPLIERS.get(activity_level, 1.2)
    return bmr * multiplier

def calculate_target_calories(tdee, goal):
    # Adjust calories based on user goal
    adjustment = GOAL_ADJUSTMENTS.get(goal, 0)
    return tdee + adjustment

def generate_workout_plan(goal, activity_level):
    # Generate a weekly workout plan based on goal and activity level
    plans = {
        'lose_weight': {
            'Monday':    'Cardio 45 min (running or cycling)',
            'Tuesday':   'Full body strength training 40 min',
            'Wednesday': 'Rest or light walking 30 min',
            'Thursday':  'HIIT training 30 min',
            'Friday':    'Strength training (upper body) 40 min',
            'Saturday':  'Cardio 45 min (swimming or cycling)',
            'Sunday':    'Rest day'
        },
        'gain_muscle': {
            'Monday':    'Chest and triceps 50 min',
            'Tuesday':   'Back and biceps 50 min',
            'Wednesday': 'Rest or light cardio 20 min',
            'Thursday':  'Legs and shoulders 50 min',
            'Friday':    'Full body compound movements 45 min',
            'Saturday':  'Arms and core 40 min',
            'Sunday':    'Rest day'
        },
        'get_fit': {
            'Monday':    'Moderate cardio 30 min',
            'Tuesday':   'Full body workout 40 min',
            'Wednesday': 'Yoga or stretching 30 min',
            'Thursday':  'Cardio + core 35 min',
            'Friday':    'Strength training 40 min',
            'Saturday':  'Outdoor activity 45 min',
            'Sunday':    'Rest day'
        }
    }
    return plans.get(goal, plans['get_fit'])

def generate_full_plan(user):
    # Main function — generates complete fitness plan for a user
    bmr = calculate_bmr(user.weight, user.height, user.age, user.gender)
    tdee = calculate_tdee(bmr, user.activity_level)

    # Use ML model to predict calories
    ml_predicted = predict_calories(
        user.age, user.height, user.weight,
        user.gender, user.activity_level, user.goal
    )

    # Use ML prediction if available, otherwise fall back to formula
    target_calories = ml_predicted if ml_predicted else calculate_target_calories(tdee, user.goal)

    workout_plan = generate_workout_plan(user.goal, user.activity_level)
    meal_suggestions = get_meal_suggestions(target_calories, user.goal)

    # Get model accuracy info
    model_info = get_model_accuracy()

    return {
        'bmr': round(bmr),
        'tdee': round(tdee),
        'target_calories': round(target_calories),
        'workout_plan': workout_plan,
        'protein_g': round((target_calories * 0.30) / 4),
        'carbs_g':   round((target_calories * 0.45) / 4),
        'fat_g':     round((target_calories * 0.25) / 9),
        'meal_suggestions': meal_suggestions,
        'model_accuracy': model_info
    }

def update_plan_based_on_progress(user, progress_entries):
    # Need at least 2 entries to detect a trend
    if len(progress_entries) < 2:
        return generate_full_plan(user)

    # Get the last two weight entries to calculate weekly change
    weights = [entry.weight for entry in progress_entries]
    latest_weight = weights[-1]
    previous_weight = weights[-2]
    weekly_change = latest_weight - previous_weight

    # Update user's current weight with latest entry
    user.weight = latest_weight

    # Adaptive logic — adjust goal based on progress trend
    if user.goal == 'lose_weight':
        if weekly_change > 0.5:
            user.activity_level = 'active'
        elif weekly_change < -1.5:
            user.activity_level = 'lightly_active'

    elif user.goal == 'gain_muscle':
        if weekly_change < 0:
            user.activity_level = 'very_active'
        elif weekly_change > 1.0:
            user.activity_level = 'moderate'

    # Recalculate and return updated plan
    return generate_full_plan(user)