from marshmallow import Schema, fields

from setup_db import db


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __str__(self):
        return self.name


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
