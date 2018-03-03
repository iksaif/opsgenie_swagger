# opsgenie_swagger.IntegrationActionApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration_action**](IntegrationActionApi.md#create_integration_action) | **POST** /v2/integrations/{id}/actions | Create Integration Action
[**list_integration_actions**](IntegrationActionApi.md#list_integration_actions) | **GET** /v2/integrations/{id}/actions | List Integration Actions
[**update_integration_actions**](IntegrationActionApi.md#update_integration_actions) | **PUT** /v2/integrations/{id}/actions | Update Integration Actions


# **create_integration_action**
> CreateIntegrationActionsResponse create_integration_action(id, body)

Create Integration Action

Creates integration actions of given integration id

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
api_instance = opsgenie_swagger.IntegrationActionApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id
body = opsgenie_swagger.BaseIntegrationAction() # BaseIntegrationAction | Request payload to create integration action

try:
    # Create Integration Action
    api_response = api_instance.create_integration_action(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationActionApi->create_integration_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 
 **body** | [**BaseIntegrationAction**](BaseIntegrationAction.md)| Request payload to create integration action | 

### Return type

[**CreateIntegrationActionsResponse**](CreateIntegrationActionsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_actions**
> ListIntegrationActionsResponse list_integration_actions(id)

List Integration Actions

List integration actions of given integration id

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
api_instance = opsgenie_swagger.IntegrationActionApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id

try:
    # List Integration Actions
    api_response = api_instance.list_integration_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationActionApi->list_integration_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 

### Return type

[**ListIntegrationActionsResponse**](ListIntegrationActionsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_actions**
> UpdateIntegrationActionsResponse update_integration_actions(id, body)

Update Integration Actions

Updates integration actions of given integration id

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
api_instance = opsgenie_swagger.IntegrationActionApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id
body = opsgenie_swagger.ActionCategorized() # ActionCategorized | Request payload to update integration actions

try:
    # Update Integration Actions
    api_response = api_instance.update_integration_actions(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationActionApi->update_integration_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 
 **body** | [**ActionCategorized**](ActionCategorized.md)| Request payload to update integration actions | 

### Return type

[**UpdateIntegrationActionsResponse**](UpdateIntegrationActionsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

