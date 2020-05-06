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
from tator.models.inline_object12 import InlineObject12  # noqa: E501
from tator.rest import ApiException

class TestInlineObject12(unittest.TestCase):
    """InlineObject12 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject12
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.inline_object12.InlineObject12()  # noqa: E501
        if include_optional :
            return InlineObject12(
                gid = '0', 
                md5 = '0', 
                name = '0', 
                section = '0', 
                thumbnail_url = '0', 
                type = -1, 
                uid = '0', 
                url = '0'
            )
        else :
            return InlineObject12(
                gid = '0',
                md5 = '0',
                name = '0',
                section = '0',
                type = -1,
                uid = '0',
                url = '0',
        )

    def testInlineObject12(self):
        """Test InlineObject12"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
