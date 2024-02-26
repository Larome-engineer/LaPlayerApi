from laplayer_api import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_tg_id = db.Column(db.String(10), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    user_email = db.Column(db.String(70), nullable=False, unique=True)
    user_password = db.Column(db.String(255), nullable=False)
    user_api_token = db.Column(db.String(70), nullable=False, unique=True)

    def __init__(self, username, user_tg_id, user_email, user_password, user_api_token):
        self.username = username.strip()
        self.user_tg_id = user_tg_id
        self.user_email = user_email.strip()
        self.user_password = user_password.strip()
        self.user_api_token = user_api_token


class MusicLinks(db.Model):
    music_id = db.Column(db.Integer, primary_key=True, nullable=False)
    music_path = db.Column(db.String(100), nullable=False, unique=True)
    music_link = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, music_path, music_link):
        self.music_path = music_path
        self.music_link = music_link
