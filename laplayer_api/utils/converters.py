import os
from moviepy.editor import VideoFileClip
from laplayer_api.data.variables import mp3_root, wav_root


def wav_to_mp3(wav):
    wav_path = f'{wav_root}{wav}'
    mp3_path = f"{mp3_root}{wav}".replace('.wav', '.mp3')
    if wav_path is None:
        return
    else:
        video = VideoFileClip(wav_path)

        audio = video.audio
        audio.write_audiofile(mp3_path)
        video.close(), audio.close()

        os.remove(wav_path)
        print("SUCCESS CONVERTED!")
        return mp3_path

# Any converters...
