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

from opsgenie_swagger.models.recipient import Recipient  # noqa: F401,E501
from opsgenie_swagger.models.schedule_override_rotation import ScheduleOverrideRotation  # noqa: F401,E501


class CreateScheduleOverridePayload(object):
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
        'alias': 'str',
        'user': 'Recipient',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'rotations': 'list[ScheduleOverrideRotation]'
    }

    attribute_map = {
        'alias': 'alias',
        'user': 'user',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'rotations': 'rotations'
    }

    def __init__(self, alias=None, user=None, start_date=None, end_date=None, rotations=None):  # noqa: E501
        """CreateScheduleOverridePayload - a model defined in Swagger"""  # noqa: E501

        self._alias = None
        self._user = None
        self._start_date = None
        self._end_date = None
        self._rotations = None
        self.discriminator = None

        self.alias = alias
        self.user = user
        self.start_date = start_date
        self.end_date = end_date
        if rotations is not None:
            self.rotations = rotations

    @property
    def alias(self):
        """Gets the alias of this CreateScheduleOverridePayload.  # noqa: E501

        A user defined identifier for the override  # noqa: E501

        :return: The alias of this CreateScheduleOverridePayload.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CreateScheduleOverridePayload.

        A user defined identifier for the override  # noqa: E501

        :param alias: The alias of this CreateScheduleOverridePayload.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def user(self):
        """Gets the user of this CreateScheduleOverridePayload.  # noqa: E501

        The user object who will take on call responsibility or reserved word none  # noqa: E501

        :return: The user of this CreateScheduleOverridePayload.  # noqa: E501
        :rtype: Recipient
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CreateScheduleOverridePayload.

        The user object who will take on call responsibility or reserved word none  # noqa: E501

        :param user: The user of this CreateScheduleOverridePayload.  # noqa: E501
        :type: Recipient
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def start_date(self):
        """Gets the start_date of this CreateScheduleOverridePayload.  # noqa: E501

        Time for override starting  # noqa: E501

        :return: The start_date of this CreateScheduleOverridePayload.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreateScheduleOverridePayload.

        Time for override starting  # noqa: E501

        :param start_date: The start_date of this CreateScheduleOverridePayload.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CreateScheduleOverridePayload.  # noqa: E501

        Time for override ending  # noqa: E501

        :return: The end_date of this CreateScheduleOverridePayload.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreateScheduleOverridePayload.

        Time for override ending  # noqa: E501

        :param end_date: The end_date of this CreateScheduleOverridePayload.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def rotations(self):
        """Gets the rotations of this CreateScheduleOverridePayload.  # noqa: E501

        Identifier (id or name) of rotations that override will apply. When it's set, only specified schedule rotations will be overridden  # noqa: E501

        :return: The rotations of this CreateScheduleOverridePayload.  # noqa: E501
        :rtype: list[ScheduleOverrideRotation]
        """
        return self._rotations

    @rotations.setter
    def rotations(self, rotations):
        """Sets the rotations of this CreateScheduleOverridePayload.

        Identifier (id or name) of rotations that override will apply. When it's set, only specified schedule rotations will be overridden  # noqa: E501

        :param rotations: The rotations of this CreateScheduleOverridePayload.  # noqa: E501
        :type: list[ScheduleOverrideRotation]
        """

        self._rotations = rotations

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
        if not isinstance(other, CreateScheduleOverridePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
