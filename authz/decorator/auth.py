from functools import wraps
from flask import abort, request
from jwt import decode
# from jwt import JWT
from authz.config import Config
from authz.rule import ControllerRule


def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt_token = request.headers.get("X-auth-token")
        if jwt_token is None:
            abort(401)   #jwt_token is not found
        try:
            data = decode(jwt_token, Config.SECRET, algorithms=[Config.JWT_ALGO])
        except:
            abort(401)
        controller_rule = ControllerRule.get_controller_roles(f.__name__)
        if data["user"]["role"] in controller_rule:
            return f(*args, **kwargs)
        elif data["user"]["role"] == "member" and "member: user_id" in controller_rule:
            user_id = args[f.__code__.co_varnames.index("user_id")]
            if data["user"]["user_id"] == user_id:
                return f(*args, **kwargs)
            else:
                abort(403)
        else:
            abort(403)
    return wrapper
