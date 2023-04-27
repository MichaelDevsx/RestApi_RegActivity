from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class PlainWorkOutSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

class PlainRegisterActSchema(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.Date()
    time = fields.Date()
    distance = fields.Float(required=True)
    calories_burned = fields.Float(required=True)

class RegisterActSchema(PlainRegisterActSchema):
    workout_id = fields.Int(load_only=True)

class WorkOutSchema(PlainWorkOutSchema):
    users = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)
    registers = fields.List(fields.Nested(RegisterActSchema()), dump_only=True)

class UserSchema(PlainUserSchema):
    workouts = fields.List(fields.Nested(PlainWorkOutSchema()), dump_only=True)

class UserWorkoutSchema(Schema):
    message = fields.Str()
    user = fields.Nested(UserSchema)
    workout = fields.Nested(WorkOutSchema)