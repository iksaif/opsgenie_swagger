# opsgenie_swagger.ScheduleApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](ScheduleApi.md#create_schedule) | **POST** /v2/schedules | Create Schedule
[**delete_schedule**](ScheduleApi.md#delete_schedule) | **DELETE** /v2/schedules/{identifier} | Delete Schedule
[**export_schedule**](ScheduleApi.md#export_schedule) | **GET** /v2/schedules/{identifier}.ics | Export Schedule
[**get_schedule**](ScheduleApi.md#get_schedule) | **GET** /v2/schedules/{identifier} | Get Schedule
[**get_schedule_timeline**](ScheduleApi.md#get_schedule_timeline) | **GET** /v2/schedules/{identifier}/timeline | Get Schedule Timeline
[**list_schedules**](ScheduleApi.md#list_schedules) | **GET** /v2/schedules | List Schedules
[**update_schedule**](ScheduleApi.md#update_schedule) | **PATCH** /v2/schedules/{identifier} | Update Schedule (Partial)


# **create_schedule**
> CreateScheduleResponse create_schedule(body)

Create Schedule

Creates a new schedule

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
api_instance = opsgenie_swagger.ScheduleApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateSchedulePayload() # CreateSchedulePayload | Request payload of created schedule

try:
    # Create Schedule
    api_response = api_instance.create_schedule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->create_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSchedulePayload**](CreateSchedulePayload.md)| Request payload of created schedule | 

### Return type

[**CreateScheduleResponse**](CreateScheduleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule**
> SuccessResponse delete_schedule(identifier, identifier_type=identifier_type)

Delete Schedule

Delete schedule with given identifier

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
api_instance = opsgenie_swagger.ScheduleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Delete Schedule
    api_response = api_instance.delete_schedule(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->delete_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_schedule**
> str export_schedule(identifier, identifier_type=identifier_type)

Export Schedule

Returns an .ics file as byte array

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
api_instance = opsgenie_swagger.ScheduleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Export Schedule
    api_response = api_instance.export_schedule(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->export_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

**str**

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/calendar

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule**
> GetScheduleResponse get_schedule(identifier, identifier_type=identifier_type)

Get Schedule

Returns schedule with given id or name

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
api_instance = opsgenie_swagger.ScheduleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Get Schedule
    api_response = api_instance.get_schedule(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->get_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**GetScheduleResponse**](GetScheduleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_timeline**
> GetScheduleTimelineResponse get_schedule_timeline(identifier, identifier_type=identifier_type, expand=expand, interval=interval, interval_unit=interval_unit, date=date)

Get Schedule Timeline

Returns schedule timeline with given id or name

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
api_instance = opsgenie_swagger.ScheduleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)
expand = ['expand_example'] # list[str] | Returns more detailed response with expanding it. Possible values are 'base', 'forwarding', and 'override' which is also returned with expandable field of response (optional)
interval = 1 # int | Length of time as integer in intervalUnits to retrieve the timeline. Default value is 1 (optional) (default to 1)
interval_unit = 'interval_unit_example' # str | Unit of the time to retrieve the timeline. Available values are 'days', 'weeks' and 'months'. Default value is 'weeks' (optional)
date = '2013-10-20T19:20:30+01:00' # datetime | Time to return future date on-call participants. Default date is the moment of the time that request is received (optional)

try:
    # Get Schedule Timeline
    api_response = api_instance.get_schedule_timeline(identifier, identifier_type=identifier_type, expand=expand, interval=interval, interval_unit=interval_unit, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->get_schedule_timeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]
 **expand** | [**list[str]**](str.md)| Returns more detailed response with expanding it. Possible values are &#39;base&#39;, &#39;forwarding&#39;, and &#39;override&#39; which is also returned with expandable field of response | [optional] 
 **interval** | **int**| Length of time as integer in intervalUnits to retrieve the timeline. Default value is 1 | [optional] [default to 1]
 **interval_unit** | **str**| Unit of the time to retrieve the timeline. Available values are &#39;days&#39;, &#39;weeks&#39; and &#39;months&#39;. Default value is &#39;weeks&#39; | [optional] 
 **date** | **datetime**| Time to return future date on-call participants. Default date is the moment of the time that request is received | [optional] 

### Return type

[**GetScheduleTimelineResponse**](GetScheduleTimelineResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedules**
> ListSchedulesResponse list_schedules(expand=expand)

List Schedules

Returns list of schedule

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
api_instance = opsgenie_swagger.ScheduleApi(opsgenie_swagger.ApiClient(configuration))
expand = ['expand_example'] # list[str] | Returns more detailed response with expanding it. Possible value is 'rotation' which is also returned with expandable field of response (optional)

try:
    # List Schedules
    api_response = api_instance.list_schedules(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->list_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | [**list[str]**](str.md)| Returns more detailed response with expanding it. Possible value is &#39;rotation&#39; which is also returned with expandable field of response | [optional] 

### Return type

[**ListSchedulesResponse**](ListSchedulesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule**
> UpdateScheduleResponse update_schedule(identifier, identifier_type=identifier_type, body=body)

Update Schedule (Partial)

Update schedule with given id or name

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
api_instance = opsgenie_swagger.ScheduleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)
body = opsgenie_swagger.UpdateSchedulePayload() # UpdateSchedulePayload | Request payload of update schedule action (optional)

try:
    # Update Schedule (Partial)
    api_response = api_instance.update_schedule(identifier, identifier_type=identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->update_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]
 **body** | [**UpdateSchedulePayload**](UpdateSchedulePayload.md)| Request payload of update schedule action | [optional] 

### Return type

[**UpdateScheduleResponse**](UpdateScheduleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

