import json
import os
from flask import current_app


def load_v1_reviews_data():
    relative_path = "../static/reviews/reviews_v1.json"
    return load_json_data(relative_path)


def load_v2_reviews_data():
    # Poor man's pagination. We literally just have each piece of data in a file
    # Ideally we'd just create the pages from a single file but we're short on time

    # Load all 3 pages and split it up into pages
    relative_path_page_1 = "../static/reviews/paginated/v2/reviews_page1.json"
    relative_path_page_2 = "../static/reviews/paginated/v2/reviews_page2.json"
    relative_path_page_3 = "../static/reviews/paginated/v2/reviews_page3.json"
    page_1 = load_json_data(relative_path_page_1)
    page_2 = load_json_data(relative_path_page_2)
    page_3 = load_json_data(relative_path_page_3)

    return [page_1, page_2, page_3]


def load_v3_reviews_data():
    # Poor man's pagination. We literally just have each piece of data in a file
    # Ideally we'd just create the pages from a single file but we're short on time

    # Load all 3 pages and split it up into pages
    relative_path_page_1 = "../static/reviews/paginated/v3/reviews_page1.json"
    relative_path_page_2 = "../static/reviews/paginated/v3/reviews_page2.json"
    relative_path_page_3 = "../static/reviews/paginated/v3/reviews_page3.json"
    page_1 = load_json_data(relative_path_page_1)
    page_2 = load_json_data(relative_path_page_2)
    page_3 = load_json_data(relative_path_page_3)

    return [page_1, page_2, page_3]


def load_json_data(relative_path):
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(basedir, relative_path)
    with open(path) as f:
        return json.load(f)

