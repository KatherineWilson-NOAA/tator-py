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
from tator.models.box_spec import BoxSpec  # noqa: E501
from tator.rest import ApiException

class TestBoxSpec(unittest.TestCase):
    """BoxSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BoxSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.box_spec.BoxSpec()  # noqa: E501
        if include_optional :
            return BoxSpec(
                frame = 56, 
                height = 0.0, 
                media_id = 56, 
                modified = True, 
                type = 56, 
                version = 56, 
                width = 0.0, 
                x = 0.0, 
                y = 0.0
            )
        else :
            return BoxSpec(
                frame = 56,
                height = 0.0,
                media_id = 56,
                type = 56,
                width = 0.0,
                x = 0.0,
                y = 0.0,
        )

    def testBoxSpec(self):
        """Test BoxSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
