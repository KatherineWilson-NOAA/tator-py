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
from tator.models.inline_response20012_type import InlineResponse20012Type  # noqa: E501
from tator.rest import ApiException

class TestInlineResponse20012Type(unittest.TestCase):
    """InlineResponse20012Type unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20012Type
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_response20012_type.InlineResponse20012Type()  # noqa: E501
        if include_optional :
            return InlineResponse20012Type(
                description = '0', 
                id = 56, 
                name = '0', 
                project = 56
            )
        else :
            return InlineResponse20012Type(
        )

    def testInlineResponse20012Type(self):
        """Test InlineResponse20012Type"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
