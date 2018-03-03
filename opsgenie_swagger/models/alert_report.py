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


class AlertReport(object):
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
        'ack_time': 'int',
        'close_time': 'int',
        'acknowledged_by': 'str',
        'closed_by': 'str'
    }

    attribute_map = {
        'ack_time': 'ackTime',
        'close_time': 'closeTime',
        'acknowledged_by': 'acknowledgedBy',
        'closed_by': 'closedBy'
    }

    def __init__(self, ack_time=None, close_time=None, acknowledged_by=None, closed_by=None):  # noqa: E501
        """AlertReport - a model defined in Swagger"""  # noqa: E501

        self._ack_time = None
        self._close_time = None
        self._acknowledged_by = None
        self._closed_by = None
        self.discriminator = None

        if ack_time is not None:
            self.ack_time = ack_time
        if close_time is not None:
            self.close_time = close_time
        if acknowledged_by is not None:
            self.acknowledged_by = acknowledged_by
        if closed_by is not None:
            self.closed_by = closed_by

    @property
    def ack_time(self):
        """Gets the ack_time of this AlertReport.  # noqa: E501


        :return: The ack_time of this AlertReport.  # noqa: E501
        :rtype: int
        """
        return self._ack_time

    @ack_time.setter
    def ack_time(self, ack_time):
        """Sets the ack_time of this AlertReport.


        :param ack_time: The ack_time of this AlertReport.  # noqa: E501
        :type: int
        """

        self._ack_time = ack_time

    @property
    def close_time(self):
        """Gets the close_time of this AlertReport.  # noqa: E501


        :return: The close_time of this AlertReport.  # noqa: E501
        :rtype: int
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this AlertReport.


        :param close_time: The close_time of this AlertReport.  # noqa: E501
        :type: int
        """

        self._close_time = close_time

    @property
    def acknowledged_by(self):
        """Gets the acknowledged_by of this AlertReport.  # noqa: E501


        :return: The acknowledged_by of this AlertReport.  # noqa: E501
        :rtype: str
        """
        return self._acknowledged_by

    @acknowledged_by.setter
    def acknowledged_by(self, acknowledged_by):
        """Sets the acknowledged_by of this AlertReport.


        :param acknowledged_by: The acknowledged_by of this AlertReport.  # noqa: E501
        :type: str
        """

        self._acknowledged_by = acknowledged_by

    @property
    def closed_by(self):
        """Gets the closed_by of this AlertReport.  # noqa: E501


        :return: The closed_by of this AlertReport.  # noqa: E501
        :rtype: str
        """
        return self._closed_by

    @closed_by.setter
    def closed_by(self, closed_by):
        """Sets the closed_by of this AlertReport.


        :param closed_by: The closed_by of this AlertReport.  # noqa: E501
        :type: str
        """

        self._closed_by = closed_by

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
        if not isinstance(other, AlertReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
