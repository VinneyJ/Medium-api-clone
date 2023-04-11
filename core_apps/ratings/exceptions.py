from rest_framework.exceptions import APIException


class CantRateYourArticle(APIException):
    status_code = 403
    default_detail = 'You cannot rate/review your own article'
    #default_code = 'cant_rate_your_article'

class AlreadyRated(APIException):
    status_code = 400
    default_detail = 'You have already rated this article'
    #default_code = 'already_rated'
