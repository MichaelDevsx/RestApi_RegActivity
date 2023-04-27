from flask.views import MethodView
from flask_smorest import Blueprint,abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt, jwt_required
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import UserModel
from models import WorkoutModel
from schemas import UserSchema, PlainUserSchema


blp = Blueprint("Users","users", description="Operation on Users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(PlainUserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.email == user_data["email"]).first():
            abort(409, message="A user with that email already exists")
        
        user = UserModel(
            name = user_data["name"],
            email = user_data["email"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()

        return {"message":"User registration successful"},201
    
@blp.route("/users")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        user = UserModel.query.all()
        return user
    
@blp.route("/user/<int:user_id>")
class GetUser(MethodView):
    @blp.response(200, PlainUserSchema)
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        return user
    
    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        else:
            return {"message":"Error deleting user"}
        
@blp.route("/users/<int:user_id>/workouts/<int:workout_id>")
class LinkUserToWorkout(MethodView):
    @blp.response(200, UserSchema)
    def post(self, user_id, workout_id):
        user = UserModel.query.get(user_id)
        workout = WorkoutModel.query.get(workout_id)

        user.workouts.append(workout)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return workout