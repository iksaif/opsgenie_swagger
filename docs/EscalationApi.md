# opsgenie_swagger.EscalationApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_escalation**](EscalationApi.md#create_escalation) | **POST** /v2/escalations | Create Escalation
[**delete_escalation**](EscalationApi.md#delete_escalation) | **DELETE** /v2/escalations/{identifier} | Delete Escalation
[**get_escalation**](EscalationApi.md#get_escalation) | **GET** /v2/escalations/{identifier} | Get Escalation
[**list_escalations**](EscalationApi.md#list_escalations) | **GET** /v2/escalations | List Escalations
[**update_escalation**](EscalationApi.md#update_escalation) | **PATCH** /v2/escalations/{identifier} | Update Escalation (Partial)


# **create_escalation**
> SuccessResponse create_escalation(body)

Create Escalation

Creates a new escalation

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
api_instance = opsgenie_swagger.EscalationApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateEscalationPayload() # CreateEscalationPayload | Request payload of created escalation

try:
    # Create Escalation
    api_response = api_instance.create_escalation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EscalationApi->create_escalation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEscalationPayload**](CreateEscalationPayload.md)| Request payload of created escalation | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_escalation**
> SuccessResponse delete_escalation(identifier, identifier_type=identifier_type)

Delete Escalation

Deletes an escalation using escalation 'id' or 'name'

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
api_instance = opsgenie_swagger.EscalationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of escalation which could be escalation 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Delete Escalation
    api_response = api_instance.delete_escalation(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EscalationApi->delete_escalation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of escalation which could be escalation &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_escalation**
> GetEscalationResponse get_escalation(identifier, identifier_type=identifier_type)

Get Escalation

Returns escalation with given 'id' or 'name'

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
api_instance = opsgenie_swagger.EscalationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of escalation which could be escalation 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Get Escalation
    api_response = api_instance.get_escalation(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EscalationApi->get_escalation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of escalation which could be escalation &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**GetEscalationResponse**](GetEscalationResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_escalations**
> ListEscalationsResponse list_escalations()

List Escalations

Returns list of escalations

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
api_instance = opsgenie_swagger.EscalationApi(opsgenie_swagger.ApiClient(configuration))

try:
    # List Escalations
    api_response = api_instance.list_escalations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EscalationApi->list_escalations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListEscalationsResponse**](ListEscalationsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_escalation**
> SuccessResponse update_escalation(identifier, identifier_type=identifier_type, body=body)

Update Escalation (Partial)

Updates the escalation using escalation 'id' or 'name'

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
api_instance = opsgenie_swagger.EscalationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of escalation which could be escalation 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)
body = opsgenie_swagger.UpdateEscalationPayload() # UpdateEscalationPayload | Request payload of update escalation (optional)

try:
    # Update Escalation (Partial)
    api_response = api_instance.update_escalation(identifier, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EscalationApi->update_escalation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of escalation which could be escalation &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]
 **body** | [**UpdateEscalationPayload**](UpdateEscalationPayload.md)| Request payload of update escalation | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

