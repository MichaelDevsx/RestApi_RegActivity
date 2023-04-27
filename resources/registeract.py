from flask.views import MethodView
from flask_smorest import Blueprint,abort
from flask_jwt_extended import get_jwt_identity, get_jwt, jwt_required
from passlib.hash import pbkdf2_sha256

from db import db
from models import RegisterActModel
from schemas import PlainRegisterActSchema, RegisterActSchema,UserWorkoutSchema

blp = Blueprint("Registeracts", "registeracts", description="Operation on Registeracts")

@blp.route("/registeracts")
class RegisterWorkout(MethodView):
    @blp.arguments(RegisterActSchema)
    def post(self, workout_data):
        workout = RegisterActModel(**workout_data)

        db.session.add(workout)
        db.session.commit()
        return {"message":"Workout was successfully registered"},201

@blp.route("/registeracts_all")
class WorkoutsList(MethodView):
    @blp.response(200, RegisterActSchema(many=True))
    def get(self):
        workout = RegisterActModel.query.all()
        return workout
    
@blp.route("/registeracts/<int:workout_id>")
class GetWorkout(MethodView):
    @blp.response(200, PlainRegisterActSchema)
    def get(self, workout_id):
        register = RegisterActModel.query.get(workout_id)

        return register
    
    def delete(self, workout_id):
        register = RegisterActModel.query.get(workout_id)

        db.session.delete(register)
        db.session.commit()

        return {"message":"Workout was deleted"}