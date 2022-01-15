from authz import db
from authz.model import User
from flask import request, abort
from authz.schema import UserSchema

class UserController:
    
    def create_user():
        if request.content_type != "application/json":
            abort(415)
        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())                     # Validate request data
        except:
            abort(400)
        """
        az user_schema ke sakhtim ta in abort 400 kare in 2ta if paein ro mikone
        """
        # data = request.get_json()
        # if len(data) != 2:
        #     abort(400)
        # if "username" not in data or "password" not in data:
        #     abort(400)
        if not data["username"] or not data["password"]:
            abort(400)
        # if type(data["username"]) is not str or type(data["password"]) is not str:
        #     abort(400)
        user = User.query.filter_by(username = data["username"]).first()   #hamishe sabet hast
        if user is not None:
            abort(409)
        user = User(username = data["username"], password = data["password"])
        db.session.add(user)
        db.session.commit()
        user_schema = UserSchema()
        return {
            "user" : user_schema.dump(user)
        }
        
        
    def get_users():
        pass
    
    def get_users(user_id):
        pass
    
    def update_user(user_id):
        pass
    
    def delete_user(user_id):
        pass

