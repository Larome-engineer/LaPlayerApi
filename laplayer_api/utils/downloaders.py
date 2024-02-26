import validators
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from laplayer_api.data.config import wav_root
from laplayer_api.utils.is_valid import is_valid
from laplayer_api.utils.filter import filter_name


def youtube_wav_downloader(yt_link: str):
    try:
        if validators.url(yt_link) and is_valid(yt_link):
            ytl = YouTube(yt_link)
            music_data = filter_name(ytl)

            author = music_data[0]
            name = music_data[1]

            wav = f'{author} — {name}.wav'

            ytl.streams.get_highest_resolution().download(output_path=wav_root, filename=wav)
            return wav, author, name

    except (RegexMatchError, TypeError):
        return None


def spotify_downloader(request):
    pass


def yandex_downloader(request):
    pass
