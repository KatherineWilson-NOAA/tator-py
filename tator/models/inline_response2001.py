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


class InlineResponse2001(object):
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
        'attributes': 'dict(str, object)',
        'created_by_id': 'int',
        'created_datetime': 'str',
        'id': 'int',
        'image_thumbnail': 'str',
        'last_edit_end': 'datetime',
        'last_edit_start': 'datetime',
        'md5': 'str',
        'meta': 'int',
        'modified_by_id': 'int',
        'modified_datetime': 'str',
        'name': 'str',
        'original_url': 'str',
        'project': 'int',
        'url': 'str',
        'video_thumbnail': 'str',
        'video_thumbnail_gif': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'created_by_id': 'created_by_id',
        'created_datetime': 'created_datetime',
        'id': 'id',
        'image_thumbnail': 'image_thumbnail',
        'last_edit_end': 'last_edit_end',
        'last_edit_start': 'last_edit_start',
        'md5': 'md5',
        'meta': 'meta',
        'modified_by_id': 'modified_by_id',
        'modified_datetime': 'modified_datetime',
        'name': 'name',
        'original_url': 'original_url',
        'project': 'project',
        'url': 'url',
        'video_thumbnail': 'video_thumbnail',
        'video_thumbnail_gif': 'video_thumbnail_gif'
    }

    def __init__(self, attributes=None, created_by_id=None, created_datetime=None, id=None, image_thumbnail=None, last_edit_end=None, last_edit_start=None, md5=None, meta=None, modified_by_id=None, modified_datetime=None, name=None, original_url=None, project=None, url=None, video_thumbnail=None, video_thumbnail_gif=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._created_by_id = None
        self._created_datetime = None
        self._id = None
        self._image_thumbnail = None
        self._last_edit_end = None
        self._last_edit_start = None
        self._md5 = None
        self._meta = None
        self._modified_by_id = None
        self._modified_datetime = None
        self._name = None
        self._original_url = None
        self._project = None
        self._url = None
        self._video_thumbnail = None
        self._video_thumbnail_gif = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if id is not None:
            self.id = id
        if image_thumbnail is not None:
            self.image_thumbnail = image_thumbnail
        if last_edit_end is not None:
            self.last_edit_end = last_edit_end
        if last_edit_start is not None:
            self.last_edit_start = last_edit_start
        if md5 is not None:
            self.md5 = md5
        if meta is not None:
            self.meta = meta
        if modified_by_id is not None:
            self.modified_by_id = modified_by_id
        if modified_datetime is not None:
            self.modified_datetime = modified_datetime
        if name is not None:
            self.name = name
        if original_url is not None:
            self.original_url = original_url
        if project is not None:
            self.project = project
        if url is not None:
            self.url = url
        if video_thumbnail is not None:
            self.video_thumbnail = video_thumbnail
        if video_thumbnail_gif is not None:
            self.video_thumbnail_gif = video_thumbnail_gif

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse2001.  # noqa: E501

        Object containing attribute values.  # noqa: E501

        :return: The attributes of this InlineResponse2001.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse2001.

        Object containing attribute values.  # noqa: E501

        :param attributes: The attributes of this InlineResponse2001.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def created_by_id(self):
        """Gets the created_by_id of this InlineResponse2001.  # noqa: E501

        Unique integer identifying user who created this media.  # noqa: E501

        :return: The created_by_id of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this InlineResponse2001.

        Unique integer identifying user who created this media.  # noqa: E501

        :param created_by_id: The created_by_id of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def created_datetime(self):
        """Gets the created_datetime of this InlineResponse2001.  # noqa: E501

        Datetime when this media was created.  # noqa: E501

        :return: The created_datetime of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this InlineResponse2001.

        Datetime when this media was created.  # noqa: E501

        :param created_datetime: The created_datetime of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._created_datetime = created_datetime

    @property
    def id(self):
        """Gets the id of this InlineResponse2001.  # noqa: E501

        Unique integer identifying this media.  # noqa: E501

        :return: The id of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2001.

        Unique integer identifying this media.  # noqa: E501

        :param id: The id of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image_thumbnail(self):
        """Gets the image_thumbnail of this InlineResponse2001.  # noqa: E501

        URL of image thumbnail.  # noqa: E501

        :return: The image_thumbnail of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._image_thumbnail

    @image_thumbnail.setter
    def image_thumbnail(self, image_thumbnail):
        """Sets the image_thumbnail of this InlineResponse2001.

        URL of image thumbnail.  # noqa: E501

        :param image_thumbnail: The image_thumbnail of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._image_thumbnail = image_thumbnail

    @property
    def last_edit_end(self):
        """Gets the last_edit_end of this InlineResponse2001.  # noqa: E501

        Datetime of the end of the session when this media or its annotations were last edited.  # noqa: E501

        :return: The last_edit_end of this InlineResponse2001.  # noqa: E501
        :rtype: datetime
        """
        return self._last_edit_end

    @last_edit_end.setter
    def last_edit_end(self, last_edit_end):
        """Sets the last_edit_end of this InlineResponse2001.

        Datetime of the end of the session when this media or its annotations were last edited.  # noqa: E501

        :param last_edit_end: The last_edit_end of this InlineResponse2001.  # noqa: E501
        :type: datetime
        """

        self._last_edit_end = last_edit_end

    @property
    def last_edit_start(self):
        """Gets the last_edit_start of this InlineResponse2001.  # noqa: E501

        Datetime of the start of the session when this media or its annotations were last edited.  # noqa: E501

        :return: The last_edit_start of this InlineResponse2001.  # noqa: E501
        :rtype: datetime
        """
        return self._last_edit_start

    @last_edit_start.setter
    def last_edit_start(self, last_edit_start):
        """Sets the last_edit_start of this InlineResponse2001.

        Datetime of the start of the session when this media or its annotations were last edited.  # noqa: E501

        :param last_edit_start: The last_edit_start of this InlineResponse2001.  # noqa: E501
        :type: datetime
        """

        self._last_edit_start = last_edit_start

    @property
    def md5(self):
        """Gets the md5 of this InlineResponse2001.  # noqa: E501

        MD5 checksum of the media file.  # noqa: E501

        :return: The md5 of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this InlineResponse2001.

        MD5 checksum of the media file.  # noqa: E501

        :param md5: The md5 of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def meta(self):
        """Gets the meta of this InlineResponse2001.  # noqa: E501

        Unique integer identifying entity type of this media.  # noqa: E501

        :return: The meta of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this InlineResponse2001.

        Unique integer identifying entity type of this media.  # noqa: E501

        :param meta: The meta of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._meta = meta

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this InlineResponse2001.  # noqa: E501

        Unique integer identifying user who last modified this media.  # noqa: E501

        :return: The modified_by_id of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this InlineResponse2001.

        Unique integer identifying user who last modified this media.  # noqa: E501

        :param modified_by_id: The modified_by_id of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._modified_by_id = modified_by_id

    @property
    def modified_datetime(self):
        """Gets the modified_datetime of this InlineResponse2001.  # noqa: E501

        Datetime when this media was last modified.  # noqa: E501

        :return: The modified_datetime of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._modified_datetime

    @modified_datetime.setter
    def modified_datetime(self, modified_datetime):
        """Sets the modified_datetime of this InlineResponse2001.

        Datetime when this media was last modified.  # noqa: E501

        :param modified_datetime: The modified_datetime of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._modified_datetime = modified_datetime

    @property
    def name(self):
        """Gets the name of this InlineResponse2001.  # noqa: E501

        Name of the media.  # noqa: E501

        :return: The name of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2001.

        Name of the media.  # noqa: E501

        :param name: The name of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def original_url(self):
        """Gets the original_url of this InlineResponse2001.  # noqa: E501

        URL of original video, if it exists.  # noqa: E501

        :return: The original_url of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._original_url

    @original_url.setter
    def original_url(self, original_url):
        """Sets the original_url of this InlineResponse2001.

        URL of original video, if it exists.  # noqa: E501

        :param original_url: The original_url of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._original_url = original_url

    @property
    def project(self):
        """Gets the project of this InlineResponse2001.  # noqa: E501

        Unique integer identifying project of this media.  # noqa: E501

        :return: The project of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this InlineResponse2001.

        Unique integer identifying project of this media.  # noqa: E501

        :param project: The project of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def url(self):
        """Gets the url of this InlineResponse2001.  # noqa: E501

        URL of the media file.  # noqa: E501

        :return: The url of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse2001.

        URL of the media file.  # noqa: E501

        :param url: The url of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def video_thumbnail(self):
        """Gets the video_thumbnail of this InlineResponse2001.  # noqa: E501

        URL of video thumbnail.  # noqa: E501

        :return: The video_thumbnail of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._video_thumbnail

    @video_thumbnail.setter
    def video_thumbnail(self, video_thumbnail):
        """Sets the video_thumbnail of this InlineResponse2001.

        URL of video thumbnail.  # noqa: E501

        :param video_thumbnail: The video_thumbnail of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._video_thumbnail = video_thumbnail

    @property
    def video_thumbnail_gif(self):
        """Gets the video_thumbnail_gif of this InlineResponse2001.  # noqa: E501

        URL of video thumbnail gif.  # noqa: E501

        :return: The video_thumbnail_gif of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._video_thumbnail_gif

    @video_thumbnail_gif.setter
    def video_thumbnail_gif(self, video_thumbnail_gif):
        """Sets the video_thumbnail_gif of this InlineResponse2001.

        URL of video thumbnail gif.  # noqa: E501

        :param video_thumbnail_gif: The video_thumbnail_gif of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._video_thumbnail_gif = video_thumbnail_gif

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
