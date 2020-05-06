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
from tator.models.inline_response2008_type import InlineResponse2008Type  # noqa: E501
from tator.rest import ApiException

class TestInlineResponse2008Type(unittest.TestCase):
    """InlineResponse2008Type unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2008Type
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_response2008_type.InlineResponse2008Type()  # noqa: E501
        if include_optional :
            return InlineResponse2008Type(
                association = 'Media', 
                description = '0', 
                id = 56, 
                interpolation = 'latest', 
                name = '0', 
                project = 56, 
                visible = True
            )
        else :
            return InlineResponse2008Type(
        )

    def testInlineResponse2008Type(self):
        """Test InlineResponse2008Type"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
