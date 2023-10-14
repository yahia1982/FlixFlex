from flask import Blueprint
from flask_pydantic import validate

from services.movie_service import MovieService

movie_bp = Blueprint("movie_bp", __name__)

movie_service = MovieService()


@movie_bp.route('/movies', methods=['GET'])
def get_movies_list():
    return movie_service.get_movies_list()


@movie_bp.route('/series', methods=['GET'])
def get_series_list():
    return movie_service.get_series_list()


@movie_bp.route('/top-movies', methods=['GET'])
def get_top_movies_list():
    return movie_service.get_top_movies_list()


@movie_bp.route('/top-series', methods=['GET'])
def get_top_series_list():
    return movie_service.get_top_series_list()

@movie_bp.route('/movies/<page>', methods=['GET'])
@validate()
def get_movies_page(page: int):
    return movie_service.get_movies_page(page)


@movie_bp.route('/series/<page>', methods=['GET'])
@validate()
def get_series_page(page: int):
    return movie_service.get_series_page(page)


@movie_bp.route('/movies/<movie_id>/user/<user_id>/favorite', methods=['PUT'])
@validate()
def add_movie_favorite(movie_id: int, user_id: int):
    return movie_service.add_movie_to_favorite(movie_id, user_id)


@movie_bp.route('/series/<serie_id>/user/<user_id>/favorite', methods=['PUT'])
@validate()
def add_serie_favorite(serie_id: int, user_id: int):
    return movie_service.add_serie_to_favorite(serie_id, user_id)

@movie_bp.route('/movies/<movie_id>/user/<user_id>/favorite', methods=['DELETE'])
@validate()
def remove_movie_favorite(movie_id: int, user_id: int):
    return movie_service.remove_movie_from_favorite(movie_id, user_id)


@movie_bp.route('/series/<serie_id>/user/<user_id>/favorite', methods=['DELETE'])
@validate()
def remove_serie_favorite(serie_id: int, user_id: int):
    return movie_service.remove_serie_from_favorite(serie_id, user_id)


@movie_bp.route('/movies/user/<user_id>/favorites',methods=['GET'])
@validate()
def get_favorites_movies(user_id: int):
    return movie_service.get_favorites_movies(user_id)


@movie_bp.route('/series/user/<user_id>/favorites',methods=['GET'])
@validate()
def get_favorites_series(user_id: int):
    return movie_service.get_favorites_series(user_id)

@movie_bp.route('/movies/search/<keyword>',methods=['GET'])
@validate()
def lookfor_movies(keyword: str):
    return movie_service.look_for_movies(keyword)


@movie_bp.route('/series/search/<keyword>',methods=['GET'])
@validate()
def lookfor_series(keyword: str):
    return movie_service.look_for_series(keyword)


@movie_bp.route('/movies/<movie_id>',methods=['GET'])
@validate()
def movie_details(movie_id: str):
    return movie_service.get_movie_details(movie_id)


@movie_bp.route('/series/<serie_id>',methods=['GET'])
@validate()
def serie_details(serie_id: int):
    return movie_service.get_serie_details(serie_id)

@movie_bp.route('/movies/<movie_id>/trailer',methods=['GET'])
@validate()
def get_movie_trailer(movie_id: str):
    return movie_service.get_movie_trailer(movie_id)


@movie_bp.route('/series/<serie_id>/trailer',methods=['GET'])
@validate()
def get_serie_trailer(serie_id: int):
    return movie_service.get_serie_trailer(serie_id)