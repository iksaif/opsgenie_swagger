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


class IntegrationCondition(object):
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
        'field': 'str',
        '_not': 'bool',
        'operation': 'str',
        'expected_value': 'str'
    }

    attribute_map = {
        'field': 'field',
        '_not': 'not',
        'operation': 'operation',
        'expected_value': 'expectedValue'
    }

    def __init__(self, field=None, _not=None, operation=None, expected_value=None):  # noqa: E501
        """IntegrationCondition - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self.__not = None
        self._operation = None
        self._expected_value = None
        self.discriminator = None

        self.field = field
        if _not is not None:
            self._not = _not
        self.operation = operation
        self.expected_value = expected_value

    @property
    def field(self):
        """Gets the field of this IntegrationCondition.  # noqa: E501


        :return: The field of this IntegrationCondition.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this IntegrationCondition.


        :param field: The field of this IntegrationCondition.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def _not(self):
        """Gets the _not of this IntegrationCondition.  # noqa: E501


        :return: The _not of this IntegrationCondition.  # noqa: E501
        :rtype: bool
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this IntegrationCondition.


        :param _not: The _not of this IntegrationCondition.  # noqa: E501
        :type: bool
        """

        self.__not = _not

    @property
    def operation(self):
        """Gets the operation of this IntegrationCondition.  # noqa: E501


        :return: The operation of this IntegrationCondition.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this IntegrationCondition.


        :param operation: The operation of this IntegrationCondition.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["matches", "contains", "starts-with", "ends-with", "equals", "contains-key", "contains-value", "greater-than", "less-than", "is-empty", "equals-ignore-whitespace"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def expected_value(self):
        """Gets the expected_value of this IntegrationCondition.  # noqa: E501


        :return: The expected_value of this IntegrationCondition.  # noqa: E501
        :rtype: str
        """
        return self._expected_value

    @expected_value.setter
    def expected_value(self, expected_value):
        """Sets the expected_value of this IntegrationCondition.


        :param expected_value: The expected_value of this IntegrationCondition.  # noqa: E501
        :type: str
        """
        if expected_value is None:
            raise ValueError("Invalid value for `expected_value`, must not be `None`")  # noqa: E501

        self._expected_value = expected_value

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
        if not isinstance(other, IntegrationCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
