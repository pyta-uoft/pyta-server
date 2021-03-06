import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def get_env_variable(name):
    """Get server admin information from server host environment"""
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-later'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from pyta_server import routes
