from laplayer_api import db
from laplayer_api.models.models import MusicLinks


def add_music(music: MusicLinks):
    db.session.add(music)
    db.session.commit()


def get_music_path_by_link(link: str):
    return db.session.query(MusicLinks.music_path).filter(MusicLinks.music_link == link).first()
