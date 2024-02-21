from laplayer_api.services.explore import explore
from laplayer_api.services.download import download
from laplayer_api import app, jsonify, request, send_file

BASE_URL = "/laplayerapi/v1"


@app.route(f'{BASE_URL}/search', methods=['GET'])
def get_links():
    if request.args.get("token") is None:
        return "403"
    else:
        return jsonify(
            explore(
                request=request.args.get("name"), token=request.args.get("token")
            )
        )


@app.route(f'{BASE_URL}/download', methods=['GET'])
def download_music():
    if request.args.get("token") is None:
        return "403"
    else:
        mp3_path = download(
            link=request.args.get("link"), token=request.args.get("token")
        )
        return send_file(mp3_path, mimetype='audio/mpeg')


if __name__ == "__main__":
    app.run()
