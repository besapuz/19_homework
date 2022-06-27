from flask_restx import Resource, Namespace
from container import genre_service
from doa.models.genres import genres_schema, genre_schema

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genres_schema.dump(genre_service.get_genre())
        return genres, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_schema.dump(genre_service.get_genre(gid))
        return genre, 200
