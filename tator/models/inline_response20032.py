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


class InlineResponse20032(object):
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
        'id': 'int',
        'project': 'int',
        'path': 'str',
        'name': 'str',
        'parent': 'int',
        'attributes': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'project': 'project',
        'path': 'path',
        'name': 'name',
        'parent': 'parent',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, project=None, path=None, name=None, parent=None, attributes=None):  # noqa: E501
        """InlineResponse20032 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._project = None
        self._path = None
        self._name = None
        self._parent = None
        self._attributes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this InlineResponse20032.  # noqa: E501

        Unique integer identifying the tree leaf.  # noqa: E501

        :return: The id of this InlineResponse20032.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20032.

        Unique integer identifying the tree leaf.  # noqa: E501

        :param id: The id of this InlineResponse20032.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this InlineResponse20032.  # noqa: E501

        Unique integer identifying a project.  # noqa: E501

        :return: The project of this InlineResponse20032.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this InlineResponse20032.

        Unique integer identifying a project.  # noqa: E501

        :param project: The project of this InlineResponse20032.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def path(self):
        """Gets the path of this InlineResponse20032.  # noqa: E501

        Full path to leaf in hierarchy.  # noqa: E501

        :return: The path of this InlineResponse20032.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this InlineResponse20032.

        Full path to leaf in hierarchy.  # noqa: E501

        :param path: The path of this InlineResponse20032.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """Gets the name of this InlineResponse20032.  # noqa: E501

        Name of the tree leaf.  # noqa: E501

        :return: The name of this InlineResponse20032.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20032.

        Name of the tree leaf.  # noqa: E501

        :param name: The name of this InlineResponse20032.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this InlineResponse20032.  # noqa: E501

        ID to use as parent if there is one.  # noqa: E501

        :return: The parent of this InlineResponse20032.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this InlineResponse20032.

        ID to use as parent if there is one.  # noqa: E501

        :param parent: The parent of this InlineResponse20032.  # noqa: E501
        :type: int
        """

        self._parent = parent

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse20032.  # noqa: E501

        Object containing attribute values.  # noqa: E501

        :return: The attributes of this InlineResponse20032.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse20032.

        Object containing attribute values.  # noqa: E501

        :param attributes: The attributes of this InlineResponse20032.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

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
        if issubclass(InlineResponse20032, dict):
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
        if not isinstance(other, InlineResponse20032):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
