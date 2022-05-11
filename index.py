from flask import Flask, render_template,  jsonify
from flask_caching import Cache
from flask_cors import CORS
from lib.helpers import *

config = {
    "DEBUG": False,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 900
}

app = Flask(__name__, template_folder='template', static_folder='static')
CORS(app)
app.config.from_mapping(config)
cache = Cache(app)
helpersAPI = HelpersAPI()


@app.route("/details/<id>", methods=['GET'])
def details(id):
    get_detail_info_movie = helpersAPI.info_movie(movie_id=id)

    return render_template(
        'details.html',
        get_detail_info_movie=get_detail_info_movie,
        movie_id=id
    )


@app.route('/', methods=['GET'])
@cache.cached(timeout=900)
def index():
    get_detail_info_movie = helpersAPI.get_detail_info_movie()
    get_coming_soon_movie = helpersAPI.get_coming_soon_movies()
    get_currently_playing = helpersAPI.get_currently_playing_movies()
    return render_template(
        'index.html',
        coming_soon_movie=get_coming_soon_movie,
        currently_playing=get_currently_playing,
        get_detail_info_movie=get_detail_info_movie
    )


@app.route("/book/<id>", methods=['GET'])
def book(id):
    get_detail_info_movie = helpersAPI.info_movie(movie_id=id)
    return render_template(
        'book.html',
        movie_id=id,
        get_detail_info_movie=get_detail_info_movie
    )


@app.route("/food", methods=['GET'])
def food():
    return render_template('food.html')


@app.route("/food/<id>", methods=['GET'])
def food_detail(id):
    get_food = helpersAPI.get_food(theater_id=id)
    return render_template(
        'food_detail.html',
        get_food=get_food
    )


# Ajax Request Route


@app.route("/getTheaters/<id>", methods=['GET'])
def getTheaters(id):
    get_theaters = helpersAPI.getTheaters(city_id=id)
    return get_theaters


@app.route('/getCityId', methods=['GET'])
def getCityId():
    get_city_ids = helpersAPI.get_city_id()
    return jsonify(get_city_ids)


@app.route('/getSchedule/<id>/<movieId>', methods=['GET'])
def get_schdule(id, movieId):
    print(helpersAPI.get_schedule_movie(theater_id=id, movie_id=movieId))
    return jsonify(helpersAPI.get_schedule_movie(theater_id=id, movie_id=movieId))


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
