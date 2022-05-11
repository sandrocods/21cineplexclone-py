import requests
from os.path import exists


class HelpersAPI:
    def __init__(self):
        self.endpoint = "https://cinema-21-scrapper.vercel.app/"

    def get_endpoint(self):
        return self.endpoint

    def make_request(self, query):
        try:
            response = requests.get(
                url=self.get_endpoint() + query,
            )
            if response.status_code == 200:
                if response.json is not None:
                    return response.json()
                else:
                    return None
        except Exception as e:
            print(e)
            return None

    def get_coming_soon_movies(self):
        return self.make_request("/getComingSoon")

    def get_currently_playing_movies(self):
        return self.make_request("/getCurrentlyPlaying")

    def get_detail_info_movie(self):
        currentlyPlaying = self.make_request("/getCurrentlyPlaying")
        if currentlyPlaying is not None:
            for movie in currentlyPlaying:
                movie["detail"] = self.make_request("getMovies/{movie_id}".format(movie_id=movie["movieId"]))
            return currentlyPlaying
        else:
            return None

    def info_movie(self, movie_id):
        getVideo = self.get_movieId(movie_id=movie_id)

        # Can't Run at Vercel.app
        if exists("./static/{movie_id}.mp4".format(movie_id=movie_id)):
            pass
        else:

            requests_download = requests.get(
                url=getVideo["info"]["trailer"],
                allow_redirects=True
            )
            open('./static/{movie_id}.mp4'.format(movie_id=movie_id), 'wb').write(requests_download.content)

        return getVideo

    def get_movieId(self, movie_id):
        return self.make_request("getMovies/{movie_id}".format(movie_id=movie_id))

    def get_city_id(self):
        return self.make_request("getCityId")

    def getTheaters(self, city_id):
        return self.make_request("getTheaters/{city_id}".format(city_id=city_id))

    def get_schedule_theater(self, theater_id):
        return self.make_request("getSchedule/{theater_id}".format(theater_id=theater_id))

    def get_schedule_movie(self, theater_id, movie_id):
        get_schedule_theater = self.get_schedule_theater(theater_id=theater_id)
        for i in range(len(get_schedule_theater['data'])):
            movie_ids = get_schedule_theater['data'][i]['image'].split("/")[-1].split(".")[0]
            if movie_ids == movie_id:
                return {
                    "data": get_schedule_theater['data'][i],
                    'cinema_info': {
                        'name': get_schedule_theater['cinemaName'],
                        'address': get_schedule_theater['address'],
                        'contact': get_schedule_theater['contact'],

                    }
                }
        return None

    def get_food(self, theater_id):
        return self.make_request("getFoodsBeverages/{theater_id}".format(theater_id=theater_id))