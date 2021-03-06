# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Order(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer_id: str=None, basket_number: str=None, special_request: str=None, table_number: str=None):  # noqa: E501
        """Order - a model defined in Swagger

        :param customer_id: The customer_id of this Order.  # noqa: E501
        :type customer_id: str
        :param basket_number: The basket_number of this Order.  # noqa: E501
        :type basket_number: str
        :param special_request: The special_request of this Order.  # noqa: E501
        :type special_request: str
        :param table_number: The table_number of this Order.  # noqa: E501
        :type table_number: str
        """
        self.swagger_types = {
            'customer_id': str,
            'basket_number': str,
            'special_request': str,
            'table_number': str
        }

        self.attribute_map = {
            'customer_id': 'customer_id',
            'basket_number': 'basket_number',
            'special_request': 'special_request',
            'table_number': 'table_number'
        }
        self._customer_id = customer_id
        self._basket_number = basket_number
        self._special_request = special_request
        self._table_number = table_number

    @classmethod
    def from_dict(cls, dikt) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The order of this Order.  # noqa: E501
        :rtype: Order
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_id(self) -> str:
        """Gets the customer_id of this Order.


        :return: The customer_id of this Order.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """Sets the customer_id of this Order.


        :param customer_id: The customer_id of this Order.
        :type customer_id: str
        """

        self._customer_id = customer_id

    @property
    def basket_number(self) -> str:
        """Gets the basket_number of this Order.


        :return: The basket_number of this Order.
        :rtype: str
        """
        return self._basket_number

    @basket_number.setter
    def basket_number(self, basket_number: str):
        """Sets the basket_number of this Order.


        :param basket_number: The basket_number of this Order.
        :type basket_number: str
        """

        self._basket_number = basket_number

    @property
    def special_request(self) -> str:
        """Gets the special_request of this Order.


        :return: The special_request of this Order.
        :rtype: str
        """
        return self._special_request

    @special_request.setter
    def special_request(self, special_request: str):
        """Sets the special_request of this Order.


        :param special_request: The special_request of this Order.
        :type special_request: str
        """

        self._special_request = special_request

    @property
    def table_number(self) -> str:
        """Gets the table_number of this Order.


        :return: The table_number of this Order.
        :rtype: str
        """
        return self._table_number

    @table_number.setter
    def table_number(self, table_number: str):
        """Sets the table_number of this Order.


        :param table_number: The table_number of this Order.
        :type table_number: str
        """

        self._table_number = table_number
