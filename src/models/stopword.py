from . import db
from .abc import BaseModel


class Stopword(db.Model, BaseModel):
    """ The stopwords model """
    __tablename__ = 'stopwords'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), primary_key=False)
    language = db.Column(db.String(50), primary_key=False,
                         default='en')

    def __init__(self, word, language):
        """ Create a new stopword """
        self.word = word
        self.language = language
