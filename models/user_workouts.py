from db import db

class UsersWorkoutsModel(db.Model):
    __tablename__ = 'users_workouts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))