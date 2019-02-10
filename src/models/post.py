from . import db
from .abc import BaseModel


class Post(db.Model, BaseModel):
    """ The Posts model """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280), primary_key=False)
    sentiment = db.Column(db.Enum('pos', 'neg', name='sentiment'),
                          primary_key=False)

    def __init__(self, text, sentiment):
        """ Create a new post """
        self.text = text
        self.sentiment = sentiment
