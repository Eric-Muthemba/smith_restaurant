import connexion
import six

from swagger_server.models.signin import Signin  # noqa: E501
from swagger_server.models.signup import Signup  # noqa: E501
from swagger_server import util


def api_signup(body):  # noqa: E501
    """signs up new entities

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Signup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def onboarding_signin(body):  # noqa: E501
    """signs in a registered entity

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Signin.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
