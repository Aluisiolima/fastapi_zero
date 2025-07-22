from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

pwd_context: PasswordHash = PasswordHash((Argon2Hasher(),))


def hash_password(password: str) -> str:
    try:
        return pwd_context.hash(password)
    except Exception as e:
        print(e)


def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password=password, hash=hash)
