# coding: utf-8

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tator
from tator.models.inline_object9 import InlineObject9  # noqa: E501
from tator.rest import ApiException

class TestInlineObject9(unittest.TestCase):
    """InlineObject9 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject9
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_object9.InlineObject9()  # noqa: E501
        if include_optional :
            return InlineObject9(
                message = '0', 
                send_as_file = '0'
            )
        else :
            return InlineObject9(
                message = '0',
                send_as_file = '0',
        )

    def testInlineObject9(self):
        """Test InlineObject9"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
