from laplayer_api import db
from laplayer_api.models.models import Users


def add_user(user: Users):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception:
        return False


def get_token(token: str):
    return db.session.query(Users).filter(Users.user_api_token == token).first()


def get_token_by_tg_id(tg_id: str):
    return db.session.query(Users.user_api_token).filter(Users.user_tg_id == tg_id).first()
