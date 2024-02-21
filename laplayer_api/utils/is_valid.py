import urllib.request


def is_valid(link):
    if urllib.request.urlopen(link):
        return True

