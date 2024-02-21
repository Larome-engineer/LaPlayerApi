from laplayer_api.utils.explorers import youtube_explorer
from user_service import get_token


def explore(request: str, token: str) -> dict | None:
    if get_token(token=token) is None:
        return None
    else:
        return youtube_explorer(request=request)
