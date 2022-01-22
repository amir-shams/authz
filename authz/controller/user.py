from authz.schema import user
from authz import db
from authz.model import User
from flask import request, abort
from authz.schema import UserSchema

class UserController:
    
    def create_user():
        if request.content_type != "application/json":
            abort(415)           # bad media type
        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())                     # Validate request data
        except:
            abort(400)           # invalid request
        if not data["username"] or not data["password"]:
            abort(400)          # empty data
        user = User.query.filter_by(username = data["username"]).first()   #hamishe sabet hast   /// select a user
        if user is not None:
            abort(409)          # user is already registered
        try:
            user = User(username = data["username"], password = data["password"])          #create new user
        except:
            abort(500)                # database error
        db.session.add(user)          # add to database  session
        try:
            db.session.commit()       # database create query
        except:
            db.session.rollback()
            abort(500)               # database error    
        user_schema = UserSchema()
        return {
            "user" : user_schema.dump(user)
        }, 201
        
    def get_users():
        try:
            users = User.query.all()
        except:
            abort(500)          # database error
        users_schema = UserSchema(many = True)             #be manie list dorost kardane many = True
        return{
            "users": users_schema.dump(users)
        }, 200
    
    def get_user(user_id):
        try:
            user = User.query.get(user_id)
        except:
            abort(500)          # database error
        if user is None:
            abort(404)
        user_schema = UserSchema()
        return{
            "user": user_schema.dump(user)
        }, 200
        
    def update_user(user_id):
        if request.content_type != "application/json":
            abort(415)
        user_schema = UserSchema(only = ["password"])
        try:
            data = user_schema.load(request.get_json())               # validate request data
        except:
            abort(400)
        if not data["password"]:
            abort(400)
        try:
            user = User.query.get(user_id)                                # select the user
        except:
            abort(500)          #database error
        if user is None:
            abort(404)  
        user.password = data["password"]
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500)          #database error         
        user_schema = UserSchema()
        return{
            "user": user_schema.dump(user)
        }, 200
                  
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
        except:
            abort(500)
        if user is None:
            abort(404)
        db.session.delete(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500)          #database error
        return {}, 204

