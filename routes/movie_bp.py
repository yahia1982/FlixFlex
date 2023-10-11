from flask import Blueprint

from services.movie_service import MovieService

movie_bp = Blueprint("movie_bp", __name__)

movie_service = MovieService()