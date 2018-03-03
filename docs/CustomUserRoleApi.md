# opsgenie_swagger.CustomUserRoleApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_user_role**](CustomUserRoleApi.md#create_custom_user_role) | **POST** /v2/roles | Create Custom User Role
[**delete_custom_user_role**](CustomUserRoleApi.md#delete_custom_user_role) | **DELETE** /v2/roles/{identifier} | Delete Custom User Role
[**get_custom_user_role**](CustomUserRoleApi.md#get_custom_user_role) | **GET** /v2/roles/{identifier} | Get Custom User Role
[**list_custom_user_roles**](CustomUserRoleApi.md#list_custom_user_roles) | **GET** /v2/roles | List Custom User Roles
[**update_custom_user_role**](CustomUserRoleApi.md#update_custom_user_role) | **PUT** /v2/roles/{identifier} | Update Custom User Role


# **create_custom_user_role**
> SuccessResponse create_custom_user_role(body)

Create Custom User Role

Creates a new custom user role

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
api_instance = opsgenie_swagger.CustomUserRoleApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateCustomUserRolePayload() # CreateCustomUserRolePayload | Request payload of created custom user role

try:
    # Create Custom User Role
    api_response = api_instance.create_custom_user_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserRoleApi->create_custom_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomUserRolePayload**](CreateCustomUserRolePayload.md)| Request payload of created custom user role | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_user_role**
> SuccessResponse delete_custom_user_role(identifier, identifier_type=identifier_type)

Delete Custom User Role

Deletes a custom user role using role 'id' or 'name'

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
api_instance = opsgenie_swagger.CustomUserRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of custom user role which could be user role 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Delete Custom User Role
    api_response = api_instance.delete_custom_user_role(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserRoleApi->delete_custom_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of custom user role which could be user role &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_user_role**
> GetCustomUserRoleResponse get_custom_user_role(identifier, identifier_type=identifier_type)

Get Custom User Role

Returns custom user role with given 'id' or 'name'

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
api_instance = opsgenie_swagger.CustomUserRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of custom user role which could be user role 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Get Custom User Role
    api_response = api_instance.get_custom_user_role(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserRoleApi->get_custom_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of custom user role which could be user role &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**GetCustomUserRoleResponse**](GetCustomUserRoleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_user_roles**
> ListCustomUserRolesResponse list_custom_user_roles()

List Custom User Roles

Returns list of custom user roles

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
api_instance = opsgenie_swagger.CustomUserRoleApi(opsgenie_swagger.ApiClient(configuration))

try:
    # List Custom User Roles
    api_response = api_instance.list_custom_user_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserRoleApi->list_custom_user_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCustomUserRolesResponse**](ListCustomUserRolesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_user_role**
> SuccessResponse update_custom_user_role(identifier, identifier_type=identifier_type, body=body)

Update Custom User Role

Updates the custom user role using role 'id' or 'name'

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
api_instance = opsgenie_swagger.CustomUserRoleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of custom user role which could be user role 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)
body = opsgenie_swagger.UpdateCustomUserRolePayload() # UpdateCustomUserRolePayload | Request payload of update custom user role (optional)

try:
    # Update Custom User Role
    api_response = api_instance.update_custom_user_role(identifier, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomUserRoleApi->update_custom_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of custom user role which could be user role &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]
 **body** | [**UpdateCustomUserRolePayload**](UpdateCustomUserRolePayload.md)| Request payload of update custom user role | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

