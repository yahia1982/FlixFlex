from flask import Flask

from routes.user_bp import user_bp
from routes.movie_bp import movie_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(movie_bp)

