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


class InlineResponse20016(object):
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
        'created_by': 'str',
        'created_datetime': 'str',
        'description': 'str',
        'id': 'int',
        'modified_by': 'str',
        'modified_datetime': 'str',
        'name': 'str',
        'num_created': 'int',
        'num_modified': 'int',
        'number': 'int',
        'project': 'int',
        'show_empty': 'bool'
    }

    attribute_map = {
        'created_by': 'created_by',
        'created_datetime': 'created_datetime',
        'description': 'description',
        'id': 'id',
        'modified_by': 'modified_by',
        'modified_datetime': 'modified_datetime',
        'name': 'name',
        'num_created': 'num_created',
        'num_modified': 'num_modified',
        'number': 'number',
        'project': 'project',
        'show_empty': 'show_empty'
    }

    def __init__(self, created_by=None, created_datetime=None, description=None, id=None, modified_by=None, modified_datetime=None, name=None, num_created=None, num_modified=None, number=None, project=None, show_empty=None):  # noqa: E501
        """InlineResponse20016 - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_datetime = None
        self._description = None
        self._id = None
        self._modified_by = None
        self._modified_datetime = None
        self._name = None
        self._num_created = None
        self._num_modified = None
        self._number = None
        self._project = None
        self._show_empty = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_datetime is not None:
            self.modified_datetime = modified_datetime
        if name is not None:
            self.name = name
        if num_created is not None:
            self.num_created = num_created
        if num_modified is not None:
            self.num_modified = num_modified
        if number is not None:
            self.number = number
        if project is not None:
            self.project = project
        if show_empty is not None:
            self.show_empty = show_empty

    @property
    def created_by(self):
        """Gets the created_by of this InlineResponse20016.  # noqa: E501

        Name of user who created the last unmodified annotation in this version.  # noqa: E501

        :return: The created_by of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InlineResponse20016.

        Name of user who created the last unmodified annotation in this version.  # noqa: E501

        :param created_by: The created_by of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_datetime(self):
        """Gets the created_datetime of this InlineResponse20016.  # noqa: E501

        Datetime when the last unmodified annotation was created.  # noqa: E501

        :return: The created_datetime of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this InlineResponse20016.

        Datetime when the last unmodified annotation was created.  # noqa: E501

        :param created_datetime: The created_datetime of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._created_datetime = created_datetime

    @property
    def description(self):
        """Gets the description of this InlineResponse20016.  # noqa: E501

        Description of the version.  # noqa: E501

        :return: The description of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20016.

        Description of the version.  # noqa: E501

        :param description: The description of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this InlineResponse20016.  # noqa: E501

        Unique integer identifying a membership.  # noqa: E501

        :return: The id of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20016.

        Unique integer identifying a membership.  # noqa: E501

        :param id: The id of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def modified_by(self):
        """Gets the modified_by of this InlineResponse20016.  # noqa: E501

        Name of user who modified annotations in this version most recently.  # noqa: E501

        :return: The modified_by of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this InlineResponse20016.

        Name of user who modified annotations in this version most recently.  # noqa: E501

        :param modified_by: The modified_by of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def modified_datetime(self):
        """Gets the modified_datetime of this InlineResponse20016.  # noqa: E501

        Datetime when last annotation was modified in the web interface.  # noqa: E501

        :return: The modified_datetime of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._modified_datetime

    @modified_datetime.setter
    def modified_datetime(self, modified_datetime):
        """Sets the modified_datetime of this InlineResponse20016.

        Datetime when last annotation was modified in the web interface.  # noqa: E501

        :param modified_datetime: The modified_datetime of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._modified_datetime = modified_datetime

    @property
    def name(self):
        """Gets the name of this InlineResponse20016.  # noqa: E501

        Name of the version.  # noqa: E501

        :return: The name of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20016.

        Name of the version.  # noqa: E501

        :param name: The name of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_created(self):
        """Gets the num_created of this InlineResponse20016.  # noqa: E501

        Number of created annotations in this version.  # noqa: E501

        :return: The num_created of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._num_created

    @num_created.setter
    def num_created(self, num_created):
        """Sets the num_created of this InlineResponse20016.

        Number of created annotations in this version.  # noqa: E501

        :param num_created: The num_created of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._num_created = num_created

    @property
    def num_modified(self):
        """Gets the num_modified of this InlineResponse20016.  # noqa: E501

        Number of modified annotations in this version.  # noqa: E501

        :return: The num_modified of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._num_modified

    @num_modified.setter
    def num_modified(self, num_modified):
        """Sets the num_modified of this InlineResponse20016.

        Number of modified annotations in this version.  # noqa: E501

        :param num_modified: The num_modified of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._num_modified = num_modified

    @property
    def number(self):
        """Gets the number of this InlineResponse20016.  # noqa: E501

        Version number.  # noqa: E501

        :return: The number of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponse20016.

        Version number.  # noqa: E501

        :param number: The number of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def project(self):
        """Gets the project of this InlineResponse20016.  # noqa: E501

        Unique integer identifying a project.  # noqa: E501

        :return: The project of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this InlineResponse20016.

        Unique integer identifying a project.  # noqa: E501

        :param project: The project of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def show_empty(self):
        """Gets the show_empty of this InlineResponse20016.  # noqa: E501

        Whether to show this version on media for which no annotations exist.  # noqa: E501

        :return: The show_empty of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_empty

    @show_empty.setter
    def show_empty(self, show_empty):
        """Sets the show_empty of this InlineResponse20016.

        Whether to show this version on media for which no annotations exist.  # noqa: E501

        :param show_empty: The show_empty of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_empty = show_empty

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
        if issubclass(InlineResponse20016, dict):
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
        if not isinstance(other, InlineResponse20016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
