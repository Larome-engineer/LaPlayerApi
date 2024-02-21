from laplayer_api.services.user_service import get_token
from laplayer_api.utils.explorers import youtube_explorer


def explore(request: str, token: str) -> dict | None:
    if get_token(token=token) is None:
        return None
    else:
        return youtube_explorer(request=request)
