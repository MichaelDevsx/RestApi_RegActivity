from db import db

class WorkoutModel(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)

    
    registers = db.relationship("RegisterActModel", backref="registers", lazy="dynamic")

    users = db.relationship("UserModel", back_populates="workouts", secondary="users_workouts")