from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .post import Post
from .stopword import Stopword