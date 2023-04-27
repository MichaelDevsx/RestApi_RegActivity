from flask.views import MethodView
from flask_smorest import Blueprint,abort
from flask_jwt_extended import get_jwt_identity, get_jwt, jwt_required

from db import db
from models import WorkoutModel
from schemas import PlainWorkOutSchema, WorkOutSchema

blp = Blueprint("Workouts","workouts", description="Operation on Workouts")

@blp.route("/create-workout")
class Workout(MethodView):
    @blp.arguments(PlainWorkOutSchema)
    @blp.response(200, WorkOutSchema)
    def post(self, workout_data):
        workout = WorkoutModel(**workout_data)

        db.session.add(workout)
        db.session.commit()
        return workout
    
@blp.route("/workouts-category")
class WorkoutsCatList(MethodView):
    @blp.response(200, WorkOutSchema(many=True))
    def get(self):
        workouts = WorkoutModel.query.all()
        return workouts

@blp.route("/workout/<int:workout_id>")
class GetWorkout(MethodView):
    @blp.response(200, WorkOutSchema)
    def get(self,workout_id):
        workout = WorkoutModel.query.get(workout_id)
        if workout is not None:
            return workout
        else:
            abort(400, message="Workout not found")
    
    def delete(self,workout_id):
        workout = WorkoutModel.query.get(workout_id)
        if workout is not None:
            db.session.delete(workout)
            db.session.commit()
            return {"message":"Workout deleted successfully"}
        else:
            abort(500, message = "Error deleting the workout")
