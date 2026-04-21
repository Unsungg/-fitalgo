import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Generate synthetic training data based on fitness science formulas
np.random.seed(42)
n_samples = 1000

# Random user data for training
ages = np.random.randint(18, 65, n_samples)
heights = np.random.randint(155, 200, n_samples)
weights = np.random.randint(50, 120, n_samples)
genders = np.random.choice(['male', 'female'], n_samples)
activity_levels = np.random.choice(
    ['sedentary', 'lightly_active', 'moderate', 'active', 'very_active'],
    n_samples
)
goals = np.random.choice(['lose_weight', 'gain_muscle', 'get_fit'], n_samples)

# Calculate target calories using Mifflin-St Jeor as ground truth
activity_map = {
    'sedentary': 1.2,
    'lightly_active': 1.375,
    'moderate': 1.55,
    'active': 1.725,
    'very_active': 1.9
}
goal_map = {
    'lose_weight': -500,
    'gain_muscle': +300,
    'get_fit': 0
}

target_calories = []
for i in range(n_samples):
    if genders[i] == 'male':
        bmr = 10 * weights[i] + 6.25 * heights[i] - 5 * ages[i] + 5
    else:
        bmr = 10 * weights[i] + 6.25 * heights[i] - 5 * ages[i] - 161
    tdee = bmr * activity_map[activity_levels[i]]
    calories = tdee + goal_map[goals[i]]
    # Add small noise to make it realistic
    calories += np.random.normal(0, 50)
    target_calories.append(round(calories))

# Encode categorical variables for ML model
le_gender = LabelEncoder()
le_activity = LabelEncoder()
le_goal = LabelEncoder()

gender_encoded = le_gender.fit_transform(genders)
activity_encoded = le_activity.fit_transform(activity_levels)
goal_encoded = le_goal.fit_transform(goals)

# Build feature matrix
X = np.column_stack([
    ages, heights, weights,
    gender_encoded, activity_encoded, goal_encoded
])
y = np.array(target_calories)

# Split data and train Random Forest model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Calculate model accuracy score
train_score = round(model.score(X_train, y_train) * 100, 1)
test_score = round(model.score(X_test, y_test) * 100, 1)

def predict_calories(age, height, weight, gender, activity_level, goal):
    # Encode input values using trained encoders
    try:
        gender_enc = le_gender.transform([gender])[0]
        activity_enc = le_activity.transform([activity_level])[0]
        goal_enc = le_goal.transform([goal])[0]
    except ValueError:
        return None

    # Create feature array and predict
    features = np.array([[age, height, weight, gender_enc, activity_enc, goal_enc]])
    predicted = model.predict(features)[0]
    return round(predicted)

def get_model_accuracy():
    # Return model accuracy scores for display
    return {
        'train_score': train_score,
        'test_score': test_score,
        'n_samples': n_samples
    }