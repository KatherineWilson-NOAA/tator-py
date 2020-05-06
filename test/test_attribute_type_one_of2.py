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
from tator.models.attribute_type_one_of2 import AttributeTypeOneOf2  # noqa: E501
from tator.rest import ApiException

class TestAttributeTypeOneOf2(unittest.TestCase):
    """AttributeTypeOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AttributeTypeOneOf2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.attribute_type_one_of2.AttributeTypeOneOf2()  # noqa: E501
        if include_optional :
            return AttributeTypeOneOf2(
                applies_to = 56, 
                default = 1.337, 
                description = '0', 
                dtype = 'float', 
                lower_bound = 1.337, 
                name = '0', 
                order = 56, 
                upper_bound = 1.337
            )
        else :
            return AttributeTypeOneOf2(
                applies_to = 56,
                dtype = 'float',
                name = '0',
        )

    def testAttributeTypeOneOf2(self):
        """Test AttributeTypeOneOf2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
