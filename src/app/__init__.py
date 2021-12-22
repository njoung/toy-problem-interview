from flask import Flask
from config import Config
from app.utils.reviews_utils import (
    load_v1_reviews_data,
    load_v2_reviews_data,
    load_v3_reviews_data,
)

v1_reviews_data = load_v1_reviews_data()
v2_reviews_data = load_v2_reviews_data()
v3_reviews_data = load_v3_reviews_data()


def create_app():
    new_app = Flask(__name__)
    new_app.config.from_object(Config)

    from app.api import bp as api_bp

    new_app.register_blueprint(api_bp, url_prefix="/api")

    return new_app

