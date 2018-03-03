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
from opsgenie_swagger.models.bidirectional_callback import BidirectionalCallback  # noqa: F401,E501


class SolarWindsWebHelpDeskCallback(object):
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
        'solar_winds_web_help_desk_api_key': 'str',
        'solar_winds_web_help_server_url': 'str'
    }

    attribute_map = {
        'solar_winds_web_help_desk_api_key': 'solarWindsWebHelpDeskApiKey',
        'solar_winds_web_help_server_url': 'solarWindsWebHelpServerURL'
    }

    def __init__(self, solar_winds_web_help_desk_api_key=None, solar_winds_web_help_server_url=None):  # noqa: E501
        """SolarWindsWebHelpDeskCallback - a model defined in Swagger"""  # noqa: E501

        self._solar_winds_web_help_desk_api_key = None
        self._solar_winds_web_help_server_url = None
        self.discriminator = None

        if solar_winds_web_help_desk_api_key is not None:
            self.solar_winds_web_help_desk_api_key = solar_winds_web_help_desk_api_key
        if solar_winds_web_help_server_url is not None:
            self.solar_winds_web_help_server_url = solar_winds_web_help_server_url

    @property
    def solar_winds_web_help_desk_api_key(self):
        """Gets the solar_winds_web_help_desk_api_key of this SolarWindsWebHelpDeskCallback.  # noqa: E501


        :return: The solar_winds_web_help_desk_api_key of this SolarWindsWebHelpDeskCallback.  # noqa: E501
        :rtype: str
        """
        return self._solar_winds_web_help_desk_api_key

    @solar_winds_web_help_desk_api_key.setter
    def solar_winds_web_help_desk_api_key(self, solar_winds_web_help_desk_api_key):
        """Sets the solar_winds_web_help_desk_api_key of this SolarWindsWebHelpDeskCallback.


        :param solar_winds_web_help_desk_api_key: The solar_winds_web_help_desk_api_key of this SolarWindsWebHelpDeskCallback.  # noqa: E501
        :type: str
        """

        self._solar_winds_web_help_desk_api_key = solar_winds_web_help_desk_api_key

    @property
    def solar_winds_web_help_server_url(self):
        """Gets the solar_winds_web_help_server_url of this SolarWindsWebHelpDeskCallback.  # noqa: E501


        :return: The solar_winds_web_help_server_url of this SolarWindsWebHelpDeskCallback.  # noqa: E501
        :rtype: str
        """
        return self._solar_winds_web_help_server_url

    @solar_winds_web_help_server_url.setter
    def solar_winds_web_help_server_url(self, solar_winds_web_help_server_url):
        """Sets the solar_winds_web_help_server_url of this SolarWindsWebHelpDeskCallback.


        :param solar_winds_web_help_server_url: The solar_winds_web_help_server_url of this SolarWindsWebHelpDeskCallback.  # noqa: E501
        :type: str
        """

        self._solar_winds_web_help_server_url = solar_winds_web_help_server_url

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
        if not isinstance(other, SolarWindsWebHelpDeskCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
