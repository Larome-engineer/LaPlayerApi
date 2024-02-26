from laplayer_api.data.config import BASE_URL
from laplayer_api import app, jsonify, request, send_file
from laplayer_api.services.music_service import download, explore
from laplayer_api.services.user_service import create_user, check_token, token_by_tg_id


@app.route(f'{BASE_URL}/search', methods=['GET'])
def get_links():
    if request.args.get("token") is None:
        return jsonify(None)
    else:
        return jsonify(
            explore(
                request=request.args.get("name"), token=request.args.get("token")
            )
        )


@app.route(f'{BASE_URL}/download', methods=['GET'])
def download_music():
    if request.args.get("token") is None:
        return jsonify(None)
    else:
        mp3_path = download(
            link=request.args.get("link"), token=request.args.get("token")
        )
        if mp3_path is None:
            return jsonify(None)

        return send_file(mp3_path, mimetype='audio/mpeg')


@app.route(f'{BASE_URL}/register', methods=['POST'])
def verify_user():
    user_data = request.get_json()
    try:
        res = create_user(
            name=user_data["username"],
            email=user_data["email"],
            password=user_data["password"],
            tg_id=user_data["tg_id"]
        )
        return jsonify(res)
    except KeyError as e:
        return jsonify(f"Отсутствуют параметры: {' '.join(list(e.args))}")


@app.route(f'{BASE_URL}/checkToken', methods=['GET'])
def token():
    return jsonify(check_token(request.args.get("token")))


@app.route(f'{BASE_URL}/getToken', methods=['GET'])
def get_token():
    return jsonify(token_by_tg_id(request.args.get("tg_id")))


if __name__ == "__main__":
    app.run()
