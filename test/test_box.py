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
from tator.models.box import Box  # noqa: E501
from tator.rest import ApiException

class TestBox(unittest.TestCase):
    """Box unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Box
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.box.Box()  # noqa: E501
        if include_optional :
            return Box(
                attributes = { }, 
                email = '0', 
                frame = 56, 
                height = 0.0, 
                id = 56, 
                media = 56, 
                meta = 56, 
                modified = True, 
                project = 56, 
                thumbnail_image = '0', 
                version = 56, 
                width = 0.0, 
                x = 0.0, 
                y = 0.0
            )
        else :
            return Box(
        )

    def testBox(self):
        """Test Box"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
