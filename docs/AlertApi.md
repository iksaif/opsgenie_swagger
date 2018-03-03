# opsgenie_swagger.AlertApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_alert**](AlertApi.md#acknowledge_alert) | **POST** /v2/alerts/{identifier}/acknowledge | Acknowledge Alert
[**add_attachment**](AlertApi.md#add_attachment) | **POST** /v2/alerts/{identifier}/attachments | Add Alert Attachment
[**add_details**](AlertApi.md#add_details) | **POST** /v2/alerts/{identifier}/details | Add Details
[**add_note**](AlertApi.md#add_note) | **POST** /v2/alerts/{identifier}/notes | Add Note
[**add_responder**](AlertApi.md#add_responder) | **POST** /v2/alerts/{identifier}/responders | Add Responder
[**add_tags**](AlertApi.md#add_tags) | **POST** /v2/alerts/{identifier}/tags | Add Tags
[**add_team**](AlertApi.md#add_team) | **POST** /v2/alerts/{identifier}/teams | Add Team
[**assign_alert**](AlertApi.md#assign_alert) | **POST** /v2/alerts/{identifier}/assign | Assign Alert
[**close_alert**](AlertApi.md#close_alert) | **POST** /v2/alerts/{identifier}/close | Close Alert
[**create_alert**](AlertApi.md#create_alert) | **POST** /v2/alerts | Create Alert
[**create_saved_searches**](AlertApi.md#create_saved_searches) | **POST** /v2/alerts/saved-searches | Create Saved Search
[**delete_alert**](AlertApi.md#delete_alert) | **DELETE** /v2/alerts/{identifier} | Delete Alert
[**delete_saved_search**](AlertApi.md#delete_saved_search) | **DELETE** /v2/alerts/saved-searches/{identifier} | Delete Saved Search
[**escalate_alert**](AlertApi.md#escalate_alert) | **POST** /v2/alerts/{identifier}/escalate | Escalate Alert
[**execute_custom_alert_action**](AlertApi.md#execute_custom_alert_action) | **POST** /v2/alerts/{identifier}/actions/{actionName} | Custom Alert Action
[**get_alert**](AlertApi.md#get_alert) | **GET** /v2/alerts/{identifier} | Get Alert
[**get_attachment**](AlertApi.md#get_attachment) | **GET** /v2/alerts/{identifier}/attachments/{attachmentId} | Get Alert Attachment
[**get_request_status**](AlertApi.md#get_request_status) | **GET** /v2/alerts/requests/{requestId} | Get Request Status of Alert
[**get_saved_search**](AlertApi.md#get_saved_search) | **GET** /v2/alerts/saved-searches/{identifier} | Get Saved Search
[**list_alerts**](AlertApi.md#list_alerts) | **GET** /v2/alerts | List Alerts
[**list_attachments**](AlertApi.md#list_attachments) | **GET** /v2/alerts/{identifier}/attachments | List Alert Attachments
[**list_logs**](AlertApi.md#list_logs) | **GET** /v2/alerts/{identifier}/logs | List Alert Logs
[**list_notes**](AlertApi.md#list_notes) | **GET** /v2/alerts/{identifier}/notes | List Alert Notes
[**list_recipients**](AlertApi.md#list_recipients) | **GET** /v2/alerts/{identifier}/recipients | List Alert Recipients
[**list_saved_searches**](AlertApi.md#list_saved_searches) | **GET** /v2/alerts/saved-searches | Lists Saved Searches
[**remove_attachment**](AlertApi.md#remove_attachment) | **DELETE** /v2/alerts/{identifier}/attachments/{attachmentId} | Remove Alert Attachment
[**remove_details**](AlertApi.md#remove_details) | **DELETE** /v2/alerts/{identifier}/details | Remove Details
[**remove_tags**](AlertApi.md#remove_tags) | **DELETE** /v2/alerts/{identifier}/tags | Remove Tags
[**snooze_alert**](AlertApi.md#snooze_alert) | **POST** /v2/alerts/{identifier}/snooze | Snooze Alert
[**un_acknowledge_alert**](AlertApi.md#un_acknowledge_alert) | **POST** /v2/alerts/{identifier}/unacknowledge | UnAcknowledge Alert


# **acknowledge_alert**
> SuccessResponse acknowledge_alert(identifier, identifier_type=identifier_type, body=body)

Acknowledge Alert

Acknowledges alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
body = opsgenie_swagger.AcknowledgeAlertPayload() # AcknowledgeAlertPayload | Request payload of acknowledging alert action (optional)

try:
    # Acknowledge Alert
    api_response = api_instance.acknowledge_alert(identifier, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->acknowledge_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **body** | [**AcknowledgeAlertPayload**](AcknowledgeAlertPayload.md)| Request payload of acknowledging alert action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_attachment**
> SuccessResponse add_attachment(identifier, file, alert_identifier_type=alert_identifier_type, user=user, index_file=index_file)

Add Alert Attachment

Add Alert Attachment to related alert

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
file = '/path/to/file.txt' # file | Attachment file to be uploaded
alert_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
user = 'user_example' # str | Display name of the request owner (optional)
index_file = 'index_file_example' # str | Name of html file which will be shown when attachment clicked on UI (optional)

try:
    # Add Alert Attachment
    api_response = api_instance.add_attachment(identifier, file, alert_identifier_type=alert_identifier_type, user=user, index_file=index_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **file** | **file**| Attachment file to be uploaded | 
 **alert_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **user** | **str**| Display name of the request owner | [optional] 
 **index_file** | **str**| Name of html file which will be shown when attachment clicked on UI | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_details**
> SuccessResponse add_details(identifier, body, identifier_type=identifier_type)

Add Details

Add details to the alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.AddDetailsToAlertPayload() # AddDetailsToAlertPayload | Request payload of adding alert details action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Add Details
    api_response = api_instance.add_details(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**AddDetailsToAlertPayload**](AddDetailsToAlertPayload.md)| Request payload of adding alert details action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_note**
> SuccessResponse add_note(identifier, body, identifier_type=identifier_type)

Add Note

Adds note to alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.AddNoteToAlertPayload() # AddNoteToAlertPayload | Request payload of adding note to alert action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Add Note
    api_response = api_instance.add_note(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**AddNoteToAlertPayload**](AddNoteToAlertPayload.md)| Request payload of adding note to alert action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_responder**
> SuccessResponse add_responder(identifier, body, identifier_type=identifier_type)

Add Responder

Add responder to alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.AddResponderToAlertPayload() # AddResponderToAlertPayload | Request payload of adding responder to alert action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Add Responder
    api_response = api_instance.add_responder(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**AddResponderToAlertPayload**](AddResponderToAlertPayload.md)| Request payload of adding responder to alert action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tags**
> SuccessResponse add_tags(identifier, body, identifier_type=identifier_type)

Add Tags

Add tags to the alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.AddTagsToAlertPayload() # AddTagsToAlertPayload | Request payload of creating alert tags action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Add Tags
    api_response = api_instance.add_tags(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**AddTagsToAlertPayload**](AddTagsToAlertPayload.md)| Request payload of creating alert tags action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_team**
> SuccessResponse add_team(identifier, body, identifier_type=identifier_type)

Add Team

Add team to alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.AddTeamToAlertPayload() # AddTeamToAlertPayload | Request payload of adding team to alert action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Add Team
    api_response = api_instance.add_team(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**AddTeamToAlertPayload**](AddTeamToAlertPayload.md)| Request payload of adding team to alert action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_alert**
> SuccessResponse assign_alert(identifier, body, identifier_type=identifier_type)

Assign Alert

Assign alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.AssignAlertPayload() # AssignAlertPayload | Request payload of assigning alert action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Assign Alert
    api_response = api_instance.assign_alert(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->assign_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**AssignAlertPayload**](AssignAlertPayload.md)| Request payload of assigning alert action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_alert**
> SuccessResponse close_alert(identifier, identifier_type=identifier_type, body=body)

Close Alert

Closes alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
body = opsgenie_swagger.CloseAlertPayload() # CloseAlertPayload | Request payload of closing alert action (optional)

try:
    # Close Alert
    api_response = api_instance.close_alert(identifier, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->close_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **body** | [**CloseAlertPayload**](CloseAlertPayload.md)| Request payload of closing alert action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert**
> SuccessResponse create_alert(body)

Create Alert

Creates a new alert

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateAlertPayload() # CreateAlertPayload | Request payload of created alert

try:
    # Create Alert
    api_response = api_instance.create_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->create_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlertPayload**](CreateAlertPayload.md)| Request payload of created alert | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_saved_searches**
> CreateSavedSearchResponse create_saved_searches(body)

Create Saved Search

Create saved search with given fields

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateSavedSearchPayload() # CreateSavedSearchPayload | Request payload of creating saved search

try:
    # Create Saved Search
    api_response = api_instance.create_saved_searches(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->create_saved_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSavedSearchPayload**](CreateSavedSearchPayload.md)| Request payload of creating saved search | 

### Return type

[**CreateSavedSearchResponse**](CreateSavedSearchResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> SuccessResponse delete_alert(identifier, identifier_type=identifier_type, user=user, source=source)

Delete Alert

Deletes an alert using alert id, tiny id or alias

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
user = 'user_example' # str | Display name of the request owner (optional)
source = 'source_example' # str | Display name of the request source (optional)

try:
    # Delete Alert
    api_response = api_instance.delete_alert(identifier, identifier_type=identifier_type, user=user, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **user** | **str**| Display name of the request owner | [optional] 
 **source** | **str**| Display name of the request source | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_search**
> SuccessResponse delete_saved_search(identifier, identifier_type=identifier_type)

Delete Saved Search

Deletes saved search using given search identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the saved search which could be 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', or 'name' (optional) (default to id)

try:
    # Delete Saved Search
    api_response = api_instance.delete_saved_search(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->delete_saved_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the saved search which could be &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **escalate_alert**
> SuccessResponse escalate_alert(identifier, body, identifier_type=identifier_type)

Escalate Alert

Escalate alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.EscalateAlertToNextPayload() # EscalateAlertToNextPayload | Request payload of escalating alert action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Escalate Alert
    api_response = api_instance.escalate_alert(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->escalate_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**EscalateAlertToNextPayload**](EscalateAlertToNextPayload.md)| Request payload of escalating alert action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_custom_alert_action**
> SuccessResponse execute_custom_alert_action(identifier, action_name, identifier_type=identifier_type, body=body)

Custom Alert Action

Custom actions for the alert

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
action_name = 'action_name_example' # str | Name of the action to execute
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
body = opsgenie_swagger.ExecuteCustomAlertActionPayload() # ExecuteCustomAlertActionPayload | Request payload of executing custom alert action (optional)

try:
    # Custom Alert Action
    api_response = api_instance.execute_custom_alert_action(identifier, action_name, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->execute_custom_alert_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **action_name** | **str**| Name of the action to execute | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **body** | [**ExecuteCustomAlertActionPayload**](ExecuteCustomAlertActionPayload.md)| Request payload of executing custom alert action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> GetAlertResponse get_alert(identifier, identifier_type=identifier_type)

Get Alert

Returns alert with given id, tiny id or alias

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Get Alert
    api_response = api_instance.get_alert(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**GetAlertResponse**](GetAlertResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> GetAlertAttachmentResponse get_attachment(identifier, attachment_id, alert_identifier_type=alert_identifier_type)

Get Alert Attachment

Get alert attachment name and url for the given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
attachment_id = 789 # int | Identifier of alert attachment
alert_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Get Alert Attachment
    api_response = api_instance.get_attachment(identifier, attachment_id, alert_identifier_type=alert_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **attachment_id** | **int**| Identifier of alert attachment | 
 **alert_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**GetAlertAttachmentResponse**](GetAlertAttachmentResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_status**
> GetRequestStatusResponse get_request_status(request_id)

Get Request Status of Alert

Used to track the status and alert details (if any) of the request whose identifier is given

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
request_id = 'request_id_example' # str | Universally unique identifier of the questioned request

try:
    # Get Request Status of Alert
    api_response = api_instance.get_request_status(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_request_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Universally unique identifier of the questioned request | 

### Return type

[**GetRequestStatusResponse**](GetRequestStatusResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_search**
> GetSavedSearchResponse get_saved_search(identifier, identifier_type=identifier_type)

Get Saved Search

Get saved search for the given search identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the saved search which could be 'id' or 'name'
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', or 'name' (optional) (default to id)

try:
    # Get Saved Search
    api_response = api_instance.get_saved_search(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_saved_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the saved search which could be &#39;id&#39; or &#39;name&#39; | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, or &#39;name&#39; | [optional] [default to id]

### Return type

[**GetSavedSearchResponse**](GetSavedSearchResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alerts**
> ListAlertsResponse list_alerts(query=query, search_identifier=search_identifier, search_identifier_type=search_identifier_type, offset=offset, limit=limit, sort=sort, order=order)

List Alerts

Returns list of alerts

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
query = 'query_example' # str | Search query to apply while filtering the alerts (optional)
search_identifier = 'search_identifier_example' # str | Identifier of the saved search query to apply while filtering the alerts (optional)
search_identifier_type = 'id' # str | Identifier type of the saved search query. Possible values are 'id', or 'name' (optional) (default to id)
offset = 56 # int | Start index of the result set (to apply pagination). Minimum value (and also default value) is 0 (optional)
limit = 56 # int | Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 (optional)
sort = 'createdAt' # str | Name of the field that result set will be sorted by (optional) (default to createdAt)
order = 'desc' # str | Sorting order of the result set (optional) (default to desc)

try:
    # List Alerts
    api_response = api_instance.list_alerts(query=query, search_identifier=search_identifier, search_identifier_type=search_identifier_type, offset=offset, limit=limit, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->list_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query to apply while filtering the alerts | [optional] 
 **search_identifier** | **str**| Identifier of the saved search query to apply while filtering the alerts | [optional] 
 **search_identifier_type** | **str**| Identifier type of the saved search query. Possible values are &#39;id&#39;, or &#39;name&#39; | [optional] [default to id]
 **offset** | **int**| Start index of the result set (to apply pagination). Minimum value (and also default value) is 0 | [optional] 
 **limit** | **int**| Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 | [optional] 
 **sort** | **str**| Name of the field that result set will be sorted by | [optional] [default to createdAt]
 **order** | **str**| Sorting order of the result set | [optional] [default to desc]

### Return type

[**ListAlertsResponse**](ListAlertsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachments**
> ListAlertAttachmentsResponse list_attachments(identifier, alert_identifier_type=alert_identifier_type)

List Alert Attachments

List alert attachment names and urls for related alert

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
alert_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # List Alert Attachments
    api_response = api_instance.list_attachments(identifier, alert_identifier_type=alert_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->list_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **alert_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**ListAlertAttachmentsResponse**](ListAlertAttachmentsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logs**
> ListAlertLogsResponse list_logs(identifier, identifier_type=identifier_type, offset=offset, direction=direction, limit=limit, order=order)

List Alert Logs

List alert logs for the given alert identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
offset = 'offset_example' # str | Starting value of the offset property (optional)
direction = 'next' # str | Page direction to apply for the given offset with 'next' and 'prev' (optional) (default to next)
limit = 56 # int | Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 (optional)
order = 'desc' # str | Sorting order of the result set (optional) (default to desc)

try:
    # List Alert Logs
    api_response = api_instance.list_logs(identifier, identifier_type=identifier_type, offset=offset, direction=direction, limit=limit, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->list_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **offset** | **str**| Starting value of the offset property | [optional] 
 **direction** | **str**| Page direction to apply for the given offset with &#39;next&#39; and &#39;prev&#39; | [optional] [default to next]
 **limit** | **int**| Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 | [optional] 
 **order** | **str**| Sorting order of the result set | [optional] [default to desc]

### Return type

[**ListAlertLogsResponse**](ListAlertLogsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notes**
> ListAlertNotesResponse list_notes(identifier, identifier_type=identifier_type, offset=offset, direction=direction, limit=limit, order=order)

List Alert Notes

List alert notes for the given alert identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
offset = 'offset_example' # str | Starting value of the offset property (optional)
direction = 'next' # str | Page direction to apply for the given offset with 'next' and 'prev' (optional) (default to next)
limit = 56 # int | Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 (optional)
order = 'desc' # str | Sorting order of the result set (optional) (default to desc)

try:
    # List Alert Notes
    api_response = api_instance.list_notes(identifier, identifier_type=identifier_type, offset=offset, direction=direction, limit=limit, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->list_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **offset** | **str**| Starting value of the offset property | [optional] 
 **direction** | **str**| Page direction to apply for the given offset with &#39;next&#39; and &#39;prev&#39; | [optional] [default to next]
 **limit** | **int**| Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 | [optional] 
 **order** | **str**| Sorting order of the result set | [optional] [default to desc]

### Return type

[**ListAlertNotesResponse**](ListAlertNotesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recipients**
> ListAlertRecipientsResponse list_recipients(identifier, identifier_type=identifier_type)

List Alert Recipients

List alert recipients for the given alert identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # List Alert Recipients
    api_response = api_instance.list_recipients(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->list_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**ListAlertRecipientsResponse**](ListAlertRecipientsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_saved_searches**
> ListSavedSearchesResponse list_saved_searches()

Lists Saved Searches

List all saved searches

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))

try:
    # Lists Saved Searches
    api_response = api_instance.list_saved_searches()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->list_saved_searches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSavedSearchesResponse**](ListSavedSearchesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attachment**
> SuccessResponse remove_attachment(identifier, attachment_id, alert_identifier_type=alert_identifier_type, user=user)

Remove Alert Attachment

Remove alert attachment for the given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
attachment_id = 789 # int | Identifier of alert attachment
alert_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
user = 'user_example' # str | Display name of the request owner (optional)

try:
    # Remove Alert Attachment
    api_response = api_instance.remove_attachment(identifier, attachment_id, alert_identifier_type=alert_identifier_type, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->remove_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **attachment_id** | **int**| Identifier of alert attachment | 
 **alert_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **user** | **str**| Display name of the request owner | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_details**
> SuccessResponse remove_details(identifier, keys, identifier_type=identifier_type, user=user, note=note, source=source)

Remove Details

Remove details of the alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
keys = ['keys_example'] # list[str] | Comma separated list of keys to remove from the custom properties of the alert (e.g. 'key1,key2')
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
user = 'user_example' # str | Display name of the request owner (optional)
note = 'note_example' # str | Additional alert note to add (optional)
source = 'source_example' # str | Display name of the request source (optional)

try:
    # Remove Details
    api_response = api_instance.remove_details(identifier, keys, identifier_type=identifier_type, user=user, note=note, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->remove_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **keys** | [**list[str]**](str.md)| Comma separated list of keys to remove from the custom properties of the alert (e.g. &#39;key1,key2&#39;) | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **user** | **str**| Display name of the request owner | [optional] 
 **note** | **str**| Additional alert note to add | [optional] 
 **source** | **str**| Display name of the request source | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tags**
> SuccessResponse remove_tags(identifier, tags, identifier_type=identifier_type, user=user, note=note, source=source)

Remove Tags

Remove tags of the alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
tags = ['tags_example'] # list[str] | Tags field of the given alert as comma seperated values (e.g. 'tag1, tag2')
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
user = 'user_example' # str | Display name of the request owner (optional)
note = 'note_example' # str | Additional alert note to add (optional)
source = 'source_example' # str | Display name of the request source (optional)

try:
    # Remove Tags
    api_response = api_instance.remove_tags(identifier, tags, identifier_type=identifier_type, user=user, note=note, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->remove_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **tags** | [**list[str]**](str.md)| Tags field of the given alert as comma seperated values (e.g. &#39;tag1, tag2&#39;) | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **user** | **str**| Display name of the request owner | [optional] 
 **note** | **str**| Additional alert note to add | [optional] 
 **source** | **str**| Display name of the request source | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snooze_alert**
> SuccessResponse snooze_alert(identifier, body, identifier_type=identifier_type)

Snooze Alert

Snooze alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
body = opsgenie_swagger.SnoozeAlertPayload() # SnoozeAlertPayload | Request payload of snoozing alert action
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)

try:
    # Snooze Alert
    api_response = api_instance.snooze_alert(identifier, body, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->snooze_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **body** | [**SnoozeAlertPayload**](SnoozeAlertPayload.md)| Request payload of snoozing alert action | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_acknowledge_alert**
> SuccessResponse un_acknowledge_alert(identifier, identifier_type=identifier_type, body=body)

UnAcknowledge Alert

UnAcknowledge alert with given identifier

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
api_instance = opsgenie_swagger.AlertApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of alert which could be alert id, tiny id or alert alias
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny' (optional) (default to id)
body = opsgenie_swagger.UnAcknowledgeAlertPayload() # UnAcknowledgeAlertPayload | Request payload of unacknowledging alert action (optional)

try:
    # UnAcknowledge Alert
    api_response = api_instance.un_acknowledge_alert(identifier, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->un_acknowledge_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of alert which could be alert id, tiny id or alert alias | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39; | [optional] [default to id]
 **body** | [**UnAcknowledgeAlertPayload**](UnAcknowledgeAlertPayload.md)| Request payload of unacknowledging alert action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

