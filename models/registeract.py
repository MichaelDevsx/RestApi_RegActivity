from db import db
from sqlalchemy import DateTime, func, Column, Time

class RegisterActModel(db.Model):
    __tablename__ = "registers"

    id = db.Column(db.Integer, primary_key=True)
    createdat = db.Column(DateTime(timezone=True), server_default=func.now())
    time = db.Column(Time)
    distance = db.Column(db.Float)
    calories_burned = db.Column(db.Float)

    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"),nullable=False)
    workout_id = db.Column(db.Integer(), db.ForeignKey("workouts.id"),nullable=False)