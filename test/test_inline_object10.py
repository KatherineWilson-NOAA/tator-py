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
from tator.models.inline_object10 import InlineObject10  # noqa: E501
from tator.rest import ApiException

class TestInlineObject10(unittest.TestCase):
    """InlineObject10 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject10
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_object10.InlineObject10()  # noqa: E501
        if include_optional :
            return InlineObject10(
                name = '0', 
                summary = '0'
            )
        else :
            return InlineObject10(
        )

    def testInlineObject10(self):
        """Test InlineObject10"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
