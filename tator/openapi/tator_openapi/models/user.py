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


class User(object):
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
        'email': 'str',
        'first_name': 'str',
        'id': 'int',
        'last_name': 'str',
        'username': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'id': 'id',
        'last_name': 'last_name',
        'username': 'username'
    }

    def __init__(self, email=None, first_name=None, id=None, last_name=None, username=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._first_name = None
        self._id = None
        self._last_name = None
        self._username = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if id is not None:
            self.id = id
        if last_name is not None:
            self.last_name = last_name
        if username is not None:
            self.username = username

    @property
    def email(self):
        """
        Email address of user.

        :return: The email of this User. 
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Email address of user.

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        First name of user.

        :return: The first_name of this User. 
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        First name of user.

        :param first_name: The first_name of this User.
        :type: str
        """

        self._first_name = first_name

    @property
    def id(self):
        """
        Unique integer identifying a user.

        :return: The id of this User. 
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Unique integer identifying a user.

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def last_name(self):
        """
        Last name of user.

        :return: The last_name of this User. 
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Last name of user.

        :param last_name: The last_name of this User.
        :type: str
        """

        self._last_name = last_name

    @property
    def username(self):
        """
        Username of user.

        :return: The username of this User. 
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Username of user.

        :param username: The username of this User.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
