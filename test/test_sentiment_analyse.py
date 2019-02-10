import unittest
import json
import pickle

from server import server
from helpers import bag_of_words


class TestSentimentAnalyse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def test_with_positive_tweet_text(self):
        """ The GET on `I am happy` -  should return POS """
        response = self.client.get('/application/sentiment_analysis/I%20am%20happy')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_json['I am happy'],
            "POS"
        )

    def test_with_negative_tweet_text(self):
        """ The GET on `/I am tired`   -  should return NEG """
        response = self.client.get('/application/sentiment_analysis/I%20am%20tired')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_json['I am tired'],
            "NEG"
        )

    def test_saved_classification_model(self):
        model = pickle.load(open("sentiment_classifier.pkl", "rb"))

        sentiment_set = bag_of_words('This tweet is great')
        result = model.classify(sentiment_set)
        self.assertEqual(
            result,
            "pos"
        )

        sentiment_set = bag_of_words('I hate tweets')
        result = model.classify(sentiment_set)
        self.assertEqual(
            result,
            "neg"
        )
