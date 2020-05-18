import datetime

from flask import request, abort, current_app
from functools import wraps
from authlib.jose import jwt
from .get_jwk import get_jwk


def authorise(f):
    @wraps(f)
    def check(*args, **kwargs):
        try:
            token = request.headers.get('Authorization').split(' ')[1]
            jwk = get_jwk()

            claims_options = {
                'aud': {
                    'essential': True,
                    'values': ['{}'.format(current_app.config['JWT_AUDIENCE'])]
                },
                'iss': {
                    'essential': True,
                    'values': ['{}'.format(current_app.config['JWT_ISSUER'])]
                },
                'sub': {
                    'essential': True
                }
            }

            claims = jwt.decode(token, jwk, claims_options=claims_options)
            claims.validate(
                now=datetime.datetime.now().timestamp(),
                leeway=current_app.config['JWT_LEEWAY'])
        except Exception:
            abort(401)
        return f(*args, **kwargs)
    return check
