from flask import g, request
from functools import wraps
from authlib.jose import jwt
from .get_jwk import get_jwk


def get_subject(f):
    @wraps(f)
    def subject(*args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1]
        jwk = get_jwk()
        sub = jwt.decode(token, jwk)['sub']
        g.current_user_id = sub
        return f(*args, **kwargs)
    return subject
