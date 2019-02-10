import pickle

from flasgger import swag_from
from flask.ext.restful import Resource
from flask.json import jsonify

from helpers import bag_of_words


class SentimentAnalysisResource(Resource):

    @staticmethod
    @swag_from('../swagger/sentiment_analysis/GET.yml')
    def get(tweet_body):
        """
        uses sentiment classifier model for  sentiment analysis
        and returns result as json

        Parameters:
        tweet_body (str): body of twitter post

        Returns:
        json: {tweet_body: "POS"/"NEG"}
        """

        model = pickle.load(open("sentiment_classifier.pkl", "rb"))

        sentiment_set = bag_of_words(tweet_body)
        result = model.classify(sentiment_set)
        return jsonify({tweet_body: result.upper()})
