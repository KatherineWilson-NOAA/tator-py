# coding: utf-8

# flake8: noqa

"""
    Tator REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.0.1"

# import apis into sdk package
from tator.api.tator_api import TatorApi

# import ApiClient
from tator.api_client import ApiClient
from tator.configuration import Configuration
from tator.exceptions import OpenApiException
from tator.exceptions import ApiTypeError
from tator.exceptions import ApiValueError
from tator.exceptions import ApiKeyError
from tator.exceptions import ApiException
# import models into sdk package
from tator.models.algorithm_launch_response import AlgorithmLaunchResponse
from tator.models.algorithm_launch_spec import AlgorithmLaunchSpec
from tator.models.analysis_spec import AnalysisSpec
from tator.models.attribute_bulk_update import AttributeBulkUpdate
from tator.models.attribute_type import AttributeType
from tator.models.attribute_type_one_of import AttributeTypeOneOf
from tator.models.attribute_type_one_of1 import AttributeTypeOneOf1
from tator.models.attribute_type_one_of2 import AttributeTypeOneOf2
from tator.models.attribute_type_one_of3 import AttributeTypeOneOf3
from tator.models.attribute_type_one_of4 import AttributeTypeOneOf4
from tator.models.attribute_type_one_of5 import AttributeTypeOneOf5
from tator.models.attribute_type_one_of6 import AttributeTypeOneOf6
from tator.models.attribute_type_spec import AttributeTypeSpec
from tator.models.attribute_type_update import AttributeTypeUpdate
from tator.models.box import Box
from tator.models.box_element import BoxElement
from tator.models.box_spec import BoxSpec
from tator.models.box_update import BoxUpdate
from tator.models.create_response import CreateResponse
from tator.models.dot import Dot
from tator.models.dot_element import DotElement
from tator.models.dot_spec import DotSpec
from tator.models.dot_update import DotUpdate
from tator.models.entity_type_schema import EntityTypeSchema
from tator.models.inline_object import InlineObject
from tator.models.inline_object1 import InlineObject1
from tator.models.inline_object10 import InlineObject10
from tator.models.inline_object11 import InlineObject11
from tator.models.inline_object12 import InlineObject12
from tator.models.inline_object13 import InlineObject13
from tator.models.inline_object14 import InlineObject14
from tator.models.inline_object15 import InlineObject15
from tator.models.inline_object16 import InlineObject16
from tator.models.inline_object17 import InlineObject17
from tator.models.inline_object18 import InlineObject18
from tator.models.inline_object19 import InlineObject19
from tator.models.inline_object2 import InlineObject2
from tator.models.inline_object20 import InlineObject20
from tator.models.inline_object21 import InlineObject21
from tator.models.inline_object22 import InlineObject22
from tator.models.inline_object23 import InlineObject23
from tator.models.inline_object24 import InlineObject24
from tator.models.inline_object25 import InlineObject25
from tator.models.inline_object3 import InlineObject3
from tator.models.inline_object4 import InlineObject4
from tator.models.inline_object5 import InlineObject5
from tator.models.inline_object6 import InlineObject6
from tator.models.inline_object7 import InlineObject7
from tator.models.inline_object8 import InlineObject8
from tator.models.inline_object9 import InlineObject9
from tator.models.inline_response200 import InlineResponse200
from tator.models.inline_response2001 import InlineResponse2001
from tator.models.inline_response20010 import InlineResponse20010
from tator.models.inline_response20011 import InlineResponse20011
from tator.models.inline_response20012 import InlineResponse20012
from tator.models.inline_response20012_type import InlineResponse20012Type
from tator.models.inline_response20013 import InlineResponse20013
from tator.models.inline_response20014 import InlineResponse20014
from tator.models.inline_response20015 import InlineResponse20015
from tator.models.inline_response2002 import InlineResponse2002
from tator.models.inline_response2003 import InlineResponse2003
from tator.models.inline_response2004 import InlineResponse2004
from tator.models.inline_response2005 import InlineResponse2005
from tator.models.inline_response2005_type import InlineResponse2005Type
from tator.models.inline_response2006 import InlineResponse2006
from tator.models.inline_response2007 import InlineResponse2007
from tator.models.inline_response2008 import InlineResponse2008
from tator.models.inline_response2008_type import InlineResponse2008Type
from tator.models.inline_response2009 import InlineResponse2009
from tator.models.inline_response200_type import InlineResponse200Type
from tator.models.inline_response201 import InlineResponse201
from tator.models.inline_response2011 import InlineResponse2011
from tator.models.inline_response2012 import InlineResponse2012
from tator.models.inline_response2013 import InlineResponse2013
from tator.models.inline_response400 import InlineResponse400
from tator.models.inline_response404 import InlineResponse404
from tator.models.line import Line
from tator.models.line_element import LineElement
from tator.models.line_spec import LineSpec
from tator.models.line_update import LineUpdate
from tator.models.localization import Localization
from tator.models.localization_association_update import LocalizationAssociationUpdate
from tator.models.localization_list import LocalizationList
from tator.models.localization_spec import LocalizationSpec
from tator.models.localization_update import LocalizationUpdate
from tator.models.many_spec import ManySpec
from tator.models.message_response import MessageResponse
from tator.models.video_spec import VideoSpec
from tator.models.video_update import VideoUpdate

