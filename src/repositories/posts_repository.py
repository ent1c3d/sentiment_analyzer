from models import Post


class PostsRepository:
    """ The repository for posts """

    @staticmethod
    def create(text, sentiment):
        """ Create a new post """
        sentiment = Post(text=text, sentiment=sentiment)
        return sentiment.save()

    @staticmethod
    def get_total_count():
        """ get total count of posts"""
        return Post.query.filter_by().count()

    @staticmethod
    def get_by_sentiment(sentiment):
        """ get posts by sentiment"""
        return Post.query.filter_by(sentiment=sentiment).all()
