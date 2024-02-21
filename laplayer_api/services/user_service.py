import hashlib
from laplayer_api.models.models import Users
from laplayer_api.repository.user_reposotiry import add_user, get_token, get_token_by_username


def create_user(name, email, password):
    token = __generate_api_token(name, email, password)
    pwd = __hash_password(password=password)
    user = Users(username=name, user_email=email, user_password=pwd, user_api_token=token)
    add_user(user)


def check_token(api_token):
    user = get_token(token=api_token)
    if user is None:
        return None
    else:
        return "SUCCESS"


def token_by_username(username):
    token = get_token_by_username(username=username)
    if token is None:
        return None
    else:
        return token


def __generate_api_token(name: str, email: str, password: str):
    alg_sha256 = hashlib.new('sha256')
    data = name + email + password
    alg_sha256.update(data.encode())
    return alg_sha256.hexdigest()


def __hash_password(password):
    alg_sha256 = hashlib.new('sha256')
    data = password
    alg_sha256.update(data.encode())
    return alg_sha256.hexdigest()
