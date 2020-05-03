import requests

from flask import current_app
from authlib.jose import JsonWebKey, JWK_ALGORITHMS


def get_jwk():
    r = requests.get(
        '{}/.well-known/jwks.json'.format(current_app.config['JWKS_URL']))
    key = r.json()['keys'][0]
    jwk = JsonWebKey(algorithms=JWK_ALGORITHMS)
    return jwk.loads(key)
