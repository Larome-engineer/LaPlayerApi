from youtubesearchpython import VideosSearch


def youtube_explorer(request: str) -> dict:
    you_tube_links = {}

    try:
        for link in VideosSearch(request, limit=6).result()['result']:
            if link['duration'].count(":") > 1 or int(link['duration'].split(":")[0]) > 7:
                continue
            you_tube_links[f"{link['duration']} | {link['title']}"] = link['link']

        return you_tube_links
    except AttributeError:
        return you_tube_links


def spotify_explorer(request: str):
    pass


def yandex_explorer(request: str):
    pass
