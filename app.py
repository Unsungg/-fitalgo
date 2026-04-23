import json
from nutrition_data import get_meal_suggestions, get_meal_recipes
from supplement_data import get_supplement_recommendations
from workout_data import generate_detailed_workout
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Progress
from engine import generate_full_plan, update_plan_based_on_progress

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitalgo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'fitalgo-secret-key'

db.init_app(app)

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        existing_user = User.query.filter_by(email=request.form['email']).first()
        if existing_user:
            flash('Email already registered. Please login.', 'danger')
            return redirect(url_for('login'))
        hashed_password = generate_password_hash(request.form['password'])
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('setup'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/setup', methods=['GET', 'POST'])
@login_required
def setup():
    if request.method == 'POST':
        current_user.age = int(request.form['age'])
        current_user.height = float(request.form['height'])
        current_user.weight = float(request.form['weight'])
        current_user.gender = request.form['gender']
        current_user.goal = request.form['goal']
        current_user.activity_level = request.form['activity_level']
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('setup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    fitness_plan = generate_full_plan(current_user)
    progress_history = Progress.query.filter_by(user_id=current_user.id).order_by(Progress.date).all()
    return render_template('plan.html', user=current_user, plan=fitness_plan, progress_history=progress_history)

@app.route('/log_progress', methods=['POST'])
@login_required
def log_progress():
    entry = Progress(
        user_id=current_user.id,
        weight=float(request.form['weight']),
        notes=request.form.get('notes', '')
    )
    db.session.add(entry)
    db.session.commit()
    all_entries = Progress.query.filter_by(user_id=current_user.id).order_by(Progress.date).all()
    updated_plan = update_plan_based_on_progress(current_user, all_entries)
    db.session.commit()
    progress_history = Progress.query.filter_by(user_id=current_user.id).order_by(Progress.date).all()
    return render_template('plan.html', user=current_user, plan=updated_plan, progress_history=progress_history)
@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat_api():
    # Get user message
    data = request.get_json()
    user_message = data.get('message', '')

    try:
        import ollama
        # Send message to local Ollama AI
        response = ollama.chat(
            model='llama3.2',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a professional fitness and nutrition coach named Fitalgo AI. Answer only fitness, nutrition, and health related questions. Keep answers concise and practical (max 3-4 sentences). If the question is not related to fitness or health, politely redirect.'
                },
                {
                    'role': 'user',
                    'content': user_message
                }
            ]
        )
        reply = response['message']['content']
    except Exception as e:
        # Fallback to rule-based responses if Ollama is not available
        reply = get_fitness_response(user_message)

    return json.dumps({'reply': reply})

def get_fitness_response(message):
    # Rule-based fallback responses
    message = message.lower()
    if any(w in message for w in ['squat', 'leg', 'quads', 'glutes']):
        return "For squats: stand with feet shoulder-width apart, keep your chest up and back straight. Lower until thighs are parallel to the floor, then drive through your heels to stand. Aim for 3-4 sets of 8-12 reps."
    elif any(w in message for w in ['protein', 'gain']):
        return "For muscle gain, aim for 1.6-2.2g of protein per kg of bodyweight daily. Best sources: chicken breast (31g/100g), eggs (13g/100g), Greek yogurt (10g/100g), and tuna (29g/100g)."
    elif any(w in message for w in ['calorie', 'lose weight', 'fat', 'deficit']):
        return "For weight loss, create a 300-500 calorie daily deficit. Focus on high-volume, low-calorie foods like vegetables, lean proteins, and fruits. Combine with cardio 3-4x per week for best results."
    elif any(w in message for w in ['cardio', 'running', 'cycling', 'hiit']):
        return "HIIT cardio is most effective for fat loss — try 30 seconds max effort, 30 seconds rest for 20 minutes. Aim for 150 minutes of moderate cardio per week minimum."
    elif any(w in message for w in ['bench', 'chest', 'push', 'pectoral']):
        return "For chest development: Bench Press (3x8-12), Incline Dumbbell Press (3x10), Cable Flyes (3x15). Keep shoulder blades retracted and maintain full range of motion."
    elif any(w in message for w in ['back', 'pull', 'lat', 'row']):
        return "For a strong back: Deadlifts (4x5), Pull-ups (3x max), Barbell Rows (3x10). Focus on pulling with your elbows, not your hands."
    elif any(w in message for w in ['sleep', 'recovery', 'rest']):
        return "Sleep is crucial for muscle recovery — aim for 7-9 hours per night. Avoid training the same muscle group 2 days in a row."
    elif any(w in message for w in ['supplement', 'creatine', 'whey']):
        return "Key supplements: Creatine monohydrate (5g/day) for strength, Whey protein for convenient intake, Vitamin D3 for hormonal health, Omega-3 for inflammation reduction."
    else:
        return "Great question! Focus on these fundamentals: progressive overload in training, adequate protein intake (1.6-2g per kg bodyweight), quality sleep (7-9 hours), and consistency."
@app.route('/workout')
@login_required
def workout():
    # Generate detailed workout plan for current user
    detailed_plan = generate_detailed_workout(current_user.goal, current_user.activity_level)
    return render_template('workout.html', plan=detailed_plan)
@app.route('/timer')
@login_required
def timer():
    # Get today's exercises for the timer
    from workout_data import generate_detailed_workout
    detailed_plan = generate_detailed_workout(current_user.goal, current_user.activity_level)
    
    # Get first non-rest day exercises
    exercises = []
    for day, day_exercises in detailed_plan['detailed_workout'].items():
        if day_exercises != 'rest':
            exercises = day_exercises
            break
    
    return render_template('timer.html', exercises=exercises)
@app.route('/supplements')
@login_required
def supplements():
    # Get personalized supplement recommendations
    supp_data = get_supplement_recommendations(current_user.goal)
    goal_display = {
        'lose_weight': 'Lose Weight',
        'gain_muscle': 'Gain Muscle',
        'get_fit': 'Get Fit'
    }.get(current_user.goal, 'Get Fit')
    return render_template('supplements.html', supplements=supp_data, goal_display=goal_display)

@app.route('/recipes')
@login_required
def recipes():
    # Get meal recipes based on user goal
    meal_recipes = get_meal_recipes(current_user.goal)
    return render_template('recipes.html', recipes=meal_recipes)

@app.route('/set_language/<lang>')
def set_language(lang):
    # Store language preference in session
    from flask import session
    session['language'] = lang
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)