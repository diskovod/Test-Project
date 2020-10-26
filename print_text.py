import unittest
from mailjet_rest import Client
import os
import random
import string


class TestSuite(unittest.TestCase):

    def setUp(self):
        self.auth = (
            os.environ['MJ_APIKEY_PUBLIC'],
            os.environ['MJ_APIKEY_PRIVATE']
        )
       	self.client = Client(auth=self.auth)

    def test_get_no_param(self):
        result = self.client.contact.get().json()
        self.assertTrue(('Data' in result and 'Count' in result))

    def test_get_valid_params(self):
        result = self.client.contact.get(filters={'limit': 2}).json()
        self.assertTrue(result['Count'] >= 0 or result['Count'] <= 2)
