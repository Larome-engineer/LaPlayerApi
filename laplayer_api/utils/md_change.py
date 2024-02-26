from mutagen.id3 import ID3, APIC, TPE1, TIT2
from mutagen.mp3 import MP3, HeaderNotFoundError
from laplayer_api.data.config import logo_path


def md_changer(mp3_path, artist, title):
    try:
        music = MP3(mp3_path, ID3=ID3)
        with open(logo_path, 'rb') as album_art:
            music.tags.add(
                APIC(
                    encoding=3,
                    mime='image/jpeg',
                    type=3,
                    desc='Cover',
                    data=album_art.read()
                )
            )
            title.replace('—', '-').replace('^', '*').replace('#', '|').replace('.', '?').replace("'", "/")
            music.tags.add(TPE1(encoding=3, text=artist))
            music.tags.add(TIT2(encoding=3, text=title))
            music.save()

        print("SUCCESS ADDED METADATA")
    except HeaderNotFoundError as HNFE:
        print(HNFE)
