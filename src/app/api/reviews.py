import json
import random

from flask import current_app, jsonify, request, url_for
from app.api import bp

from app import v1_reviews_data, v2_reviews_data, v3_reviews_data

V3_PROBABILITY_OF_ERROR = 0.85


@bp.route("/reviews/v1")
def reviews_v1():
    return jsonify({"data": v1_reviews_data})


@bp.route("/reviews/v2")
def reviews_v2():
    result = _get_paginated_data_for_route("api.reviews_v2")
    if result is None:
        return jsonify({"error": "Invalid page"}), 404

    return jsonify(result)


@bp.route("/reviews/v3")
def reviews_v3():
    result = _get_paginated_data_for_route("api.reviews_v3")
    if result is None:
        return jsonify({"error": "Invalid page"}), 404

    should_randomly_error = random.randint(0, 1) <= V3_PROBABILITY_OF_ERROR
    if should_randomly_error:
        return (
            jsonify(
                {
                    "error": "You have exceeded the rate limit for this endpoint. Please try again later"
                }
            ),
            429,
        )
    return jsonify(result)


def _get_paginated_data_for_route(route):
    page_number = int(request.args.get("page", "1"))
    if route == "api.reviews_v2":
        paginated_reviews_data = v2_reviews_data
    elif route == "api.reviews_v3":
        paginated_reviews_data = v3_reviews_data
    else:
        raise Exception(f"Unexpected route {route}")

    if page_number > len(paginated_reviews_data):
        return None

    data = paginated_reviews_data[page_number - 1]

    has_prev_page = page_number != 1
    has_next_page = page_number < len(paginated_reviews_data)
    prev_page_url = url_for(route, page=(page_number - 1)) if has_prev_page else None
    next_page_url = url_for(route, page=(page_number + 1)) if has_next_page else None
    page_info = {
        "hasPrevPage": has_prev_page,
        "hasNextPage": has_next_page,
        "prevPageUrl": prev_page_url,
        "nextPageUrl": next_page_url,
    }

    return {
        "pageInfo": page_info,
        "data": data,
    }
