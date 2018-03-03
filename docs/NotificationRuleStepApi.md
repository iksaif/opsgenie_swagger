# opsgenie_swagger.NotificationRuleStepApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_rule_step**](NotificationRuleStepApi.md#create_notification_rule_step) | **POST** /v2/users/{identifier}/notification-rules/{ruleId}/steps | Create Notification Rule Step
[**delete_notification_rule_step**](NotificationRuleStepApi.md#delete_notification_rule_step) | **DELETE** /v2/users/{identifier}/notification-rules/{ruleId}/steps/{id} | Delete Notification Rule Step
[**disable_notification_rule_step**](NotificationRuleStepApi.md#disable_notification_rule_step) | **POST** /v2/users/{identifier}/notification-rules/{ruleId}/steps/{id}/disable | Disable Notification Rule Step
[**enable_notification_rule_step**](NotificationRuleStepApi.md#enable_notification_rule_step) | **POST** /v2/users/{identifier}/notification-rules/{ruleId}/steps/{id}/enable | Enable Notification Rule Step
[**get_notification_rule_step**](NotificationRuleStepApi.md#get_notification_rule_step) | **GET** /v2/users/{identifier}/notification-rules/{ruleId}/steps/{id} | Get Notification Rule Step
[**list_notification_rule_steps**](NotificationRuleStepApi.md#list_notification_rule_steps) | **GET** /v2/users/{identifier}/notification-rules/{ruleId}/steps | List Notification Rule Steps
[**update_notification_rule_step**](NotificationRuleStepApi.md#update_notification_rule_step) | **PATCH** /v2/users/{identifier}/notification-rules/{ruleId}/steps/{id} | Update Notification Rule Step (Partial)


# **create_notification_rule_step**
> SuccessResponse create_notification_rule_step(identifier, rule_id, body)

Create Notification Rule Step

Creates a new notification rule step

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
api_instance = opsgenie_swagger.NotificationRuleStepApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
body = opsgenie_swagger.CreateNotificationRuleStepPayload() # CreateNotificationRuleStepPayload | Request payload to create notification rule step

try:
    # Create Notification Rule Step
    api_response = api_instance.create_notification_rule_step(identifier, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleStepApi->create_notification_rule_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **body** | [**CreateNotificationRuleStepPayload**](CreateNotificationRuleStepPayload.md)| Request payload to create notification rule step | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_rule_step**
> SuccessResponse delete_notification_rule_step(identifier, rule_id, id)

Delete Notification Rule Step

Deletes a notification rule step using user identifier, rule id, notification rule step id

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
api_instance = opsgenie_swagger.NotificationRuleStepApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
id = 'id_example' # str | Id of the rule step will be changed.

try:
    # Delete Notification Rule Step
    api_response = api_instance.delete_notification_rule_step(identifier, rule_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleStepApi->delete_notification_rule_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **id** | **str**| Id of the rule step will be changed. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_notification_rule_step**
> SuccessResponse disable_notification_rule_step(identifier, rule_id, id)

Disable Notification Rule Step

Disables a new notification rule step

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
api_instance = opsgenie_swagger.NotificationRuleStepApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
id = 'id_example' # str | Id of the rule step will be changed.

try:
    # Disable Notification Rule Step
    api_response = api_instance.disable_notification_rule_step(identifier, rule_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleStepApi->disable_notification_rule_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **id** | **str**| Id of the rule step will be changed. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_notification_rule_step**
> SuccessResponse enable_notification_rule_step(identifier, rule_id, id)

Enable Notification Rule Step

Enables a new notification rule step

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
api_instance = opsgenie_swagger.NotificationRuleStepApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
id = 'id_example' # str | Id of the rule step will be changed.

try:
    # Enable Notification Rule Step
    api_response = api_instance.enable_notification_rule_step(identifier, rule_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleStepApi->enable_notification_rule_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **id** | **str**| Id of the rule step will be changed. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_rule_step**
> GetNotificationRuleStepResponse get_notification_rule_step(identifier, rule_id, id)

Get Notification Rule Step

Returns notification rule step with given user identifier and rule id

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
api_instance = opsgenie_swagger.NotificationRuleStepApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
id = 'id_example' # str | Id of the rule step will be changed.

try:
    # Get Notification Rule Step
    api_response = api_instance.get_notification_rule_step(identifier, rule_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleStepApi->get_notification_rule_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **id** | **str**| Id of the rule step will be changed. | 

### Return type

[**GetNotificationRuleStepResponse**](GetNotificationRuleStepResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_rule_steps**
> ListNotificationRuleStepsResponse list_notification_rule_steps(identifier, rule_id)

List Notification Rule Steps

Returns list of notification rule steps

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
api_instance = opsgenie_swagger.NotificationRuleStepApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.

try:
    # List Notification Rule Steps
    api_response = api_instance.list_notification_rule_steps(identifier, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleStepApi->list_notification_rule_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 

### Return type

[**ListNotificationRuleStepsResponse**](ListNotificationRuleStepsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_rule_step**
> SuccessResponse update_notification_rule_step(identifier, rule_id, id, body=body)

Update Notification Rule Step (Partial)

Update a notification rule step with given user identifier, rule id, and notification rule step id

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
api_instance = opsgenie_swagger.NotificationRuleStepApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
id = 'id_example' # str | Id of the rule step will be changed.
body = opsgenie_swagger.UpdateNotificationRuleStepPayload() # UpdateNotificationRuleStepPayload | Request payload of update schedule action (optional)

try:
    # Update Notification Rule Step (Partial)
    api_response = api_instance.update_notification_rule_step(identifier, rule_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleStepApi->update_notification_rule_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **id** | **str**| Id of the rule step will be changed. | 
 **body** | [**UpdateNotificationRuleStepPayload**](UpdateNotificationRuleStepPayload.md)| Request payload of update schedule action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

