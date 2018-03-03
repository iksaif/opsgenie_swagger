# opsgenie_swagger.TeamApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](TeamApi.md#create_team) | **POST** /v2/teams | Create Team
[**delete_team**](TeamApi.md#delete_team) | **DELETE** /v2/teams/{identifier} | Delete Team
[**get_team**](TeamApi.md#get_team) | **GET** /v2/teams/{identifier} | Get Team
[**list_team_logs**](TeamApi.md#list_team_logs) | **GET** /v2/teams/{identifier}/logs | List Team Logs
[**list_teams**](TeamApi.md#list_teams) | **GET** /v2/teams | List Teams
[**update_team**](TeamApi.md#update_team) | **PATCH** /v2/teams/{identifier} | Update Team (Partial)


# **create_team**
> SuccessResponse create_team(body)

Create Team

Creates a new team

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
api_instance = opsgenie_swagger.TeamApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateTeamPayload() # CreateTeamPayload | Request payload of created team

try:
    # Create Team
    api_response = api_instance.create_team(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTeamPayload**](CreateTeamPayload.md)| Request payload of created team | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> SuccessResponse delete_team(identifier, identifier_type=identifier_type)

Delete Team

Delete team with given id or name

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
api_instance = opsgenie_swagger.TeamApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Delete Team
    api_response = api_instance.delete_team(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> GetTeamResponse get_team(identifier, identifier_type=identifier_type)

Get Team

Returns team with given 'id' or 'name'

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
api_instance = opsgenie_swagger.TeamApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Get Team
    api_response = api_instance.get_team(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**GetTeamResponse**](GetTeamResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_logs**
> ListTeamLogsResponse list_team_logs(identifier, identifier_type=identifier_type, limit=limit, order=order, offset=offset)

List Team Logs

Return logs of a team given with identifier

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
api_instance = opsgenie_swagger.TeamApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)
limit = 56 # int | Maximum number of items to provide in the result. Must be a positive integer value. (optional)
order = 'desc' # str | Sorting order of the result set (optional) (default to desc)
offset = 'offset_example' # str | Key which will be used in pagination (optional)

try:
    # List Team Logs
    api_response = api_instance.list_team_logs(identifier, identifier_type=identifier_type, limit=limit, order=order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_team_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]
 **limit** | **int**| Maximum number of items to provide in the result. Must be a positive integer value. | [optional] 
 **order** | **str**| Sorting order of the result set | [optional] [default to desc]
 **offset** | **str**| Key which will be used in pagination | [optional] 

### Return type

[**ListTeamLogsResponse**](ListTeamLogsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> ListTeamsResponse list_teams(expand=expand)

List Teams

Return list of teams

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
api_instance = opsgenie_swagger.TeamApi(opsgenie_swagger.ApiClient(configuration))
expand = ['expand_example'] # list[str] | Returns more detailed response with expanding it. Possible value is 'member' which is also returned with expandable field of response (optional)

try:
    # List Teams
    api_response = api_instance.list_teams(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | [**list[str]**](str.md)| Returns more detailed response with expanding it. Possible value is &#39;member&#39; which is also returned with expandable field of response | [optional] 

### Return type

[**ListTeamsResponse**](ListTeamsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> SuccessResponse update_team(identifier, body=body)

Update Team (Partial)

Update team with given id

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
api_instance = opsgenie_swagger.TeamApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
body = opsgenie_swagger.UpdateTeamPayload() # UpdateTeamPayload | Request payload of update team action (optional)

try:
    # Update Team (Partial)
    api_response = api_instance.update_team(identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **body** | [**UpdateTeamPayload**](UpdateTeamPayload.md)| Request payload of update team action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

