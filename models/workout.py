from db import db

class WorkoutModel(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)

    registeract = db.relationship("RegisterActModel", backref="workouts", lazy="dynamic")