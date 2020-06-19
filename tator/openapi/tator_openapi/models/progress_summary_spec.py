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


class ProgressSummarySpec(object):
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
        'gid': 'str',
        'num_complete': 'int',
        'num_jobs': 'int'
    }

    attribute_map = {
        'gid': 'gid',
        'num_complete': 'num_complete',
        'num_jobs': 'num_jobs'
    }

    def __init__(self, gid=None, num_complete=None, num_jobs=None, local_vars_configuration=None):  # noqa: E501
        """ProgressSummarySpec - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gid = None
        self._num_complete = None
        self._num_jobs = None
        self.discriminator = None

        self.gid = gid
        self.num_complete = num_complete
        self.num_jobs = num_jobs

    @property
    def gid(self):
        """
        UUID generated for the job group. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.

        :return: The gid of this ProgressSummarySpec. 
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        UUID generated for the job group. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.

        :param gid: The gid of this ProgressSummarySpec.
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and gid is None:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must not be `None`")  # noqa: E501

        self._gid = gid

    @property
    def num_complete(self):
        """
        Number of jobs completed in this job group.

        :return: The num_complete of this ProgressSummarySpec. 
        :rtype: int
        """
        return self._num_complete

    @num_complete.setter
    def num_complete(self, num_complete):
        """
        Number of jobs completed in this job group.

        :param num_complete: The num_complete of this ProgressSummarySpec.
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and num_complete is None:  # noqa: E501
            raise ValueError("Invalid value for `num_complete`, must not be `None`")  # noqa: E501

        self._num_complete = num_complete

    @property
    def num_jobs(self):
        """
        Number of jobs in this job group.

        :return: The num_jobs of this ProgressSummarySpec. 
        :rtype: int
        """
        return self._num_jobs

    @num_jobs.setter
    def num_jobs(self, num_jobs):
        """
        Number of jobs in this job group.

        :param num_jobs: The num_jobs of this ProgressSummarySpec.
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and num_jobs is None:  # noqa: E501
            raise ValueError("Invalid value for `num_jobs`, must not be `None`")  # noqa: E501

        self._num_jobs = num_jobs

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
        if not isinstance(other, ProgressSummarySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProgressSummarySpec):
            return True

        return self.to_dict() != other.to_dict()
