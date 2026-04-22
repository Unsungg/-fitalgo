# Detailed exercise database with form tips and calorie burn

EXERCISES = {
    'chest': [
        {
            'name': 'Barbell Bench Press',
            'muscles': ['Chest', 'Triceps', 'Front Deltoid'],
            'sets': 4, 'reps': '8-10 reps', 'rest': '90 sec rest',
            'calories': 45,
            'form_tip': 'Keep shoulder blades retracted, feet flat on floor, bar touches mid-chest.',
            'mistake': 'Flaring elbows outward — keep them at 45 degrees to protect shoulders.'
        },
        {
            'name': 'Incline Dumbbell Press',
            'muscles': ['Upper Chest', 'Front Deltoid'],
            'sets': 3, 'reps': '10-12 reps', 'rest': '75 sec rest',
            'calories': 38,
            'form_tip': 'Set bench to 30-45 degrees, press dumbbells up and slightly inward.',
            'mistake': 'Using too steep an incline — this shifts load to shoulders, not chest.'
        },
        {
            'name': 'Cable Chest Fly',
            'muscles': ['Chest', 'Front Deltoid'],
            'sets': 3, 'reps': '12-15 reps', 'rest': '60 sec rest',
            'calories': 28,
            'form_tip': 'Slight bend in elbows, think of hugging a tree. Squeeze chest at peak.',
            'mistake': 'Bending elbows too much — this turns it into a press, not a fly.'
        }
    ],
    'back': [
        {
            'name': 'Deadlift',
            'muscles': ['Lower Back', 'Glutes', 'Hamstrings', 'Traps'],
            'sets': 4, 'reps': '5-6 reps', 'rest': '2 min rest',
            'calories': 60,
            'form_tip': 'Bar over mid-foot, hinge at hips, keep back neutral, drive through heels.',
            'mistake': 'Rounding the lower back — this is the most common injury cause in deadlifts.'
        },
        {
            'name': 'Pull-ups',
            'muscles': ['Lats', 'Biceps', 'Rear Deltoid'],
            'sets': 3, 'reps': 'Max reps', 'rest': '90 sec rest',
            'calories': 35,
            'form_tip': 'Full hang at bottom, pull elbows to hips, chin over bar at top.',
            'mistake': 'Using momentum and kipping — do slow, controlled reps for muscle growth.'
        },
        {
            'name': 'Barbell Row',
            'muscles': ['Lats', 'Rhomboids', 'Biceps'],
            'sets': 3, 'reps': '8-10 reps', 'rest': '90 sec rest',
            'calories': 40,
            'form_tip': 'Hinge forward 45 degrees, pull bar to lower chest, lead with elbows.',
            'mistake': 'Standing too upright — this reduces lat engagement significantly.'
        }
    ],
    'legs': [
        {
            'name': 'Barbell Back Squat',
            'muscles': ['Quads', 'Glutes', 'Hamstrings', 'Core'],
            'sets': 4, 'reps': '8-10 reps', 'rest': '2 min rest',
            'calories': 65,
            'form_tip': 'Feet shoulder-width, chest up, squat until thighs parallel, drive through heels.',
            'mistake': 'Knees caving inward — push knees out in line with toes throughout.'
        },
        {
            'name': 'Romanian Deadlift',
            'muscles': ['Hamstrings', 'Glutes', 'Lower Back'],
            'sets': 3, 'reps': '10-12 reps', 'rest': '90 sec rest',
            'calories': 48,
            'form_tip': 'Soft knee bend, push hips back, lower bar along legs, feel hamstring stretch.',
            'mistake': 'Bending knees too much — this turns it into a regular deadlift.'
        },
        {
            'name': 'Leg Press',
            'muscles': ['Quads', 'Glutes'],
            'sets': 3, 'reps': '12-15 reps', 'rest': '75 sec rest',
            'calories': 42,
            'form_tip': 'Feet hip-width on platform, lower until 90 degrees, press without locking knees.',
            'mistake': 'Placing feet too low — this puts excessive stress on the knees.'
        }
    ],
    'shoulders': [
        {
            'name': 'Overhead Press',
            'muscles': ['Front Deltoid', 'Side Deltoid', 'Triceps'],
            'sets': 4, 'reps': '8-10 reps', 'rest': '90 sec rest',
            'calories': 40,
            'form_tip': 'Bar at upper chest, press overhead, lock out arms, bar behind ears at top.',
            'mistake': 'Leaning back excessively — engage core to keep spine neutral.'
        },
        {
            'name': 'Lateral Raise',
            'muscles': ['Side Deltoid'],
            'sets': 3, 'reps': '12-15 reps', 'rest': '60 sec rest',
            'calories': 22,
            'form_tip': 'Slight bend in elbows, raise arms to shoulder height, pinky slightly higher.',
            'mistake': 'Using momentum and swinging — use lighter weight and go slow.'
        }
    ],
    'arms': [
        {
            'name': 'Barbell Curl',
            'muscles': ['Biceps', 'Forearms'],
            'sets': 3, 'reps': '10-12 reps', 'rest': '60 sec rest',
            'calories': 25,
            'form_tip': 'Elbows pinned to sides, curl to shoulder height, squeeze at top.',
            'mistake': 'Swinging body to lift weight — reduce weight and keep torso still.'
        },
        {
            'name': 'Tricep Pushdown',
            'muscles': ['Triceps'],
            'sets': 3, 'reps': '12-15 reps', 'rest': '60 sec rest',
            'calories': 22,
            'form_tip': 'Elbows at sides, push rope down and apart, fully extend arms.',
            'mistake': 'Letting elbows flare out — keep them locked to your sides.'
        }
    ],
    'core': [
        {
            'name': 'Plank',
            'muscles': ['Core', 'Transverse Abdominis'],
            'sets': 3, 'reps': '45-60 sec', 'rest': '45 sec rest',
            'calories': 15,
            'form_tip': 'Forearms on floor, body straight line, squeeze glutes and abs.',
            'mistake': 'Letting hips sag or rise — keep a perfectly straight line.'
        },
        {
            'name': 'Cable Crunch',
            'muscles': ['Rectus Abdominis', 'Obliques'],
            'sets': 3, 'reps': '15-20 reps', 'rest': '45 sec rest',
            'calories': 18,
            'form_tip': 'Kneel facing cable, pull weight down by crunching abs, not pulling with arms.',
            'mistake': 'Using hip flexors to pull down — focus on contracting abs only.'
        }
    ],
    'cardio': [
        {
            'name': 'HIIT Treadmill',
            'muscles': ['Full Body', 'Cardiovascular System'],
            'sets': 8, 'reps': '30 sec sprint / 30 sec walk', 'rest': '30 sec rest',
            'calories': 120,
            'form_tip': 'Sprint at 80-90% max effort, walk at recovery pace between intervals.',
            'mistake': 'Not going hard enough on sprints — HIIT only works at high intensity.'
        },
        {
            'name': 'Jump Rope',
            'muscles': ['Calves', 'Shoulders', 'Cardiovascular System'],
            'sets': 5, 'reps': '2 min continuous', 'rest': '60 sec rest',
            'calories': 80,
            'form_tip': 'Stay on balls of feet, small jumps, wrists do the rotation not arms.',
            'mistake': 'Jumping too high — small efficient jumps conserve energy.'
        }
    ]
}

def generate_detailed_workout(goal, activity_level):
    # Generate a full weekly detailed workout plan based on goal
    goal_display = {
        'lose_weight': 'Lose Weight',
        'gain_muscle': 'Gain Muscle',
        'get_fit': 'Get Fit'
    }.get(goal, 'Get Fit')

    if goal == 'gain_muscle':
        weekly_sessions = 5
        session_duration = 60
        detailed_workout = {
            'Monday — Chest & Triceps': EXERCISES['chest'] + [EXERCISES['arms'][1]],
            'Tuesday — Back & Biceps': EXERCISES['back'] + [EXERCISES['arms'][0]],
            'Wednesday — Rest Day': 'rest',
            'Thursday — Legs': EXERCISES['legs'],
            'Friday — Shoulders & Arms': EXERCISES['shoulders'] + EXERCISES['arms'],
            'Saturday — Full Body & Core': [EXERCISES['back'][0]] + [EXERCISES['legs'][0]] + EXERCISES['core'],
            'Sunday — Rest Day': 'rest'
        }
    elif goal == 'lose_weight':
        weekly_sessions = 5
        session_duration = 45
        detailed_workout = {
            'Monday — Cardio & Core': EXERCISES['cardio'] + EXERCISES['core'],
            'Tuesday — Full Body Strength': [EXERCISES['legs'][0]] + [EXERCISES['chest'][0]] + [EXERCISES['back'][1]],
            'Wednesday — Rest Day': 'rest',
            'Thursday — HIIT & Arms': [EXERCISES['cardio'][0]] + EXERCISES['arms'],
            'Friday — Upper Body': EXERCISES['chest'] + EXERCISES['shoulders'],
            'Saturday — Cardio & Core': EXERCISES['cardio'] + EXERCISES['core'],
            'Sunday — Rest Day': 'rest'
        }
    else:  # get_fit
        weekly_sessions = 4
        session_duration = 50
        detailed_workout = {
            'Monday — Upper Body': EXERCISES['chest'] + EXERCISES['back'][:2],
            'Tuesday — Cardio': EXERCISES['cardio'],
            'Wednesday — Rest Day': 'rest',
            'Thursday — Lower Body': EXERCISES['legs'],
            'Friday — Full Body': [EXERCISES['shoulders'][0]] + EXERCISES['arms'] + EXERCISES['core'],
            'Saturday — Cardio & Core': EXERCISES['cardio'] + EXERCISES['core'],
            'Sunday — Rest Day': 'rest'
        }

    return {
        'goal_display': goal_display,
        'weekly_sessions': weekly_sessions,
        'session_duration': session_duration,
        'detailed_workout': detailed_workout
    }