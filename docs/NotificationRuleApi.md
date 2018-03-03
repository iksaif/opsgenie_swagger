# opsgenie_swagger.NotificationRuleApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_notification_rule_order**](NotificationRuleApi.md#change_notification_rule_order) | **POST** /v2/users/{identifier}/notification-rules/{ruleId}/change-order | Change order of Notification Rule
[**create_notification_rule**](NotificationRuleApi.md#create_notification_rule) | **POST** /v2/users/{identifier}/notification-rules | Create Notification Rule
[**delete_notification_rule**](NotificationRuleApi.md#delete_notification_rule) | **DELETE** /v2/users/{identifier}/notification-rules/{ruleId} | Delete Notification Rule
[**disable_notification_rule**](NotificationRuleApi.md#disable_notification_rule) | **POST** /v2/users/{identifier}/notification-rules/{ruleId}/disable | Disable Notification Rule
[**enable_notification_rule**](NotificationRuleApi.md#enable_notification_rule) | **POST** /v2/users/{identifier}/notification-rules/{ruleId}/enable | Enable Notification Rule
[**get_notification_rule**](NotificationRuleApi.md#get_notification_rule) | **GET** /v2/users/{identifier}/notification-rules/{ruleId} | Get Notification Rule
[**list_notification_rules**](NotificationRuleApi.md#list_notification_rules) | **GET** /v2/users/{identifier}/notification-rules | List Notification Rules
[**update_notification_rule**](NotificationRuleApi.md#update_notification_rule) | **PATCH** /v2/users/{identifier}/notification-rules/{ruleId} | Update Notification Rule (Partial)


# **change_notification_rule_order**
> SuccessResponse change_notification_rule_order(identifier, rule_id, body)

Change order of Notification Rule

Changes order of a notification rule with given notification rule id

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
body = opsgenie_swagger.ChangeNotificationRuleOrderPayload() # ChangeNotificationRuleOrderPayload | Request payload of change order of notification rule

try:
    # Change order of Notification Rule
    api_response = api_instance.change_notification_rule_order(identifier, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->change_notification_rule_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **body** | [**ChangeNotificationRuleOrderPayload**](ChangeNotificationRuleOrderPayload.md)| Request payload of change order of notification rule | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_notification_rule**
> CreateNotificationRuleResponse create_notification_rule(identifier, body)

Create Notification Rule

Creates a new notification rule

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
body = opsgenie_swagger.CreateNotificationRulePayload() # CreateNotificationRulePayload | Request payload of create notification rule

try:
    # Create Notification Rule
    api_response = api_instance.create_notification_rule(identifier, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->create_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **body** | [**CreateNotificationRulePayload**](CreateNotificationRulePayload.md)| Request payload of create notification rule | 

### Return type

[**CreateNotificationRuleResponse**](CreateNotificationRuleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_rule**
> SuccessResponse delete_notification_rule(identifier, rule_id)

Delete Notification Rule

Deletes a notification rule with given notification rule id

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.

try:
    # Delete Notification Rule
    api_response = api_instance.delete_notification_rule(identifier, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->delete_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_notification_rule**
> SuccessResponse disable_notification_rule(identifier, rule_id)

Disable Notification Rule

Disables a notification rule with given notification rule id

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.

try:
    # Disable Notification Rule
    api_response = api_instance.disable_notification_rule(identifier, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->disable_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_notification_rule**
> SuccessResponse enable_notification_rule(identifier, rule_id)

Enable Notification Rule

Enables a notification rule with given notification rule id

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.

try:
    # Enable Notification Rule
    api_response = api_instance.enable_notification_rule(identifier, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->enable_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_rule**
> GetNotificationRuleResponse get_notification_rule(identifier, rule_id)

Get Notification Rule

Returns notification rule with given id

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.

try:
    # Get Notification Rule
    api_response = api_instance.get_notification_rule(identifier, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->get_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 

### Return type

[**GetNotificationRuleResponse**](GetNotificationRuleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_rules**
> ListNotificationRulesResponse list_notification_rules(identifier)

List Notification Rules

Returns list of notification rules

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched

try:
    # List Notification Rules
    api_response = api_instance.list_notification_rules(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->list_notification_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 

### Return type

[**ListNotificationRulesResponse**](ListNotificationRulesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_rule**
> UpdateNotificationRuleResponse update_notification_rule(identifier, rule_id, body)

Update Notification Rule (Partial)

Updates the notification rule with given notification rule id

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
api_instance = opsgenie_swagger.NotificationRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
rule_id = 'rule_id_example' # str | Id of the notification rule that step will belong to.
body = opsgenie_swagger.UpdateNotificationRulePayload() # UpdateNotificationRulePayload | Request payload of update notification rule

try:
    # Update Notification Rule (Partial)
    api_response = api_instance.update_notification_rule(identifier, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRuleApi->update_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **rule_id** | **str**| Id of the notification rule that step will belong to. | 
 **body** | [**UpdateNotificationRulePayload**](UpdateNotificationRulePayload.md)| Request payload of update notification rule | 

### Return type

[**UpdateNotificationRuleResponse**](UpdateNotificationRuleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

