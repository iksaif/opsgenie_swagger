# opsgenie_swagger.TeamMemberApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_member**](TeamMemberApi.md#add_team_member) | **POST** /v2/teams/{identifier}/members | Add Team Member
[**delete_team_member**](TeamMemberApi.md#delete_team_member) | **DELETE** /v2/teams/{identifier}/members/{memberIdentifier} | Delete Team Member


# **add_team_member**
> SuccessResponse add_team_member(identifier, body, team_identifier_type=team_identifier_type)

Add Team Member

Adds a member to team with given identifier

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
api_instance = opsgenie_swagger.TeamMemberApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
body = opsgenie_swagger.AddTeamMemberPayload() # AddTeamMemberPayload | Request payload of added team member
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Add Team Member
    api_response = api_instance.add_team_member(identifier, body, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->add_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **body** | [**AddTeamMemberPayload**](AddTeamMemberPayload.md)| Request payload of added team member | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_member**
> SuccessResponse delete_team_member(identifier, member_identifier, team_identifier_type=team_identifier_type)

Delete Team Member

Deletes the member of team with given identifier

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
api_instance = opsgenie_swagger.TeamMemberApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
member_identifier = 'member_identifier_example' # str | User id or username of member for removal
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Delete Team Member
    api_response = api_instance.delete_team_member(identifier, member_identifier, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->delete_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **member_identifier** | **str**| User id or username of member for removal | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

