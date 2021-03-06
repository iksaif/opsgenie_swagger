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

from opsgenie_swagger.models.schedule_rotation import ScheduleRotation  # noqa: F401,E501
from opsgenie_swagger.models.team_meta import TeamMeta  # noqa: F401,E501


class Schedule(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'timezone': 'str',
        'enabled': 'bool',
        'owner_team': 'TeamMeta',
        'rotations': 'list[ScheduleRotation]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'timezone': 'timezone',
        'enabled': 'enabled',
        'owner_team': 'ownerTeam',
        'rotations': 'rotations'
    }

    def __init__(self, id=None, name=None, description=None, timezone=None, enabled=None, owner_team=None, rotations=None):  # noqa: E501
        """Schedule - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._timezone = None
        self._enabled = None
        self._owner_team = None
        self._rotations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if timezone is not None:
            self.timezone = timezone
        if enabled is not None:
            self.enabled = enabled
        if owner_team is not None:
            self.owner_team = owner_team
        if rotations is not None:
            self.rotations = rotations

    @property
    def id(self):
        """Gets the id of this Schedule.  # noqa: E501


        :return: The id of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schedule.


        :param id: The id of this Schedule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Schedule.  # noqa: E501


        :return: The name of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Schedule.


        :param name: The name of this Schedule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Schedule.  # noqa: E501


        :return: The description of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Schedule.


        :param description: The description of this Schedule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def timezone(self):
        """Gets the timezone of this Schedule.  # noqa: E501


        :return: The timezone of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Schedule.


        :param timezone: The timezone of this Schedule.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def enabled(self):
        """Gets the enabled of this Schedule.  # noqa: E501


        :return: The enabled of this Schedule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Schedule.


        :param enabled: The enabled of this Schedule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def owner_team(self):
        """Gets the owner_team of this Schedule.  # noqa: E501


        :return: The owner_team of this Schedule.  # noqa: E501
        :rtype: TeamMeta
        """
        return self._owner_team

    @owner_team.setter
    def owner_team(self, owner_team):
        """Sets the owner_team of this Schedule.


        :param owner_team: The owner_team of this Schedule.  # noqa: E501
        :type: TeamMeta
        """

        self._owner_team = owner_team

    @property
    def rotations(self):
        """Gets the rotations of this Schedule.  # noqa: E501


        :return: The rotations of this Schedule.  # noqa: E501
        :rtype: list[ScheduleRotation]
        """
        return self._rotations

    @rotations.setter
    def rotations(self, rotations):
        """Sets the rotations of this Schedule.


        :param rotations: The rotations of this Schedule.  # noqa: E501
        :type: list[ScheduleRotation]
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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
