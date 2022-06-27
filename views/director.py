from flask_restx import Resource, Namespace
from doa.models.directors import directors_schema, director_schema
from container import director_service

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = directors_schema.dump(director_service.get_director())
        return directors, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_schema.dump(director_service.get_director(did))
        return director, 200
