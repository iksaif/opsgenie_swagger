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

from opsgenie_swagger.models.alert_filter import AlertFilter  # noqa: F401,E501
from opsgenie_swagger.models.outgoing_callback import OutgoingCallback  # noqa: F401,E501


class FlowdockCallback(object):
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
        'flowdock_api_token': 'str',
        'flowdock_tags': 'dict(str, str)',
        'external_username': 'str'
    }

    attribute_map = {
        'flowdock_api_token': 'flowdockApiToken',
        'flowdock_tags': 'flowdockTags',
        'external_username': 'externalUsername'
    }

    def __init__(self, flowdock_api_token=None, flowdock_tags=None, external_username=None):  # noqa: E501
        """FlowdockCallback - a model defined in Swagger"""  # noqa: E501

        self._flowdock_api_token = None
        self._flowdock_tags = None
        self._external_username = None
        self.discriminator = None

        if flowdock_api_token is not None:
            self.flowdock_api_token = flowdock_api_token
        if flowdock_tags is not None:
            self.flowdock_tags = flowdock_tags
        if external_username is not None:
            self.external_username = external_username

    @property
    def flowdock_api_token(self):
        """Gets the flowdock_api_token of this FlowdockCallback.  # noqa: E501


        :return: The flowdock_api_token of this FlowdockCallback.  # noqa: E501
        :rtype: str
        """
        return self._flowdock_api_token

    @flowdock_api_token.setter
    def flowdock_api_token(self, flowdock_api_token):
        """Sets the flowdock_api_token of this FlowdockCallback.


        :param flowdock_api_token: The flowdock_api_token of this FlowdockCallback.  # noqa: E501
        :type: str
        """

        self._flowdock_api_token = flowdock_api_token

    @property
    def flowdock_tags(self):
        """Gets the flowdock_tags of this FlowdockCallback.  # noqa: E501


        :return: The flowdock_tags of this FlowdockCallback.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._flowdock_tags

    @flowdock_tags.setter
    def flowdock_tags(self, flowdock_tags):
        """Sets the flowdock_tags of this FlowdockCallback.


        :param flowdock_tags: The flowdock_tags of this FlowdockCallback.  # noqa: E501
        :type: dict(str, str)
        """

        self._flowdock_tags = flowdock_tags

    @property
    def external_username(self):
        """Gets the external_username of this FlowdockCallback.  # noqa: E501


        :return: The external_username of this FlowdockCallback.  # noqa: E501
        :rtype: str
        """
        return self._external_username

    @external_username.setter
    def external_username(self, external_username):
        """Sets the external_username of this FlowdockCallback.


        :param external_username: The external_username of this FlowdockCallback.  # noqa: E501
        :type: str
        """

        self._external_username = external_username

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
        if not isinstance(other, FlowdockCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
