import requests
from laplayer_api.data.variables import params, headers

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, headers=headers)
chart = response.json()['chartPositions']


def get_charts():
    top_chart = {}
    for track in chart:
        position = track['track']['chart']['position']
        title = track['track']['title']
        author = track['track']['artists'][0]['name']
        top_chart[position] = f"{position} | {author} - {title}"
    return top_chart
