from laplayer_api.utils.downloaders import youtube_wav_downloader
from user_service import get_token
from laplayer_api.utils.converters import wav_to_mp3
from laplayer_api.utils.md_change import md_changer


def download(link: str, token: str) -> str | None:
    if get_token(token=token) is None:
        return None
    else:
        download_data = youtube_wav_downloader(yt_link=link)
        wav = download_data[0]
        mp3 = wav_to_mp3(wav=wav)
        md_changer(
            mp3_path=mp3,
            artist=download_data[1],
            title=download_data[2]
        )
        return mp3



