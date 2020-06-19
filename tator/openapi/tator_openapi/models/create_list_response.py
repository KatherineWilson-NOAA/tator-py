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

from tator_openapi.configuration import Configuration


class CreateListResponse(object):
    """
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'list[int]',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message'
    }

    def __init__(self, id=None, message=None, local_vars_configuration=None):  # noqa: E501
        """CreateListResponse - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message

    @property
    def id(self):
        """
        List of unique integers identifying created objects.

        :return: The id of this CreateListResponse. 
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        List of unique integers identifying created objects.

        :param id: The id of this CreateListResponse.
        :type: list[int]
        """

        self._id = id

    @property
    def message(self):
        """
        Message indicating successful creation.

        :return: The message of this CreateListResponse. 
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Message indicating successful creation.

        :param message: The message of this CreateListResponse.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, CreateListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateListResponse):
            return True

        return self.to_dict() != other.to_dict()
