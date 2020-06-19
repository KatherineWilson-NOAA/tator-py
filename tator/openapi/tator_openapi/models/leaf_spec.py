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


class LeafSpec(object):
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
        'name': 'str',
        'parent': 'int',
        'type': 'int'
    }

    attribute_map = {
        'name': 'name',
        'parent': 'parent',
        'type': 'type'
    }

    def __init__(self, name=None, parent=None, type=None, local_vars_configuration=None):  # noqa: E501
        """LeafSpec - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._parent = None
        self._type = None
        self.discriminator = None

        self.name = name
        if parent is not None:
            self.parent = parent
        self.type = type

    @property
    def name(self):
        """
        Name of the leaf.

        :return: The name of this LeafSpec. 
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Name of the leaf.

        :param name: The name of this LeafSpec.
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent(self):
        """
        ID to use as parent if there is one.

        :return: The parent of this LeafSpec. 
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        ID to use as parent if there is one.

        :param parent: The parent of this LeafSpec.
        :type: int
        """

        self._parent = parent

    @property
    def type(self):
        """
        Unique integer identifying a leaf type.

        :return: The type of this LeafSpec. 
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Unique integer identifying a leaf type.

        :param type: The type of this LeafSpec.
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, LeafSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LeafSpec):
            return True

        return self.to_dict() != other.to_dict()
