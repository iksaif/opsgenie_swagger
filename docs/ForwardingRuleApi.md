# opsgenie_swagger.ForwardingRuleApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_forwarding_rule**](ForwardingRuleApi.md#create_forwarding_rule) | **POST** /v2/forwarding-rules | Create Forwarding Rule
[**delete_forwarding_rule**](ForwardingRuleApi.md#delete_forwarding_rule) | **DELETE** /v2/forwarding-rules/{identifier} | Delete Forwarding Rule
[**get_forwarding_rule**](ForwardingRuleApi.md#get_forwarding_rule) | **GET** /v2/forwarding-rules/{identifier} | Get Forwarding Rule
[**list_forwarding_rules**](ForwardingRuleApi.md#list_forwarding_rules) | **GET** /v2/forwarding-rules | List Forwarding Rules
[**update_forwarding_rule**](ForwardingRuleApi.md#update_forwarding_rule) | **PUT** /v2/forwarding-rules/{identifier} | Update Forwarding Rule


# **create_forwarding_rule**
> CreateForwardingRuleResponse create_forwarding_rule(body)

Create Forwarding Rule

Creates a new forwarding rule

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
api_instance = opsgenie_swagger.ForwardingRuleApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateForwardingRulePayload() # CreateForwardingRulePayload | Request payload to created forwarding rule

try:
    # Create Forwarding Rule
    api_response = api_instance.create_forwarding_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForwardingRuleApi->create_forwarding_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateForwardingRulePayload**](CreateForwardingRulePayload.md)| Request payload to created forwarding rule | 

### Return type

[**CreateForwardingRuleResponse**](CreateForwardingRuleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_forwarding_rule**
> SuccessResponse delete_forwarding_rule(identifier, identifier_type=identifier_type)

Delete Forwarding Rule

Deletes forwarding rule with given identifier

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
api_instance = opsgenie_swagger.ForwardingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias' (optional) (default to id)

try:
    # Delete Forwarding Rule
    api_response = api_instance.delete_forwarding_rule(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForwardingRuleApi->delete_forwarding_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the forwarding rule which could be forwarding rule &#39;id&#39; or &#39;alias&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;alias&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forwarding_rule**
> GetForwardingRuleResponse get_forwarding_rule(identifier, identifier_type=identifier_type)

Get Forwarding Rule

Returns forwarding rule with given id or alias

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
api_instance = opsgenie_swagger.ForwardingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias' (optional) (default to id)

try:
    # Get Forwarding Rule
    api_response = api_instance.get_forwarding_rule(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForwardingRuleApi->get_forwarding_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the forwarding rule which could be forwarding rule &#39;id&#39; or &#39;alias&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;alias&#39; | [optional] [default to id]

### Return type

[**GetForwardingRuleResponse**](GetForwardingRuleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forwarding_rules**
> ListForwardingRulesResponse list_forwarding_rules()

List Forwarding Rules

Returns list of forwarding rules

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
api_instance = opsgenie_swagger.ForwardingRuleApi(opsgenie_swagger.ApiClient(configuration))

try:
    # List Forwarding Rules
    api_response = api_instance.list_forwarding_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForwardingRuleApi->list_forwarding_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListForwardingRulesResponse**](ListForwardingRulesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_forwarding_rule**
> SuccessResponse update_forwarding_rule(identifier, body, identifier_type=identifier_type)

Update Forwarding Rule

Update forwarding rule with given rule id or alias

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
api_instance = opsgenie_swagger.ForwardingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias'
body = opsgenie_swagger.UpdateForwardingRulePayload() # UpdateForwardingRulePayload | Request payload of update forwarding rule action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias' (optional) (default to id)

try:
    # Update Forwarding Rule
    api_response = api_instance.update_forwarding_rule(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForwardingRuleApi->update_forwarding_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the forwarding rule which could be forwarding rule &#39;id&#39; or &#39;alias&#39; | 
 **body** | [**UpdateForwardingRulePayload**](UpdateForwardingRulePayload.md)| Request payload of update forwarding rule action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;alias&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

