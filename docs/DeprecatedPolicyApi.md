# opsgenie_swagger.DeprecatedPolicyApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_alert_policy_order**](DeprecatedPolicyApi.md#change_alert_policy_order) | **POST** /v1/policies/{policyId}/change-order | Change Alert Policy Order
[**create_alert_policy**](DeprecatedPolicyApi.md#create_alert_policy) | **POST** /v1/policies | Create Alert Policy
[**delete_alert_policy**](DeprecatedPolicyApi.md#delete_alert_policy) | **DELETE** /v1/policies/{policyId} | Delete Alert Policy
[**disable_alert_policy**](DeprecatedPolicyApi.md#disable_alert_policy) | **POST** /v1/policies/{policyId}/disable | Disable Alert Policy
[**enable_alert_policy**](DeprecatedPolicyApi.md#enable_alert_policy) | **POST** /v1/policies/{policyId}/enable | Enable Alert Policy
[**get_alert_policy**](DeprecatedPolicyApi.md#get_alert_policy) | **GET** /v1/policies/{policyId} | Get Alert Policy
[**list_alert_policies**](DeprecatedPolicyApi.md#list_alert_policies) | **GET** /v1/policies | List Alert Policies
[**update_alert_policy**](DeprecatedPolicyApi.md#update_alert_policy) | **PUT** /v1/policies/{policyId} | Update Alert Policy


# **change_alert_policy_order**
> SuccessResponse change_alert_policy_order(policy_id, body)

Change Alert Policy Order

Change execution order of the alert policy with given id

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
body = opsgenie_swagger.DeprecatedChangeAlertPolicyOrderPayload() # DeprecatedChangeAlertPolicyOrderPayload | Change order payload

try:
    # Change Alert Policy Order
    api_response = api_instance.change_alert_policy_order(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->change_alert_policy_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **body** | [**DeprecatedChangeAlertPolicyOrderPayload**](DeprecatedChangeAlertPolicyOrderPayload.md)| Change order payload | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert_policy**
> DeprecatedCreateAlertPolicyResponse create_alert_policy(body)

Create Alert Policy

Creates a new alert policy

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.DeprecatedAlertPolicy() # DeprecatedAlertPolicy | Payload of created alert policy

try:
    # Create Alert Policy
    api_response = api_instance.create_alert_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->create_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeprecatedAlertPolicy**](DeprecatedAlertPolicy.md)| Payload of created alert policy | 

### Return type

[**DeprecatedCreateAlertPolicyResponse**](DeprecatedCreateAlertPolicyResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_policy**
> SuccessResponse delete_alert_policy(policy_id)

Delete Alert Policy

Delete alert policy with given id

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Delete Alert Policy
    api_response = api_instance.delete_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->delete_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_alert_policy**
> SuccessResponse disable_alert_policy(policy_id)

Disable Alert Policy

Disable the alert policy with given id

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Disable Alert Policy
    api_response = api_instance.disable_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->disable_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_alert_policy**
> SuccessResponse enable_alert_policy(policy_id)

Enable Alert Policy

Enable the alert policy with given id

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Enable Alert Policy
    api_response = api_instance.enable_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->enable_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_policy**
> DeprecatedGetAlertPolicyResponse get_alert_policy(policy_id)

Get Alert Policy

Used to get details of a single policy with id

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Get Alert Policy
    api_response = api_instance.get_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->get_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**DeprecatedGetAlertPolicyResponse**](DeprecatedGetAlertPolicyResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_policies**
> DeprecatedListAlertPoliciesResponse list_alert_policies()

List Alert Policies

Returns list alert policies

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))

try:
    # List Alert Policies
    api_response = api_instance.list_alert_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->list_alert_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeprecatedListAlertPoliciesResponse**](DeprecatedListAlertPoliciesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_policy**
> SuccessResponse update_alert_policy(policy_id, body)

Update Alert Policy

Update alert policy with given id

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
api_instance = opsgenie_swagger.DeprecatedPolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
body = opsgenie_swagger.DeprecatedAlertPolicy() # DeprecatedAlertPolicy | Payload of updated alert policy

try:
    # Update Alert Policy
    api_response = api_instance.update_alert_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedPolicyApi->update_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **body** | [**DeprecatedAlertPolicy**](DeprecatedAlertPolicy.md)| Payload of updated alert policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

