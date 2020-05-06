# coding: utf-8

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tator.configuration import Configuration


class InlineResponse2002(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'next': 'int'
    }

    attribute_map = {
        'next': 'next'
    }

    def __init__(self, next=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2002 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._next = None
        self.discriminator = None

        if next is not None:
            self.next = next

    @property
    def next(self):
        """Gets the next of this InlineResponse2002.  # noqa: E501


        :return: The next of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this InlineResponse2002.


        :param next: The next of this InlineResponse2002.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                next is not None and next < 0):  # noqa: E501
            raise ValueError("Invalid value for `next`, must be a value greater than or equal to `0`")  # noqa: E501

        self._next = next

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2002):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2002):
            return True

        return self.to_dict() != other.to_dict()
