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


class EscalationRepeat(object):
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
        'wait_interval': 'int',
        'count': 'int',
        'reset_recipient_states': 'bool',
        'close_alert_after_all': 'bool'
    }

    attribute_map = {
        'wait_interval': 'waitInterval',
        'count': 'count',
        'reset_recipient_states': 'resetRecipientStates',
        'close_alert_after_all': 'closeAlertAfterAll'
    }

    def __init__(self, wait_interval=None, count=None, reset_recipient_states=None, close_alert_after_all=None):  # noqa: E501
        """EscalationRepeat - a model defined in Swagger"""  # noqa: E501

        self._wait_interval = None
        self._count = None
        self._reset_recipient_states = None
        self._close_alert_after_all = None
        self.discriminator = None

        if wait_interval is not None:
            self.wait_interval = wait_interval
        if count is not None:
            self.count = count
        if reset_recipient_states is not None:
            self.reset_recipient_states = reset_recipient_states
        if close_alert_after_all is not None:
            self.close_alert_after_all = close_alert_after_all

    @property
    def wait_interval(self):
        """Gets the wait_interval of this EscalationRepeat.  # noqa: E501


        :return: The wait_interval of this EscalationRepeat.  # noqa: E501
        :rtype: int
        """
        return self._wait_interval

    @wait_interval.setter
    def wait_interval(self, wait_interval):
        """Sets the wait_interval of this EscalationRepeat.


        :param wait_interval: The wait_interval of this EscalationRepeat.  # noqa: E501
        :type: int
        """

        self._wait_interval = wait_interval

    @property
    def count(self):
        """Gets the count of this EscalationRepeat.  # noqa: E501


        :return: The count of this EscalationRepeat.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EscalationRepeat.


        :param count: The count of this EscalationRepeat.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def reset_recipient_states(self):
        """Gets the reset_recipient_states of this EscalationRepeat.  # noqa: E501


        :return: The reset_recipient_states of this EscalationRepeat.  # noqa: E501
        :rtype: bool
        """
        return self._reset_recipient_states

    @reset_recipient_states.setter
    def reset_recipient_states(self, reset_recipient_states):
        """Sets the reset_recipient_states of this EscalationRepeat.


        :param reset_recipient_states: The reset_recipient_states of this EscalationRepeat.  # noqa: E501
        :type: bool
        """

        self._reset_recipient_states = reset_recipient_states

    @property
    def close_alert_after_all(self):
        """Gets the close_alert_after_all of this EscalationRepeat.  # noqa: E501


        :return: The close_alert_after_all of this EscalationRepeat.  # noqa: E501
        :rtype: bool
        """
        return self._close_alert_after_all

    @close_alert_after_all.setter
    def close_alert_after_all(self, close_alert_after_all):
        """Sets the close_alert_after_all of this EscalationRepeat.


        :param close_alert_after_all: The close_alert_after_all of this EscalationRepeat.  # noqa: E501
        :type: bool
        """

        self._close_alert_after_all = close_alert_after_all

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
        if not isinstance(other, EscalationRepeat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
