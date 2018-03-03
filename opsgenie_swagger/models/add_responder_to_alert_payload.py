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

from opsgenie_swagger.models.alert_action_payload import AlertActionPayload  # noqa: F401,E501
from opsgenie_swagger.models.recipient import Recipient  # noqa: F401,E501


class AddResponderToAlertPayload(object):
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
        'user': 'str',
        'note': 'str',
        'source': 'str',
        'responder': 'Recipient'
    }

    attribute_map = {
        'user': 'user',
        'note': 'note',
        'source': 'source',
        'responder': 'responder'
    }

    def __init__(self, user=None, note=None, source=None, responder=None):  # noqa: E501
        """AddResponderToAlertPayload - a model defined in Swagger"""  # noqa: E501

        self._user = None
        self._note = None
        self._source = None
        self._responder = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if note is not None:
            self.note = note
        if source is not None:
            self.source = source
        self.responder = responder

    @property
    def user(self):
        """Gets the user of this AddResponderToAlertPayload.  # noqa: E501

        Display name of the request owner  # noqa: E501

        :return: The user of this AddResponderToAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AddResponderToAlertPayload.

        Display name of the request owner  # noqa: E501

        :param user: The user of this AddResponderToAlertPayload.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def note(self):
        """Gets the note of this AddResponderToAlertPayload.  # noqa: E501

        Additional note that will be added while creating the alert  # noqa: E501

        :return: The note of this AddResponderToAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AddResponderToAlertPayload.

        Additional note that will be added while creating the alert  # noqa: E501

        :param note: The note of this AddResponderToAlertPayload.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def source(self):
        """Gets the source of this AddResponderToAlertPayload.  # noqa: E501

        Source field of the alert. Default value is IP address of the incoming request  # noqa: E501

        :return: The source of this AddResponderToAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AddResponderToAlertPayload.

        Source field of the alert. Default value is IP address of the incoming request  # noqa: E501

        :param source: The source of this AddResponderToAlertPayload.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def responder(self):
        """Gets the responder of this AddResponderToAlertPayload.  # noqa: E501


        :return: The responder of this AddResponderToAlertPayload.  # noqa: E501
        :rtype: Recipient
        """
        return self._responder

    @responder.setter
    def responder(self, responder):
        """Sets the responder of this AddResponderToAlertPayload.


        :param responder: The responder of this AddResponderToAlertPayload.  # noqa: E501
        :type: Recipient
        """
        if responder is None:
            raise ValueError("Invalid value for `responder`, must not be `None`")  # noqa: E501

        self._responder = responder

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
        if not isinstance(other, AddResponderToAlertPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
