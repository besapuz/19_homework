# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from doa.models.movies import movies_schema, movie_schema

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movies_schema.dump(movie_service.get_movie(**request.args))
        return movies, 200

    def post(self):
        req_json = request.json
        new_movie = movie_service.creat_movie(req_json)
        return "", 201, {'location': f"{movie_ns.path}/{new_movie}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return movie_schema.dump(movie_service.get_movie(mid))

    def put(self, mid):
        movie = movie_schema.dump(movie_service.update_movie(mid, request.json))
        if not movie:
            return f"Фильм не найден", 404
        return f"Movie обновлен", 204



    def patch(self, mid):
        movie = movie_schema.dump(movie_service.update_movie_partial(mid, request.json))
        if not movie:
            return f"Фильм не найден", 404
        return f"Movie обновлен", 204

    def delete(self, mid):
        try:
            movie_service.delete(mid)
            return 204
        except Exception as e:
            print(e)
            return 500
