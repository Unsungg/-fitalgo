import json

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
    # Smart rule-based fitness assistant
    data = request.get_json()
    message = data.get('message', '').lower()

    # Keyword-based intelligent responses
    if any(w in message for w in ['squat', 'leg', 'quads', 'glutes']):
        reply = "For squats: stand with feet shoulder-width apart, keep your chest up and back straight. Lower until thighs are parallel to the floor, then drive through your heels to stand. Aim for 3-4 sets of 8-12 reps. Keep knees aligned with toes throughout the movement."
    elif any(w in message for w in ['protein', 'muscle', 'gain']):
        reply = "For muscle gain, aim for 1.6-2.2g of protein per kg of bodyweight daily. Best sources: chicken breast (31g/100g), eggs (13g/100g), Greek yogurt (10g/100g), and tuna (29g/100g). Spread intake across 4-5 meals for optimal absorption."
    elif any(w in message for w in ['calorie', 'lose weight', 'fat', 'deficit']):
        reply = "For weight loss, create a 300-500 calorie daily deficit. Focus on high-volume, low-calorie foods like vegetables, lean proteins, and fruits. Avoid liquid calories and processed foods. Combine with cardio 3-4x per week for best results."
    elif any(w in message for w in ['cardio', 'running', 'cycling', 'hiit']):
        reply = "HIIT cardio is most effective for fat loss — try 30 seconds max effort, 30 seconds rest for 20 minutes. For endurance, steady-state cardio at 60-70% max heart rate works best. Aim for 150 minutes of moderate cardio per week minimum."
    elif any(w in message for w in ['bench', 'chest', 'push', 'pectoral']):
        reply = "For chest development, focus on: Bench Press (3x8-12), Incline Dumbbell Press (3x10), Cable Flyes (3x15). Keep shoulder blades retracted and maintain a slight arch in your lower back. Full range of motion is key for maximum muscle activation."
    elif any(w in message for w in ['back', 'pull', 'lat', 'row']):
        reply = "For a strong back: Deadlifts (4x5), Pull-ups (3x max), Barbell Rows (3x10), and Lat Pulldowns (3x12). Focus on pulling with your elbows, not your hands. Keep your core tight and avoid rounding your lower back."
    elif any(w in message for w in ['sleep', 'recovery', 'rest']):
        reply = "Sleep is crucial for muscle recovery — aim for 7-9 hours per night. During deep sleep, growth hormone is released which repairs muscle tissue. Avoid training the same muscle group 2 days in a row. Active recovery like walking or yoga on rest days is beneficial."
    elif any(w in message for w in ['supplement', 'creatine', 'whey', 'vitamin']):
        reply = "Key supplements worth considering: Creatine monohydrate (5g/day) for strength and power, Whey protein for convenient protein intake, Vitamin D3 for hormonal health, and Omega-3 for inflammation reduction. Always prioritize whole foods over supplements."
    elif any(w in message for w in ['water', 'hydration', 'drink']):
        reply = "Hydration is essential for performance — aim for 35-45ml per kg of bodyweight daily. During exercise, drink 200-300ml every 15-20 minutes. Signs of dehydration include dark urine, headaches, and decreased performance. Add electrolytes for sessions over 60 minutes."
    elif any(w in message for w in ['warm up', 'warmup', 'stretch', 'flexibility']):
        reply = "Always warm up for 5-10 minutes before training. Start with light cardio, then dynamic stretches (leg swings, arm circles, hip rotations). Save static stretching for after your workout when muscles are warm. A proper warm-up reduces injury risk by up to 50%."
    else:
        reply = "Great question! For personalized fitness advice, focus on these fundamentals: progressive overload in training, adequate protein intake (1.6-2g per kg bodyweight), quality sleep (7-9 hours), and consistency. Would you like specific advice on training, nutrition, or recovery?"

    return json.dumps({'reply': reply})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)