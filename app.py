import os
from flask import Flask, jsonify
from flask_smorest import Api
from flask_migrate import Migrate

import models

from db import db

from resources.user import blp as UserBlueprint
from resources.workout import blp as WorkoutBlueprint
from resources.registeract import blp as RegisteractBlueprint

def create_app(db_url=None):
    app= Flask(__name__, instance_path=os.path.join(os.getcwd(), "instance"))
    app.config["API_TITLE"] = "RestApi of Activity"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "SecretKey"


    api.register_blueprint(UserBlueprint)
    api.register_blueprint(WorkoutBlueprint)
    api.register_blueprint(RegisteractBlueprint)

    return app