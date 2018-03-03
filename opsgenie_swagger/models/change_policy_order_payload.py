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


class ChangePolicyOrderPayload(object):
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
        'target_index': 'int'
    }

    attribute_map = {
        'target_index': 'targetIndex'
    }

    def __init__(self, target_index=None):  # noqa: E501
        """ChangePolicyOrderPayload - a model defined in Swagger"""  # noqa: E501

        self._target_index = None
        self.discriminator = None

        self.target_index = target_index

    @property
    def target_index(self):
        """Gets the target_index of this ChangePolicyOrderPayload.  # noqa: E501

        Order of the target policy will be changed to this value. Larger values than policy count will put the target policy to last place  # noqa: E501

        :return: The target_index of this ChangePolicyOrderPayload.  # noqa: E501
        :rtype: int
        """
        return self._target_index

    @target_index.setter
    def target_index(self, target_index):
        """Sets the target_index of this ChangePolicyOrderPayload.

        Order of the target policy will be changed to this value. Larger values than policy count will put the target policy to last place  # noqa: E501

        :param target_index: The target_index of this ChangePolicyOrderPayload.  # noqa: E501
        :type: int
        """
        if target_index is None:
            raise ValueError("Invalid value for `target_index`, must not be `None`")  # noqa: E501
        if target_index is not None and target_index < 0:  # noqa: E501
            raise ValueError("Invalid value for `target_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._target_index = target_index

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
        if not isinstance(other, ChangePolicyOrderPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
