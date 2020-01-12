# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.add_item import AddItem  # noqa: E501
from swagger_server.models.add_to_basket import AddToBasket  # noqa: E501
from swagger_server.models.assign_task import AssignTask  # noqa: E501
from swagger_server.models.feedback import Feedback  # noqa: E501
from swagger_server.models.new_customer import NewCustomer  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.update_item import UpdateItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCrudAPIsController(BaseTestCase):
    """CrudAPIsController integration test stubs"""

    def test_api_add_item(self):
        """Test case for api_add_item

        adds new menu items to the menu
        """
        body = AddItem()
        response = self.client.open(
            '/add_item',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_add_to_basket(self):
        """Test case for api_add_to_basket

        make an order
        """
        body = AddToBasket()
        response = self.client.open(
            '/add_to_basket',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_ask_for_help(self):
        """Test case for api_ask_for_help

        request help for specific table
        """
        response = self.client.open(
            '/ask_for_help/{table_id}'.format(table_id='table_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_assign_task(self):
        """Test case for api_assign_task

        assign task to personel
        """
        body = AssignTask()
        response = self.client.open(
            '/assign_task',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_confirm_order(self):
        """Test case for api_confirm_order

        chef confirms that he/she has received the order and has started working on it.
        """
        response = self.client.open(
            '/confirm_order/{work_id}'.format(work_id='work_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_feedback(self):
        """Test case for api_feedback

        give feedback on use
        """
        body = Feedback()
        response = self.client.open(
            '/feedback',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_get_orders(self):
        """Test case for api_get_orders

        Get all orders
        """
        response = self.client.open(
            '/get_order/{customer_id}'.format(customer_id='customer_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_new_customer(self):
        """Test case for api_new_customer

        updates new customer info
        """
        body = NewCustomer()
        response = self.client.open(
            '/new_customer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_order(self):
        """Test case for api_order

        make an order
        """
        body = Order()
        response = self.client.open(
            '/order',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_order_ready(self):
        """Test case for api_order_ready

        chef confirms that he/she has finished the order.
        """
        response = self.client.open(
            '/order_ready/{work_id}'.format(work_id='work_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_update_item(self):
        """Test case for api_update_item

        updates menu items to the menu
        """
        body = UpdateItem()
        response = self.client.open(
            '/update_item',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
