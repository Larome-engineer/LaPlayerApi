from laplayer_api.utils.explorers import youtube_explorer
from laplayer_api.utils.downloaders import youtube_wav_downloader
from laplayer_api.services.user_service import get_token
from laplayer_api.utils.converters import wav_to_mp3
from laplayer_api.data.config import mp3_root
from laplayer_api.utils.md_change import md_changer
from laplayer_api.models.models import MusicLinks
from laplayer_api.repository.music_repository import add_music, get_music_path_by_link


def explore(request: str, token: str) -> dict | None:
    if get_token(token=token) is None:
        return None
    else:
        return youtube_explorer(request=request)


def download(link: str, token: str) -> str | None:
    if get_token(token=token) is None:
        return None
    else:
        path = __get_music(link)
        if path is None:
            download_data = youtube_wav_downloader(yt_link=link)
            wav = download_data[0]
            convert_mp3_data = wav_to_mp3(wav=wav)
            mp3 = convert_mp3_data[0]
            md_changer(
                mp3_path=mp3,
                artist=download_data[1].replace('—', '-').replace('^', '*').replace('#', '|').replace('.', '?').replace("'", "/"),
                title=download_data[2].replace('—', '-').replace('^', '*').replace('#', '|').replace('.', '?').replace("'", "/")
            )
            __create_music(music_path=convert_mp3_data[1], music_link=link)
        else:
            mp3 = mp3_root+path[0]
        return mp3


def __create_music(music_path: str, music_link: str):
    music = MusicLinks(music_path=music_path, music_link=music_link)
    add_music(music)


def __get_music(link: str):
    path = get_music_path_by_link(link=link)
    if path is None:
        return None
    else:
        return path
