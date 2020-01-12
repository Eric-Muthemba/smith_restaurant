# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.signin import Signin  # noqa: E501
from swagger_server.models.signup import Signup  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOnboardingAPIsController(BaseTestCase):
    """OnboardingAPIsController integration test stubs"""

    def test_api_signup(self):
        """Test case for api_signup

        signs up new entities
        """
        body = Signup()
        response = self.client.open(
            '/signup',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_onboarding_signin(self):
        """Test case for onboarding_signin

        signs in a registered entity
        """
        body = Signin()
        response = self.client.open(
            '/signin',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
