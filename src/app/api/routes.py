from app.api import bp
from flask import current_app


@bp.route("/health")
def health():
    return "success"


@bp.route("/boom")
def boom():
    raise Exception("boom")
