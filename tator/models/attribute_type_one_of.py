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


class AttributeTypeOneOf(object):
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
        'applies_to': 'int',
        'default': 'bool',
        'description': 'str',
        'dtype': 'str',
        'name': 'str',
        'order': 'int'
    }

    attribute_map = {
        'applies_to': 'applies_to',
        'default': 'default',
        'description': 'description',
        'dtype': 'dtype',
        'name': 'name',
        'order': 'order'
    }

    def __init__(self, applies_to=None, default=None, description='', dtype=None, name=None, order=0, local_vars_configuration=None):  # noqa: E501
        """AttributeTypeOneOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._applies_to = None
        self._default = None
        self._description = None
        self._dtype = None
        self._name = None
        self._order = None
        self.discriminator = None

        self.applies_to = applies_to
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        self.dtype = dtype
        self.name = name
        if order is not None:
            self.order = order

    @property
    def applies_to(self):
        """Gets the applies_to of this AttributeTypeOneOf.  # noqa: E501

        Unique integer identifying the entity type that this attribute describes.  # noqa: E501

        :return: The applies_to of this AttributeTypeOneOf.  # noqa: E501
        :rtype: int
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this AttributeTypeOneOf.

        Unique integer identifying the entity type that this attribute describes.  # noqa: E501

        :param applies_to: The applies_to of this AttributeTypeOneOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and applies_to is None:  # noqa: E501
            raise ValueError("Invalid value for `applies_to`, must not be `None`")  # noqa: E501

        self._applies_to = applies_to

    @property
    def default(self):
        """Gets the default of this AttributeTypeOneOf.  # noqa: E501

        Default value for the attribute.  # noqa: E501

        :return: The default of this AttributeTypeOneOf.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this AttributeTypeOneOf.

        Default value for the attribute.  # noqa: E501

        :param default: The default of this AttributeTypeOneOf.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this AttributeTypeOneOf.  # noqa: E501

        Description of the attribute.  # noqa: E501

        :return: The description of this AttributeTypeOneOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttributeTypeOneOf.

        Description of the attribute.  # noqa: E501

        :param description: The description of this AttributeTypeOneOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dtype(self):
        """Gets the dtype of this AttributeTypeOneOf.  # noqa: E501

        Data type of the attribute.  # noqa: E501

        :return: The dtype of this AttributeTypeOneOf.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this AttributeTypeOneOf.

        Data type of the attribute.  # noqa: E501

        :param dtype: The dtype of this AttributeTypeOneOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dtype is None:  # noqa: E501
            raise ValueError("Invalid value for `dtype`, must not be `None`")  # noqa: E501
        allowed_values = ["bool"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dtype not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dtype` ({0}), must be one of {1}"  # noqa: E501
                .format(dtype, allowed_values)
            )

        self._dtype = dtype

    @property
    def name(self):
        """Gets the name of this AttributeTypeOneOf.  # noqa: E501

        Name of the attribute.  # noqa: E501

        :return: The name of this AttributeTypeOneOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttributeTypeOneOf.

        Name of the attribute.  # noqa: E501

        :param name: The name of this AttributeTypeOneOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order(self):
        """Gets the order of this AttributeTypeOneOf.  # noqa: E501

        Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default.  # noqa: E501

        :return: The order of this AttributeTypeOneOf.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AttributeTypeOneOf.

        Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default.  # noqa: E501

        :param order: The order of this AttributeTypeOneOf.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if not isinstance(other, AttributeTypeOneOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttributeTypeOneOf):
            return True

        return self.to_dict() != other.to_dict()
