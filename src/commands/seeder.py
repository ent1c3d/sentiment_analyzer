from flask_script import Command
import nltk
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords

from repositories import PostsRepository
from repositories import StopwordsRepository


class Seeder(Command):
    '''
    This class is used by flask-script.
    It downloads nltk files and inserts them into appropriate db tables
    '''

    def run(self):
        nltk.download('twitter_samples')
        nltk.download('stopwords')
        pos_tweets = twitter_samples.strings('positive_tweets.json')
        neg_tweets = twitter_samples.strings('negative_tweets.json')
        stopwords_english = stopwords.words('english')

        for post_tweet, neg_tweet in zip(pos_tweets, neg_tweets):
            PostsRepository.create(text=post_tweet, sentiment='pos')
            PostsRepository.create(text=neg_tweet, sentiment='neg')

        for stopword in stopwords_english:
            StopwordsRepository.create(word=stopword)
