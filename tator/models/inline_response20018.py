# coding: utf-8

"""
    Tator REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse20018(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'RestMediaTypesprojectType',
        'columns': 'list[OneOfinlineResponse20018ColumnsItems]'
    }

    attribute_map = {
        'type': 'type',
        'columns': 'columns'
    }

    def __init__(self, type=None, columns=None):  # noqa: E501
        """InlineResponse20018 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._columns = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if columns is not None:
            self.columns = columns

    @property
    def type(self):
        """Gets the type of this InlineResponse20018.  # noqa: E501


        :return: The type of this InlineResponse20018.  # noqa: E501
        :rtype: RestMediaTypesprojectType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20018.


        :param type: The type of this InlineResponse20018.  # noqa: E501
        :type: RestMediaTypesprojectType
        """

        self._type = type

    @property
    def columns(self):
        """Gets the columns of this InlineResponse20018.  # noqa: E501

        Attribute types associated with this localization type.  # noqa: E501

        :return: The columns of this InlineResponse20018.  # noqa: E501
        :rtype: list[OneOfinlineResponse20018ColumnsItems]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this InlineResponse20018.

        Attribute types associated with this localization type.  # noqa: E501

        :param columns: The columns of this InlineResponse20018.  # noqa: E501
        :type: list[OneOfinlineResponse20018ColumnsItems]
        """

        self._columns = columns

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse20018, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20018):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
