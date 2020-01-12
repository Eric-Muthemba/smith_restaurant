# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Feedback(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer_name: str=None, feedback: str=None, rate_us: int=None):  # noqa: E501
        """Feedback - a model defined in Swagger

        :param customer_name: The customer_name of this Feedback.  # noqa: E501
        :type customer_name: str
        :param feedback: The feedback of this Feedback.  # noqa: E501
        :type feedback: str
        :param rate_us: The rate_us of this Feedback.  # noqa: E501
        :type rate_us: int
        """
        self.swagger_types = {
            'customer_name': str,
            'feedback': str,
            'rate_us': int
        }

        self.attribute_map = {
            'customer_name': 'customer_name',
            'feedback': 'feedback',
            'rate_us': 'rate_us'
        }
        self._customer_name = customer_name
        self._feedback = feedback
        self._rate_us = rate_us

    @classmethod
    def from_dict(cls, dikt) -> 'Feedback':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The feedback of this Feedback.  # noqa: E501
        :rtype: Feedback
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_name(self) -> str:
        """Gets the customer_name of this Feedback.


        :return: The customer_name of this Feedback.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name: str):
        """Sets the customer_name of this Feedback.


        :param customer_name: The customer_name of this Feedback.
        :type customer_name: str
        """

        self._customer_name = customer_name

    @property
    def feedback(self) -> str:
        """Gets the feedback of this Feedback.


        :return: The feedback of this Feedback.
        :rtype: str
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback: str):
        """Sets the feedback of this Feedback.


        :param feedback: The feedback of this Feedback.
        :type feedback: str
        """

        self._feedback = feedback

    @property
    def rate_us(self) -> int:
        """Gets the rate_us of this Feedback.


        :return: The rate_us of this Feedback.
        :rtype: int
        """
        return self._rate_us

    @rate_us.setter
    def rate_us(self, rate_us: int):
        """Sets the rate_us of this Feedback.


        :param rate_us: The rate_us of this Feedback.
        :type rate_us: int
        """

        self._rate_us = rate_us
