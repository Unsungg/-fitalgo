import urllib.request

exercises = {
    "Barbell Bench Press": "Barbell_Bench_Press_-_Medium_Grip",
    "Incline Dumbbell Press": "Incline_Dumbbell_Press",
    "Cable Chest Fly": "Cable_Crossover",
    "Deadlift": "Barbell_Deadlift",
    "Pull-ups": "Pullups",
    "Barbell Row": "Bent_Over_Barbell_Row",
    "Barbell Back Squat": "Barbell_Squat",
    "Romanian Deadlift": "Romanian_Deadlift",
    "Leg Press": "Leg_Press",
    "Overhead Press": "Standing_Military_Press",
    "Lateral Raise": "Side_Lateral_Raise",
    "Barbell Curl": "Barbell_Curl",
    "Tricep Pushdown": "Triceps_Pushdown",
    "Plank": "Plank",
    "Cable Crunch": "Cable_Crunch",
    "HIIT Treadmill": "Walking",
    "Jump Rope": "Jump_Rope"
}

base_url = 'https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/'

for name, path in exercises.items():
    url = f"{base_url}{path}/0.jpg"
    try:
        response = urllib.request.urlopen(url)
        print(f"OK: {name}")
    except Exception as e:
        print(f"FAIL: {name} ({url}) - {e}")
