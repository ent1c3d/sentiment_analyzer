from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()

from .sentiment_analysis import SentimentAnalysisResource

