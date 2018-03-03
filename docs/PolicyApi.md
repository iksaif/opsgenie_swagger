# opsgenie_swagger.PolicyApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_policy_order**](PolicyApi.md#change_policy_order) | **POST** /v2/policies/{policyId}/change-order | Change Policy Order
[**create_policy**](PolicyApi.md#create_policy) | **POST** /v2/policies | Create Policy
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /v2/policies/{policyId} | Delete Policy
[**disable_policy**](PolicyApi.md#disable_policy) | **POST** /v2/policies/{policyId}/disable | Disable Policy
[**enable_policy**](PolicyApi.md#enable_policy) | **POST** /v2/policies/{policyId}/enable | Enable Policy
[**get_policy**](PolicyApi.md#get_policy) | **GET** /v2/policies/{policyId} | Get Policy
[**list_alert_policies**](PolicyApi.md#list_alert_policies) | **GET** /v2/policies/alert | List Alert Policies
[**list_notification_policies**](PolicyApi.md#list_notification_policies) | **GET** /v2/policies/notification | List Notification Policies
[**update_policy**](PolicyApi.md#update_policy) | **PUT** /v2/policies/{policyId} | Update Policy


# **change_policy_order**
> SuccessResponse change_policy_order(policy_id, body, team_id=team_id)

Change Policy Order

Change execution order of the policy with given id

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
body = opsgenie_swagger.ChangePolicyOrderPayload() # ChangePolicyOrderPayload | Change order payload
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # Change Policy Order
    api_response = api_instance.change_policy_order(policy_id, body, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->change_policy_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **body** | [**ChangePolicyOrderPayload**](ChangePolicyOrderPayload.md)| Change order payload | 
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> CreatePolicyResponse create_policy(body, team_id=team_id)

Create Policy

Creates a new policy

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.Policy() # Policy | Payload of created policy
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # Create Policy
    api_response = api_instance.create_policy(body, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)| Payload of created policy | 
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**CreatePolicyResponse**](CreatePolicyResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> SuccessResponse delete_policy(policy_id, team_id=team_id)

Delete Policy

Delete policy with given id

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # Delete Policy
    api_response = api_instance.delete_policy(policy_id, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_policy**
> SuccessResponse disable_policy(policy_id, team_id=team_id)

Disable Policy

Disable the policy with given id

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # Disable Policy
    api_response = api_instance.disable_policy(policy_id, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->disable_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_policy**
> SuccessResponse enable_policy(policy_id, team_id=team_id)

Enable Policy

Enable the policy with given id

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # Enable Policy
    api_response = api_instance.enable_policy(policy_id, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->enable_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> GetPolicyResponse get_policy(policy_id, team_id=team_id)

Get Policy

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # Get Policy
    api_response = api_instance.get_policy(policy_id, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**GetPolicyResponse**](GetPolicyResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_policies**
> ListPoliciesResponse list_alert_policies(team_id=team_id)

List Alert Policies

Returns the list of alert policies

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # List Alert Policies
    api_response = api_instance.list_alert_policies(team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->list_alert_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**ListPoliciesResponse**](ListPoliciesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_policies**
> ListPoliciesResponse list_notification_policies(team_id=team_id)

List Notification Policies

Returns the list of notification policies

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # List Notification Policies
    api_response = api_instance.list_notification_policies(team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->list_notification_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**ListPoliciesResponse**](ListPoliciesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> SuccessResponse update_policy(policy_id, body, team_id=team_id)

Update Policy

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
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
body = opsgenie_swagger.Policy() # Policy | Payload of updated policy
team_id = 'team_id_example' # str | TeamId of policy created if it belongs to a team (optional)

try:
    # Update Policy
    api_response = api_instance.update_policy(policy_id, body, team_id=team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **body** | [**Policy**](Policy.md)| Payload of updated policy | 
 **team_id** | **str**| TeamId of policy created if it belongs to a team | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

