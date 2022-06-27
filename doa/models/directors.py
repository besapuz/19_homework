from marshmallow import Schema, fields

from setup_db import db


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __str__(self):
        return self.name


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
