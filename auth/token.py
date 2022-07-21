from datetime import datetime, timedelta
from jose import JWTError, jwt
from ninja.errors import HttpError

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 24*60


def create_access_token(data: dict):
    """
    Crea un token de acceso para un usuario que expira en 24*60 minutos (1 día)

    Args:
        data (dict): [description]

    Returns:
        [type]: [description]
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HttpError(404, "Invalid Credentials")       
        return email
    except JWTError:
        raise HttpError(404, "JWT ERROR")
