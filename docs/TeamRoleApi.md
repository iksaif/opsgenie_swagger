# opsgenie_swagger.TeamRoleApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team_role**](TeamRoleApi.md#create_team_role) | **POST** /v2/teams/{identifier}/roles | Create Team Role
[**delete_team_role**](TeamRoleApi.md#delete_team_role) | **DELETE** /v2/teams/{identifier}/roles/{teamRoleIdentifier} | Delete Team Role
[**get_team_role**](TeamRoleApi.md#get_team_role) | **GET** /v2/teams/{identifier}/roles/{teamRoleIdentifier} | Get Team Role
[**list_team_roles**](TeamRoleApi.md#list_team_roles) | **GET** /v2/teams/{identifier}/roles | List Team Roles
[**update_team_role**](TeamRoleApi.md#update_team_role) | **PATCH** /v2/teams/{identifier}/roles/{teamRoleIdentifier} | Update Team Role (Partial)


# **create_team_role**
> SuccessResponse create_team_role(identifier, body, team_identifier_type=team_identifier_type)

Create Team Role

Creates a new team role

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.TeamRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
body = opsgenie_swagger.CreateTeamRolePayload() # CreateTeamRolePayload | Request payload of created team role
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Create Team Role
    api_response = api_instance.create_team_role(identifier, body, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoleApi->create_team_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **body** | [**CreateTeamRolePayload**](CreateTeamRolePayload.md)| Request payload of created team role | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_role**
> SuccessResponse delete_team_role(identifier, team_role_identifier, team_identifier_type=team_identifier_type, identifier_type=identifier_type)

Delete Team Role

Deletes a team role using team role 'id' or 'name'

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.TeamRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
team_role_identifier = 'team_role_identifier_example' # str | Identifier of team role which could be team role 'id' or 'name'
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Delete Team Role
    api_response = api_instance.delete_team_role(identifier, team_role_identifier, team_identifier_type=team_identifier_type, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoleApi->delete_team_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **team_role_identifier** | **str**| Identifier of team role which could be team role &#39;id&#39; or &#39;name&#39; | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_role**
> GetTeamRoleResponse get_team_role(identifier, team_role_identifier, team_identifier_type=team_identifier_type, identifier_type=identifier_type)

Get Team Role

Returns team role with given 'id' or 'name'

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.TeamRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
team_role_identifier = 'team_role_identifier_example' # str | Identifier of team role which could be team role 'id' or 'name'
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Get Team Role
    api_response = api_instance.get_team_role(identifier, team_role_identifier, team_identifier_type=team_identifier_type, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoleApi->get_team_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **team_role_identifier** | **str**| Identifier of team role which could be team role &#39;id&#39; or &#39;name&#39; | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**GetTeamRoleResponse**](GetTeamRoleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_roles**
> ListTeamRoleResponse list_team_roles(identifier, team_identifier_type=team_identifier_type)

List Team Roles

Returns list of team roles

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.TeamRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # List Team Roles
    api_response = api_instance.list_team_roles(identifier, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoleApi->list_team_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**ListTeamRoleResponse**](ListTeamRoleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_role**
> SuccessResponse update_team_role(identifier, team_role_identifier, team_identifier_type=team_identifier_type, identifier_type=identifier_type, body=body)

Update Team Role (Partial)

Updates the team role using team role 'id' or 'name'

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.TeamRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
team_role_identifier = 'team_role_identifier_example' # str | Identifier of team role which could be team role 'id' or 'name'
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)
body = opsgenie_swagger.UpdateTeamRolePayload() # UpdateTeamRolePayload | Request payload of update team role (optional)

try:
    # Update Team Role (Partial)
    api_response = api_instance.update_team_role(identifier, team_role_identifier, team_identifier_type=team_identifier_type, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoleApi->update_team_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **team_role_identifier** | **str**| Identifier of team role which could be team role &#39;id&#39; or &#39;name&#39; | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]
 **body** | [**UpdateTeamRolePayload**](UpdateTeamRolePayload.md)| Request payload of update team role | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

