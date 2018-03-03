# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from opsgenie_swagger.api_client import ApiClient


class PolicyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_policy_order(self, policy_id, body, **kwargs):  # noqa: E501
        """Change Policy Order  # noqa: E501

        Change execution order of the policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.change_policy_order(policy_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param ChangePolicyOrderPayload body: Change order payload (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.change_policy_order_with_http_info(policy_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.change_policy_order_with_http_info(policy_id, body, **kwargs)  # noqa: E501
            return data

    def change_policy_order_with_http_info(self, policy_id, body, **kwargs):  # noqa: E501
        """Change Policy Order  # noqa: E501

        Change execution order of the policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.change_policy_order_with_http_info(policy_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param ChangePolicyOrderPayload body: Change order payload (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'body', 'team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_policy_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `change_policy_order`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `change_policy_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/{policyId}/change-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_policy(self, body, **kwargs):  # noqa: E501
        """Create Policy  # noqa: E501

        Creates a new policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policy(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Policy body: Payload of created policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: CreatePolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_policy_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_policy_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_policy_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Policy  # noqa: E501

        Creates a new policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policy_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Policy body: Payload of created policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: CreatePolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatePolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_policy(self, policy_id, **kwargs):  # noqa: E501
        """Delete Policy  # noqa: E501

        Delete policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_policy(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def delete_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Delete Policy  # noqa: E501

        Delete policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_policy_with_http_info(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `delete_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/{policyId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def disable_policy(self, policy_id, **kwargs):  # noqa: E501
        """Disable Policy  # noqa: E501

        Disable the policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.disable_policy(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.disable_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.disable_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def disable_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Disable Policy  # noqa: E501

        Disable the policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.disable_policy_with_http_info(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `disable_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/{policyId}/disable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_policy(self, policy_id, **kwargs):  # noqa: E501
        """Enable Policy  # noqa: E501

        Enable the policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable_policy(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.enable_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def enable_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Enable Policy  # noqa: E501

        Enable the policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable_policy_with_http_info(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `enable_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/{policyId}/enable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy(self, policy_id, **kwargs):  # noqa: E501
        """Get Policy  # noqa: E501

        Used to get details of a single policy with id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_policy(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: GetPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def get_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Get Policy  # noqa: E501

        Used to get details of a single policy with id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_policy_with_http_info(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: GetPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `get_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/{policyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_alert_policies(self, **kwargs):  # noqa: E501
        """List Alert Policies  # noqa: E501

        Returns the list of alert policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_alert_policies(async=True)
        >>> result = thread.get()

        :param async bool
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: ListPoliciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_alert_policies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_alert_policies_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_alert_policies_with_http_info(self, **kwargs):  # noqa: E501
        """List Alert Policies  # noqa: E501

        Returns the list of alert policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_alert_policies_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: ListPoliciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_alert_policies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/alert', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListPoliciesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_notification_policies(self, **kwargs):  # noqa: E501
        """List Notification Policies  # noqa: E501

        Returns the list of notification policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_notification_policies(async=True)
        >>> result = thread.get()

        :param async bool
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: ListPoliciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_notification_policies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_notification_policies_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_notification_policies_with_http_info(self, **kwargs):  # noqa: E501
        """List Notification Policies  # noqa: E501

        Returns the list of notification policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_notification_policies_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: ListPoliciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_notification_policies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/notification', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListPoliciesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_policy(self, policy_id, body, **kwargs):  # noqa: E501
        """Update Policy  # noqa: E501

        Update alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_policy(policy_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param Policy body: Payload of updated policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_policy_with_http_info(policy_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_policy_with_http_info(policy_id, body, **kwargs)  # noqa: E501
            return data

    def update_policy_with_http_info(self, policy_id, body, **kwargs):  # noqa: E501
        """Update Policy  # noqa: E501

        Update alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_policy_with_http_info(policy_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str policy_id: Id of the requested policy (required)
        :param Policy body: Payload of updated policy (required)
        :param str team_id: TeamId of policy created if it belongs to a team
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'body', 'team_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `update_policy`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'team_id' in params:
            query_params.append(('teamId', params['team_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/policies/{policyId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
