from dao.movie_dao import MovieDao

movie_dao = MovieDao()

ROWS_LIMIT = 5
PAGE_SIZE = 10
class MovieService:
    def get_movies_list(self):
        movies = movie_dao.get_movies()
        return {
                  "status": "success",
                  "data": movies
                }, 200

    def get_series_list(self):
        series = movie_dao.get_series()
        return {
            "status": "success",
            "data": series
        }, 200

    def get_top_movies_list(self):
        movies = movie_dao.get_top_movies(ROWS_LIMIT)
        return {
            "status": "success",
            "data": movies
        }, 200

    def get_top_series_list(self):
        series = movie_dao.get_top_series(ROWS_LIMIT)
        return {
            "status": "success",
            "data": series
        }, 200

    def get_movies_page(self, page):
        movies = movie_dao.get_movies_page(page, PAGE_SIZE)
        return {
            "status": "success",
            "data": movies
        }, 200

    def get_series_page(self, page):
        series = movie_dao.get_series_page(page, PAGE_SIZE)
        return {
            "status": "success",
            "data": series
        }, 200

    def add_serie_to_favorite(self, serie_id, user_id):
        movie_dao.add_movie_serie_favorite(user_id, serie_id=serie_id)
        return {
            "status": "success",
            "message": "Serie added to favorite list.",
        }, 200

    def add_movie_to_favorite(self, movie_id, user_id):
        movie_dao.add_movie_serie_favorite(user_id, movie_id=movie_id)
        return {
            "status": "success",
            "message": "Movie added to favorite list.",
        }, 200

    def remove_movie_from_favorite(self, movie_id, user_id):
        movie_dao.remove_movie_serie_favorite(user_id, movie_id=movie_id)
        return {
            "status": "success",
            "message": "Movie removed from favorite list.",
        }, 200

    def remove_serie_from_favorite(self, serie_id, user_id):
        movie_dao.remove_movie_serie_favorite(user_id, serie_id=serie_id)
        return {
            "status": "success",
            "message": "Serie removed from favorite list.",
        }, 200

    def get_favorites_movies(self):
        movies = movie_dao.get_favorites_movies()
        return {
            "status": "success",
            "data": movies
        }, 200

    def get_favorites_series(self):
        series = movie_dao.get_favorites_series()
        return {
            "status": "success",
            "data": series
        }, 200

    def look_for_movies(self, keyword):
        movies = movie_dao.look_for_movies(keyword)
        return {
            "status": "success",
            "data": movies
        }, 200

    def look_for_series(self, keyword):
        series = movie_dao.look_for_series(keyword)
        return {
            "status": "success",
            "data": series
        }, 200

    def get_movie_details(self, movie_id):
        return {
            "status": "success",
            "data": movie_dao.get_movie(movie_id)
        }, 200

    def get_serie_details(self, serie_id):
        return {
            "status": "success",
            "data": movie_dao.get_serie(serie_id)
        }, 200

    def get_movie_trailer(self, movie_id):
        movie = movie_dao.get_movie(movie_id)
        return {
            "status": "success",
            "trailer_url": movie.get('trailer')
        }, 200

    def get_serie_trailer(self, serie_id):
        serie = movie_dao.get_serie(serie_id)
        return {
            "status": "success",
            "trailer_url": serie.ge('trailer')
        }, 200
