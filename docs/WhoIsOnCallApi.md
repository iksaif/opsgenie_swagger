# opsgenie_swagger.WhoIsOnCallApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_on_call_user**](WhoIsOnCallApi.md#export_on_call_user) | **GET** /v2/schedules/on-calls/{identifier}.ics | Export On-Call User
[**get_next_on_calls**](WhoIsOnCallApi.md#get_next_on_calls) | **GET** /v2/schedules/{identifier}/next-on-calls | Get Next On Calls
[**get_on_calls**](WhoIsOnCallApi.md#get_on_calls) | **GET** /v2/schedules/{identifier}/on-calls | Get On Calls
[**list_on_calls**](WhoIsOnCallApi.md#list_on_calls) | **GET** /v2/schedules/on-calls | List On Calls


# **export_on_call_user**
> str export_on_call_user(identifier)

Export On-Call User

Exports personal on-call timeline of 3 months to a .ics file

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
api_instance = opsgenie_swagger.WhoIsOnCallApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user. Should be either 'id' or 'username' of the user

try:
    # Export On-Call User
    api_response = api_instance.export_on_call_user(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhoIsOnCallApi->export_on_call_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user. Should be either &#39;id&#39; or &#39;username&#39; of the user | 

### Return type

**str**

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/calendar

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_on_calls**
> GetNextOnCallResponse get_next_on_calls(identifier, schedule_identifier_type=schedule_identifier_type, flat=flat, date=date)

Get Next On Calls

Gets next on-call participants of a specific schedule

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
api_instance = opsgenie_swagger.WhoIsOnCallApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)
flat = true # bool | Retrieves user names of all on call participants if enabled (optional)
date = '2013-10-20T19:20:30+01:00' # datetime | Starting date of the timeline (optional)

try:
    # Get Next On Calls
    api_response = api_instance.get_next_on_calls(identifier, schedule_identifier_type=schedule_identifier_type, flat=flat, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhoIsOnCallApi->get_next_on_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]
 **flat** | **bool**| Retrieves user names of all on call participants if enabled | [optional] 
 **date** | **datetime**| Starting date of the timeline | [optional] 

### Return type

[**GetNextOnCallResponse**](GetNextOnCallResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_on_calls**
> GetOnCallResponse get_on_calls(identifier, schedule_identifier_type=schedule_identifier_type, flat=flat, date=date)

Get On Calls

Gets current on-call participants of a specific schedule

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
api_instance = opsgenie_swagger.WhoIsOnCallApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)
flat = true # bool | Retrieves user names of all on call participants if enabled (optional)
date = '2013-10-20T19:20:30+01:00' # datetime | Starting date of the timeline (optional)

try:
    # Get On Calls
    api_response = api_instance.get_on_calls(identifier, schedule_identifier_type=schedule_identifier_type, flat=flat, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhoIsOnCallApi->get_on_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]
 **flat** | **bool**| Retrieves user names of all on call participants if enabled | [optional] 
 **date** | **datetime**| Starting date of the timeline | [optional] 

### Return type

[**GetOnCallResponse**](GetOnCallResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_on_calls**
> ListOnCallsResponse list_on_calls(flat=flat, date=date)

List On Calls

Lists current on-call participants of all schedules

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
api_instance = opsgenie_swagger.WhoIsOnCallApi(opsgenie_swagger.ApiClient(configuration))
flat = true # bool | Retrieves user names of all on call participants if enabled (optional)
date = '2013-10-20T19:20:30+01:00' # datetime | Starting date of the timeline (optional)

try:
    # List On Calls
    api_response = api_instance.list_on_calls(flat=flat, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhoIsOnCallApi->list_on_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flat** | **bool**| Retrieves user names of all on call participants if enabled | [optional] 
 **date** | **datetime**| Starting date of the timeline | [optional] 

### Return type

[**ListOnCallsResponse**](ListOnCallsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

