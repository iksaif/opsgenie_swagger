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


class TeamRoleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_team_role(self, identifier, body, **kwargs):  # noqa: E501
        """Create Team Role  # noqa: E501

        Creates a new team role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_team_role(identifier, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param CreateTeamRolePayload body: Request payload of created team role (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_team_role_with_http_info(identifier, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_team_role_with_http_info(identifier, body, **kwargs)  # noqa: E501
            return data

    def create_team_role_with_http_info(self, identifier, body, **kwargs):  # noqa: E501
        """Create Team Role  # noqa: E501

        Creates a new team role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_team_role_with_http_info(identifier, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param CreateTeamRolePayload body: Request payload of created team role (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'body', 'team_identifier_type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_team_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `create_team_role`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_team_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'team_identifier_type' in params:
            query_params.append(('teamIdentifierType', params['team_identifier_type']))  # noqa: E501

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
            '/v2/teams/{identifier}/roles', 'POST',
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

    def delete_team_role(self, identifier, team_role_identifier, **kwargs):  # noqa: E501
        """Delete Team Role  # noqa: E501

        Deletes a team role using team role 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_team_role(identifier, team_role_identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_role_identifier: Identifier of team role which could be team role 'id' or 'name' (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_team_role_with_http_info(identifier, team_role_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_team_role_with_http_info(identifier, team_role_identifier, **kwargs)  # noqa: E501
            return data

    def delete_team_role_with_http_info(self, identifier, team_role_identifier, **kwargs):  # noqa: E501
        """Delete Team Role  # noqa: E501

        Deletes a team role using team role 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_team_role_with_http_info(identifier, team_role_identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_role_identifier: Identifier of team role which could be team role 'id' or 'name' (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'team_role_identifier', 'team_identifier_type', 'identifier_type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_team_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_team_role`")  # noqa: E501
        # verify the required parameter 'team_role_identifier' is set
        if ('team_role_identifier' not in params or
                params['team_role_identifier'] is None):
            raise ValueError("Missing the required parameter `team_role_identifier` when calling `delete_team_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'team_role_identifier' in params:
            path_params['teamRoleIdentifier'] = params['team_role_identifier']  # noqa: E501

        query_params = []
        if 'team_identifier_type' in params:
            query_params.append(('teamIdentifierType', params['team_identifier_type']))  # noqa: E501
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

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
            '/v2/teams/{identifier}/roles/{teamRoleIdentifier}', 'DELETE',
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

    def get_team_role(self, identifier, team_role_identifier, **kwargs):  # noqa: E501
        """Get Team Role  # noqa: E501

        Returns team role with given 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_team_role(identifier, team_role_identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_role_identifier: Identifier of team role which could be team role 'id' or 'name' (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetTeamRoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_team_role_with_http_info(identifier, team_role_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_role_with_http_info(identifier, team_role_identifier, **kwargs)  # noqa: E501
            return data

    def get_team_role_with_http_info(self, identifier, team_role_identifier, **kwargs):  # noqa: E501
        """Get Team Role  # noqa: E501

        Returns team role with given 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_team_role_with_http_info(identifier, team_role_identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_role_identifier: Identifier of team role which could be team role 'id' or 'name' (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetTeamRoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'team_role_identifier', 'team_identifier_type', 'identifier_type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_team_role`")  # noqa: E501
        # verify the required parameter 'team_role_identifier' is set
        if ('team_role_identifier' not in params or
                params['team_role_identifier'] is None):
            raise ValueError("Missing the required parameter `team_role_identifier` when calling `get_team_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'team_role_identifier' in params:
            path_params['teamRoleIdentifier'] = params['team_role_identifier']  # noqa: E501

        query_params = []
        if 'team_identifier_type' in params:
            query_params.append(('teamIdentifierType', params['team_identifier_type']))  # noqa: E501
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

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
            '/v2/teams/{identifier}/roles/{teamRoleIdentifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTeamRoleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_team_roles(self, identifier, **kwargs):  # noqa: E501
        """List Team Roles  # noqa: E501

        Returns list of team roles  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_team_roles(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :return: ListTeamRoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_team_roles_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.list_team_roles_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def list_team_roles_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """List Team Roles  # noqa: E501

        Returns list of team roles  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_team_roles_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :return: ListTeamRoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'team_identifier_type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_team_roles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `list_team_roles`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'team_identifier_type' in params:
            query_params.append(('teamIdentifierType', params['team_identifier_type']))  # noqa: E501

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
            '/v2/teams/{identifier}/roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListTeamRoleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_team_role(self, identifier, team_role_identifier, **kwargs):  # noqa: E501
        """Update Team Role (Partial)  # noqa: E501

        Updates the team role using team role 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_team_role(identifier, team_role_identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_role_identifier: Identifier of team role which could be team role 'id' or 'name' (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :param UpdateTeamRolePayload body: Request payload of update team role
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_team_role_with_http_info(identifier, team_role_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_team_role_with_http_info(identifier, team_role_identifier, **kwargs)  # noqa: E501
            return data

    def update_team_role_with_http_info(self, identifier, team_role_identifier, **kwargs):  # noqa: E501
        """Update Team Role (Partial)  # noqa: E501

        Updates the team role using team role 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_team_role_with_http_info(identifier, team_role_identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: Identifier of the team (required)
        :param str team_role_identifier: Identifier of team role which could be team role 'id' or 'name' (required)
        :param str team_identifier_type: Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :param UpdateTeamRolePayload body: Request payload of update team role
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'team_role_identifier', 'team_identifier_type', 'identifier_type', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_team_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_team_role`")  # noqa: E501
        # verify the required parameter 'team_role_identifier' is set
        if ('team_role_identifier' not in params or
                params['team_role_identifier'] is None):
            raise ValueError("Missing the required parameter `team_role_identifier` when calling `update_team_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'team_role_identifier' in params:
            path_params['teamRoleIdentifier'] = params['team_role_identifier']  # noqa: E501

        query_params = []
        if 'team_identifier_type' in params:
            query_params.append(('teamIdentifierType', params['team_identifier_type']))  # noqa: E501
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

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
            '/v2/teams/{identifier}/roles/{teamRoleIdentifier}', 'PATCH',
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
