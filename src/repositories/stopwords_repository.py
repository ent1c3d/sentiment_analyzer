from models import Stopword


class StopwordsRepository:
    """ The repository for stopwords """

    @staticmethod
    def create(word, language='en'):
        """ Create a new stopword """
        sentiment = Stopword(word=word, language=language)
        return sentiment.save()

    @staticmethod
    def get_by_language(language):
        """ get stopwords by language"""
        return Stopword.query.filter_by(language=language).all()
