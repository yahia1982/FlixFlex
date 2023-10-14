from flask import Flask, jsonify
from flask_cors import CORS
from routes.user_bp import user_bp
from routes.movie_bp import movie_bp

app = Flask(__name__)

API_BASE_PATH = "/api"

cors_path = API_BASE_PATH + "/*"
CORS(app, resources={
    cors_path: {"origins": "*"}
})

app.register_blueprint(user_bp, url_prefix=API_BASE_PATH)
app.register_blueprint(movie_bp, url_prefix=API_BASE_PATH)


@app.route('/api/health-check')
def health_check():
    return jsonify({}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)