"""
Defines the blueprint for sentiment analysis
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import SentimentAnalysisResource


SA_BLUEPRINT = Blueprint('sentiment_analysis', __name__)
Api(SA_BLUEPRINT).add_resource(
    SentimentAnalysisResource,
    '/sentiment_analysis/<string:tweet_body>'
)
