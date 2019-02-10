from random import shuffle
import pickle

from flask_script import Command
from nltk import classify
from nltk import NaiveBayesClassifier

from repositories import PostsRepository
from helpers import bag_of_words


class ClassifierGenerator(Command):
    '''
    This class is used by flask-script.
    It uses helper functions,
    generates classification models and saves as file with pickle module
    '''

    def run(self):

        self.neg_tweets = PostsRepository.get_by_sentiment('neg')
        self.pos_tweets = PostsRepository.get_by_sentiment('pos')

        pos_tweets_set = []
        for tweet in self.pos_tweets:
            pos_tweets_set.append((bag_of_words(tweet.text), 'pos'))

        neg_tweets_set = []
        for tweet in self.neg_tweets:
            neg_tweets_set.append((bag_of_words(tweet.text), 'neg'))

        shuffle(pos_tweets_set)
        shuffle(neg_tweets_set)

        test_set = pos_tweets_set[:1000] + neg_tweets_set[:1000]
        train_set = pos_tweets_set[1000:] + neg_tweets_set[1000:]

        classifier = NaiveBayesClassifier.train(train_set)
        pickle.dump(classifier, open("sentiment_classifier.pkl", "wb"))

        accuracy = classify.accuracy(classifier, test_set)
        print(accuracy)
