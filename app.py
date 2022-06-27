from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie import movie_ns
from views.director import director_ns
from views.genre import genre_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    application.app_context().push()
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)



app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(port=80)
