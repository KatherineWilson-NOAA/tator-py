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
from tator.models.attribute_type_spec import AttributeTypeSpec  # noqa: E501
from tator.rest import ApiException

class TestAttributeTypeSpec(unittest.TestCase):
    """AttributeTypeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AttributeTypeSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.attribute_type_spec.AttributeTypeSpec()  # noqa: E501
        if include_optional :
            return AttributeTypeSpec(
                applies_to = 56, 
                default = [
                    1.337
                    ], 
                description = '0', 
                dtype = 'geopos', 
                name = '0', 
                order = 56, 
                lower_bound = 1.337, 
                upper_bound = 1.337, 
                autocomplete = None, 
                choices = [
                    '0'
                    ], 
                labels = [
                    '0'
                    ], 
                use_current = True
            )
        else :
            return AttributeTypeSpec(
                applies_to = 56,
                dtype = 'geopos',
                name = '0',
        )

    def testAttributeTypeSpec(self):
        """Test AttributeTypeSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
