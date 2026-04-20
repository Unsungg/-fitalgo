from flask import Flask, render_template, request
from models import db, User, Progress
from engine import generate_full_plan, update_plan_based_on_progress

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitalgo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'fitalgo-secret-key'

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plan', methods=['POST'])
def plan():
    user = User(
        name=request.form['name'],
        age=int(request.form['age']),
        height=float(request.form['height']),
        weight=float(request.form['weight']),
        gender=request.form['gender'],
        goal=request.form['goal'],
        activity_level=request.form['activity_level']
    )
    db.session.add(user)
    db.session.commit()

    fitness_plan = generate_full_plan(user)
    progress_history = Progress.query.filter_by(user_id=user.id).all()

    return render_template('plan.html', user=user, plan=fitness_plan, progress_history=progress_history)


@app.route('/log_progress', methods=['POST'])
def log_progress():
    user_id = int(request.form['user_id'])
    entry = Progress(
        user_id=user_id,
        weight=float(request.form['weight']),
        notes=request.form.get('notes', '')
    )
    db.session.add(entry)
    db.session.commit()

    user = User.query.get(user_id)
    all_entries = Progress.query.filter_by(user_id=user_id).order_by(Progress.date).all()
    updated_plan = update_plan_based_on_progress(user, all_entries)
    progress_history = Progress.query.filter_by(user_id=user_id).order_by(Progress.date).all()

    return render_template('plan.html', user=user, plan=updated_plan, progress_history=progress_history)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)