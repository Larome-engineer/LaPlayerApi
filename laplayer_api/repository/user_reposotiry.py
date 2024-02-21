from laplayer_api import db
from laplayer_api.models.models import Users


def add_user(user: Users):
    db.session.add(user)
    db.session.commit()


def get_token(token: str):
    return db.session.query(Users).filter(Users.user_api_token == token).first()
