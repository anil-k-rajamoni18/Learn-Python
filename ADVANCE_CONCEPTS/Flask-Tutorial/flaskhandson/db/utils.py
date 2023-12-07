import hashlib
def json_helper(data) -> dict:
    return {
        'username': data['username'],
        'password': encrypt_password(data['password']),
        'email': data['email']
    }


def encrypt_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(rawPassword, hashPassword) -> bool:
    return encrypt_password(rawPassword) == hashPassword