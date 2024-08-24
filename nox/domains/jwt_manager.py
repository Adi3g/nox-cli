from __future__ import annotations

import datetime
import json
from typing import Any

import jwt


class JWTManager:
    def __init__(self, secret: str, algorithm: str = 'HS256') -> None:
        self.secret = secret
        self.algorithm = algorithm

    def generate_token(
        self, payload: dict[str, Any],
        expires_in: int = 3600,
    ) -> str:
        """Generate a JWT token."""
        expiration = datetime.datetime.now() +\
            datetime.timedelta(seconds=expires_in)
        payload.update({'exp': expiration})
        token = jwt.encode(payload, self.secret, algorithm=self.algorithm)
        return token

    def verify_token(self, token: str) -> dict[str, Any]:
        """Verify a JWT token."""
        try:
            decoded = jwt.decode(
                token, self.secret,
                algorithms=[self.algorithm],
            )
            return decoded
        except jwt.ExpiredSignatureError:
            raise ValueError('Token has expired')
        except jwt.InvalidTokenError:
            raise ValueError('Invalid token')

    @staticmethod
    def load_claims(claims_file: str) -> dict[str, Any]:
        """Load claims from a JSON file."""
        with open(claims_file) as file:
            return json.load(file)
