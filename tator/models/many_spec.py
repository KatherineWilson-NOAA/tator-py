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


class ManySpec(object):
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
        'frame': 'int',
        'many': 'list[OneOfmapmapmap]',
        'media_id': 'int',
        'modified': 'bool',
        'type': 'int',
        'version': 'int'
    }

    attribute_map = {
        'frame': 'frame',
        'many': 'many',
        'media_id': 'media_id',
        'modified': 'modified',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, frame=None, many=None, media_id=None, modified=False, type=None, version=None, local_vars_configuration=None):  # noqa: E501
        """ManySpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._frame = None
        self._many = None
        self._media_id = None
        self._modified = None
        self._type = None
        self._version = None
        self.discriminator = None

        if frame is not None:
            self.frame = frame
        self.many = many
        self.media_id = media_id
        if modified is not None:
            self.modified = modified
        self.type = type
        if version is not None:
            self.version = version

    @property
    def frame(self):
        """Gets the frame of this ManySpec.  # noqa: E501

        Frame number of this localization if it is in a video.  # noqa: E501

        :return: The frame of this ManySpec.  # noqa: E501
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this ManySpec.

        Frame number of this localization if it is in a video.  # noqa: E501

        :param frame: The frame of this ManySpec.  # noqa: E501
        :type: int
        """

        self._frame = frame

    @property
    def many(self):
        """Gets the many of this ManySpec.  # noqa: E501

        List of localizations if this request is for bulkcreate.  # noqa: E501

        :return: The many of this ManySpec.  # noqa: E501
        :rtype: list[OneOfmapmapmap]
        """
        return self._many

    @many.setter
    def many(self, many):
        """Sets the many of this ManySpec.

        List of localizations if this request is for bulkcreate.  # noqa: E501

        :param many: The many of this ManySpec.  # noqa: E501
        :type: list[OneOfmapmapmap]
        """
        if self.local_vars_configuration.client_side_validation and many is None:  # noqa: E501
            raise ValueError("Invalid value for `many`, must not be `None`")  # noqa: E501

        self._many = many

    @property
    def media_id(self):
        """Gets the media_id of this ManySpec.  # noqa: E501

        Unique integer identifying a media. Required if `many` is not given.  # noqa: E501

        :return: The media_id of this ManySpec.  # noqa: E501
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this ManySpec.

        Unique integer identifying a media. Required if `many` is not given.  # noqa: E501

        :param media_id: The media_id of this ManySpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and media_id is None:  # noqa: E501
            raise ValueError("Invalid value for `media_id`, must not be `None`")  # noqa: E501

        self._media_id = media_id

    @property
    def modified(self):
        """Gets the modified of this ManySpec.  # noqa: E501

        Whether this localization was created in the web UI.  # noqa: E501

        :return: The modified of this ManySpec.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ManySpec.

        Whether this localization was created in the web UI.  # noqa: E501

        :param modified: The modified of this ManySpec.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    @property
    def type(self):
        """Gets the type of this ManySpec.  # noqa: E501

        Unique integer identifying a localization type.Required if `many` is not given.  # noqa: E501

        :return: The type of this ManySpec.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ManySpec.

        Unique integer identifying a localization type.Required if `many` is not given.  # noqa: E501

        :param type: The type of this ManySpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def version(self):
        """Gets the version of this ManySpec.  # noqa: E501

        Unique integer identifying the version.  # noqa: E501

        :return: The version of this ManySpec.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ManySpec.

        Unique integer identifying the version.  # noqa: E501

        :param version: The version of this ManySpec.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, ManySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManySpec):
            return True

        return self.to_dict() != other.to_dict()
