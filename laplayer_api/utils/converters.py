import os
from moviepy.editor import VideoFileClip
from laplayer_api.data.config import mp3_root, wav_root


def wav_to_mp3(wav):
    wav_path = f'{wav_root}{wav}'
    mp3_name = f"{wav}".replace('.wav', '.mp3')
    mp3_path = f"{mp3_root}{mp3_name}"

    if wav_path is None:
        return
    else:
        video = VideoFileClip(wav_path)

        audio = video.audio
        audio.write_audiofile(mp3_path)
        video.close(), audio.close()

        os.remove(wav_path)
        print("SUCCESS CONVERTED!")
        return mp3_path, mp3_name

# Any converters...
