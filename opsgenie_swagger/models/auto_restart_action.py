# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from opsgenie_swagger.models.duration import Duration  # noqa: F401,E501


class AutoRestartAction(object):
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
        'duration': 'Duration',
        'max_repeat_count': 'int'
    }

    attribute_map = {
        'duration': 'duration',
        'max_repeat_count': 'maxRepeatCount'
    }

    def __init__(self, duration=None, max_repeat_count=None):  # noqa: E501
        """AutoRestartAction - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._max_repeat_count = None
        self.discriminator = None

        self.duration = duration
        self.max_repeat_count = max_repeat_count

    @property
    def duration(self):
        """Gets the duration of this AutoRestartAction.  # noqa: E501


        :return: The duration of this AutoRestartAction.  # noqa: E501
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AutoRestartAction.


        :param duration: The duration of this AutoRestartAction.  # noqa: E501
        :type: Duration
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def max_repeat_count(self):
        """Gets the max_repeat_count of this AutoRestartAction.  # noqa: E501


        :return: The max_repeat_count of this AutoRestartAction.  # noqa: E501
        :rtype: int
        """
        return self._max_repeat_count

    @max_repeat_count.setter
    def max_repeat_count(self, max_repeat_count):
        """Sets the max_repeat_count of this AutoRestartAction.


        :param max_repeat_count: The max_repeat_count of this AutoRestartAction.  # noqa: E501
        :type: int
        """
        if max_repeat_count is None:
            raise ValueError("Invalid value for `max_repeat_count`, must not be `None`")  # noqa: E501

        self._max_repeat_count = max_repeat_count

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoRestartAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
