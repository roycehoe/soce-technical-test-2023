from datetime import datetime, timedelta

from jose import JWTError, jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 1337
ALGORITHM = "HS256"  # or whatever algo of your choosing
SECRET_KEY = "some secret goes here"  # store this in an .env file


class InvalidAuthenticationTokenError(Exception):
    pass


class MissingAuthenticationTokenError(Exception):
    pass


def create_access_token(data: dict) -> str:
    """Converts a dictionary to a JWT access token
    :param data: A dictionary containing data to encode into a JWT access token
    :type data: dict
    :returns: A JWT token based on param data
    :rtype: str
    """

    raw_token_data = data.copy()
    token_expiry_time = datetime.utcnow() + timedelta(
        minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    raw_token_data.update({"exp": token_expiry_time})
    encoded_jwt = jwt.encode(raw_token_data, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def authenticate_token(token: str) -> None:
    """Authenticates a JWT token
    :param token: A JWT token
    :type token: str
    :returns: None
    :rtype: None
    :raises JWTError: If token decoding fails
    :raises InvalidAuthenticationTokenError: If token does not have a "username" key
    """

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise JWTError

    try:
        payload["username"]
    except KeyError:
        raise InvalidAuthenticationTokenError


def get_token_data(token: str, key: str) -> str:
    """Decodes and gets user_id stored within a JWT token
    :param token: A JWT token
    :type token: str
    :param key: Data to obtain from token
    :type token: str
    returns: value with corresponding key, stored within a JWT token
    :rtype: str
    :raises JWTError: If token decoding fails
    :raises MissingAuthenticationTokenError: If no authentication token is given
    :raises InvalidAuthenticationTokenError: If token does not have a given key
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise JWTError
    except AttributeError:
        raise MissingAuthenticationTokenError

    try:
        data: str = payload[key]
    except KeyError:
        raise InvalidAuthenticationTokenError

    return data
