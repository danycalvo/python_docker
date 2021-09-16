from mongoengine import *
from app import db


class Mensaje(Document):
    ts = FloatField()
    texto = StringField()

    def _init__(self, ts, texto):
        self.texto = texto
        self.ts = ts
