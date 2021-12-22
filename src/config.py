import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    DEBUG = os.environ.get("FLASK_DEBUG") == "1"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "someone-done-fucked-up"
