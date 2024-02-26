import hashlib
from laplayer_api.models.models import Users
from laplayer_api.repository.user_reposotiry import add_user, get_token, get_token_by_tg_id


def create_user(name, email, password, tg_id):
    user = Users(
        username=name,
        user_email=email,
        user_password=__hash_password(password=password),
        user_api_token=__generate_api_token(name, email, password, tg_id)
    )

    registration = add_user(user)

    if registration is True:
        return 200
    else:
        return 404


def check_token(api_token: str):
    user = get_token(token=api_token)
    if user is None:
        return 404
    else:
        return 200


def token_by_tg_id(tg_id: int):
    token = get_token_by_tg_id(tg_id=tg_id)
    if token is None:
        return 404
    else:
        return token


def __generate_api_token(name: str, email: str, password: str, tg_id: str):
    alg_sha256 = hashlib.new('sha256')
    data = name + email + password + tg_id
    alg_sha256.update(data.encode())
    return alg_sha256.hexdigest()


def __hash_password(password):
    alg_sha256 = hashlib.new('sha256')
    data = password
    alg_sha256.update(data.encode())
    return alg_sha256.hexdigest()
