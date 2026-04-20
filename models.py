from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Main table storing user physical data and goals
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)   # in cm
    weight = db.Column(db.Float, nullable=False)   # in kg
    gender = db.Column(db.String(10), nullable=False)
    goal = db.Column(db.String(50), nullable=False)
    # goal options: 'lose_weight', 'gain_muscle', 'get_fit'
    activity_level = db.Column(db.String(50), nullable=False)
    # activity levels: 'sedentary', 'lightly_active', 'moderate', 'active', 'very_active'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # One user can have multiple progress entries
    progress = db.relationship('Progress', backref='user', lazy=True)

# Table for tracking weekly weight progress
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    weight = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String(300))