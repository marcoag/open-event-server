"""Copyright 2015 Rafal Kowalski"""
from . import db


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name
