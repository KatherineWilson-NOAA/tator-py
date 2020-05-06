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


class InlineObject5(object):
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
        'description': 'str',
        'dtype': 'str',
        'file_format': 'str',
        'keep_original': 'bool',
        'name': 'str',
        'uploadable': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'dtype': 'dtype',
        'file_format': 'file_format',
        'keep_original': 'keep_original',
        'name': 'name',
        'uploadable': 'uploadable'
    }

    def __init__(self, description='', dtype=None, file_format=None, keep_original=True, name=None, uploadable=True, local_vars_configuration=None):  # noqa: E501
        """InlineObject5 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._dtype = None
        self._file_format = None
        self._keep_original = None
        self._name = None
        self._uploadable = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.dtype = dtype
        if file_format is not None:
            self.file_format = file_format
        if keep_original is not None:
            self.keep_original = keep_original
        self.name = name
        if uploadable is not None:
            self.uploadable = uploadable

    @property
    def description(self):
        """Gets the description of this InlineObject5.  # noqa: E501

        Description of the media type.  # noqa: E501

        :return: The description of this InlineObject5.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject5.

        Description of the media type.  # noqa: E501

        :param description: The description of this InlineObject5.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dtype(self):
        """Gets the dtype of this InlineObject5.  # noqa: E501

        Type of the media, image or video.  # noqa: E501

        :return: The dtype of this InlineObject5.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this InlineObject5.

        Type of the media, image or video.  # noqa: E501

        :param dtype: The dtype of this InlineObject5.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dtype is None:  # noqa: E501
            raise ValueError("Invalid value for `dtype`, must not be `None`")  # noqa: E501
        allowed_values = ["image", "video"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dtype not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dtype` ({0}), must be one of {1}"  # noqa: E501
                .format(dtype, allowed_values)
            )

        self._dtype = dtype

    @property
    def file_format(self):
        """Gets the file_format of this InlineObject5.  # noqa: E501

        File extension. If omitted, any recognized file extension for the given dtype is accepted for upload. Do not include a dot prefix.  # noqa: E501

        :return: The file_format of this InlineObject5.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this InlineObject5.

        File extension. If omitted, any recognized file extension for the given dtype is accepted for upload. Do not include a dot prefix.  # noqa: E501

        :param file_format: The file_format of this InlineObject5.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_format is not None and len(file_format) > 4):
            raise ValueError("Invalid value for `file_format`, length must be less than or equal to `4`")  # noqa: E501

        self._file_format = file_format

    @property
    def keep_original(self):
        """Gets the keep_original of this InlineObject5.  # noqa: E501

        For video dtype, whether to keep the original video file for archival purposes after transcoding. If true, the originally uploaded file will be available for download, otherwise downloads will use the transcoded videos.  # noqa: E501

        :return: The keep_original of this InlineObject5.  # noqa: E501
        :rtype: bool
        """
        return self._keep_original

    @keep_original.setter
    def keep_original(self, keep_original):
        """Sets the keep_original of this InlineObject5.

        For video dtype, whether to keep the original video file for archival purposes after transcoding. If true, the originally uploaded file will be available for download, otherwise downloads will use the transcoded videos.  # noqa: E501

        :param keep_original: The keep_original of this InlineObject5.  # noqa: E501
        :type: bool
        """

        self._keep_original = keep_original

    @property
    def name(self):
        """Gets the name of this InlineObject5.  # noqa: E501

        Name of the media type.  # noqa: E501

        :return: The name of this InlineObject5.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject5.

        Name of the media type.  # noqa: E501

        :param name: The name of this InlineObject5.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uploadable(self):
        """Gets the uploadable of this InlineObject5.  # noqa: E501

        Whether this media can be uploaded.  # noqa: E501

        :return: The uploadable of this InlineObject5.  # noqa: E501
        :rtype: bool
        """
        return self._uploadable

    @uploadable.setter
    def uploadable(self, uploadable):
        """Sets the uploadable of this InlineObject5.

        Whether this media can be uploaded.  # noqa: E501

        :param uploadable: The uploadable of this InlineObject5.  # noqa: E501
        :type: bool
        """

        self._uploadable = uploadable

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
        if not isinstance(other, InlineObject5):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject5):
            return True

        return self.to_dict() != other.to_dict()
