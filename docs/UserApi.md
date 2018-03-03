# opsgenie_swagger.UserApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /v2/users | Create User
[**delete_user**](UserApi.md#delete_user) | **DELETE** /v2/users/{identifier} | Delete User
[**get_user**](UserApi.md#get_user) | **GET** /v2/users/{identifier} | Get User
[**list_user_escalations**](UserApi.md#list_user_escalations) | **GET** /v2/users/{identifier}/escalations | List User Escalations
[**list_user_forwarding_rules**](UserApi.md#list_user_forwarding_rules) | **GET** /v2/users/{identifier}/forwarding-rules | List User Forwarding Rules
[**list_user_schedules**](UserApi.md#list_user_schedules) | **GET** /v2/users/{identifier}/schedules | List User Schedules
[**list_user_teams**](UserApi.md#list_user_teams) | **GET** /v2/users/{identifier}/teams | List User Teams
[**list_users**](UserApi.md#list_users) | **GET** /v2/users | List users
[**update_user**](UserApi.md#update_user) | **PATCH** /v2/users/{identifier} | Update User (Partial)


# **create_user**
> SuccessResponse create_user(body)

Create User

Creates a user with the given payload

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateUserPayload() # CreateUserPayload | Request payload of the user object

try:
    # Create User
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserPayload**](CreateUserPayload.md)| Request payload of the user object | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> SuccessResponse delete_user(identifier)

Delete User

Delete user with the given identifier

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched

try:
    # Delete User
    api_response = api_instance.delete_user(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUserResponse get_user(identifier, expand=expand)

Get User

Get user for the given identifier

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
expand = ['expand_example'] # list[str] | Comma separated list of strings to create a more detailed response. The only expandable field for user api is 'contact' (optional)

try:
    # Get User
    api_response = api_instance.get_user(identifier, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **expand** | [**list[str]**](str.md)| Comma separated list of strings to create a more detailed response. The only expandable field for user api is &#39;contact&#39; | [optional] 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_escalations**
> ListUserEscalationsResponse list_user_escalations(identifier)

List User Escalations

List escalations of the user for the given identifier

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched

try:
    # List User Escalations
    api_response = api_instance.list_user_escalations(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_escalations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 

### Return type

[**ListUserEscalationsResponse**](ListUserEscalationsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_forwarding_rules**
> ListUserForwardingRulesResponse list_user_forwarding_rules(identifier)

List User Forwarding Rules

List user forwarding rules for the given user identifier

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched

try:
    # List User Forwarding Rules
    api_response = api_instance.list_user_forwarding_rules(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_forwarding_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 

### Return type

[**ListUserForwardingRulesResponse**](ListUserForwardingRulesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_schedules**
> ListUserSchedulesResponse list_user_schedules(identifier)

List User Schedules

List schedules of the user for the given identifier

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched

try:
    # List User Schedules
    api_response = api_instance.list_user_schedules(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 

### Return type

[**ListUserSchedulesResponse**](ListUserSchedulesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_teams**
> ListUserTeamsResponse list_user_teams(identifier)

List User Teams

List user teams for the given user identifier

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched

try:
    # List User Teams
    api_response = api_instance.list_user_teams(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 

### Return type

[**ListUserTeamsResponse**](ListUserTeamsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse list_users(limit=limit, offset=offset, sort_field=sort_field, order=order, query=query)

List users

List users with given parameters

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
limit = 100 # int | Number of users to retrieve (optional) (default to 100)
offset = 0 # int | Number of users to skip from start (optional) (default to 0)
sort_field = 'sort_field_example' # str | Field to use in sorting. Should be one of 'username', 'fullName' and 'insertedAt' (optional)
order = 'asc' # str | Direction of sorting. Should be one of 'asc' or 'desc' (optional) (default to asc)
query = 'query_example' # str | Field:value combinations with most of user fields to make more advanced searches. Possible fields are username, fullName, blocked, verified, role, locale, timeZone, userAddress and createdAt (optional)

try:
    # List users
    api_response = api_instance.list_users(limit=limit, offset=offset, sort_field=sort_field, order=order, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of users to retrieve | [optional] [default to 100]
 **offset** | **int**| Number of users to skip from start | [optional] [default to 0]
 **sort_field** | **str**| Field to use in sorting. Should be one of &#39;username&#39;, &#39;fullName&#39; and &#39;insertedAt&#39; | [optional] 
 **order** | **str**| Direction of sorting. Should be one of &#39;asc&#39; or &#39;desc&#39; | [optional] [default to asc]
 **query** | **str**| Field:value combinations with most of user fields to make more advanced searches. Possible fields are username, fullName, blocked, verified, role, locale, timeZone, userAddress and createdAt | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> SuccessResponse update_user(identifier, body=body)

Update User (Partial)

Update user with the given identifier

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
api_instance = opsgenie_swagger.UserApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
body = opsgenie_swagger.UpdateUserPayload() # UpdateUserPayload | Request payload of the user object (optional)

try:
    # Update User (Partial)
    api_response = api_instance.update_user(identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **body** | [**UpdateUserPayload**](UpdateUserPayload.md)| Request payload of the user object | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

