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


class InlineObject15(object):
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
        'association': 'str',
        'description': 'str',
        'media_types': 'list[int]',
        'name': 'str'
    }

    attribute_map = {
        'association': 'association',
        'description': 'description',
        'media_types': 'media_types',
        'name': 'name'
    }

    def __init__(self, association=None, description='', media_types=None, name=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject15 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._association = None
        self._description = None
        self._media_types = None
        self._name = None
        self.discriminator = None

        self.association = association
        if description is not None:
            self.description = description
        self.media_types = media_types
        self.name = name

    @property
    def association(self):
        """Gets the association of this InlineObject15.  # noqa: E501

        Type of object this state type is associated with.  # noqa: E501

        :return: The association of this InlineObject15.  # noqa: E501
        :rtype: str
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this InlineObject15.

        Type of object this state type is associated with.  # noqa: E501

        :param association: The association of this InlineObject15.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and association is None:  # noqa: E501
            raise ValueError("Invalid value for `association`, must not be `None`")  # noqa: E501
        allowed_values = ["Media", "Frame", "Localization"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and association not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `association` ({0}), must be one of {1}"  # noqa: E501
                .format(association, allowed_values)
            )

        self._association = association

    @property
    def description(self):
        """Gets the description of this InlineObject15.  # noqa: E501

        Description of the state type.  # noqa: E501

        :return: The description of this InlineObject15.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject15.

        Description of the state type.  # noqa: E501

        :param description: The description of this InlineObject15.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def media_types(self):
        """Gets the media_types of this InlineObject15.  # noqa: E501

        List of integers identifying media types that this state type may apply to.  # noqa: E501

        :return: The media_types of this InlineObject15.  # noqa: E501
        :rtype: list[int]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this InlineObject15.

        List of integers identifying media types that this state type may apply to.  # noqa: E501

        :param media_types: The media_types of this InlineObject15.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and media_types is None:  # noqa: E501
            raise ValueError("Invalid value for `media_types`, must not be `None`")  # noqa: E501

        self._media_types = media_types

    @property
    def name(self):
        """Gets the name of this InlineObject15.  # noqa: E501

        Name of the state type.  # noqa: E501

        :return: The name of this InlineObject15.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject15.

        Name of the state type.  # noqa: E501

        :param name: The name of this InlineObject15.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, InlineObject15):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject15):
            return True

        return self.to_dict() != other.to_dict()
