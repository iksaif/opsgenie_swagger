# opsgenie_swagger.ScheduleOverrideApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_override**](ScheduleOverrideApi.md#create_schedule_override) | **POST** /v2/schedules/{identifier}/overrides | Create Schedule Override
[**delete_schedule_override**](ScheduleOverrideApi.md#delete_schedule_override) | **DELETE** /v2/schedules/{identifier}/overrides/{alias} | Delete Schedule Override
[**get_schedule_override**](ScheduleOverrideApi.md#get_schedule_override) | **GET** /v2/schedules/{identifier}/overrides/{alias} | Get Schedule Override
[**list_schedule_override**](ScheduleOverrideApi.md#list_schedule_override) | **GET** /v2/schedules/{identifier}/overrides | List Schedule Overrides
[**update_schedule_override**](ScheduleOverrideApi.md#update_schedule_override) | **PUT** /v2/schedules/{identifier}/overrides/{alias} | Update Schedule Override


# **create_schedule_override**
> CreateScheduleOverrideResponse create_schedule_override(identifier, body, schedule_identifier_type=schedule_identifier_type)

Create Schedule Override

Creates a schedule override for the specified user and schedule

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
api_instance = opsgenie_swagger.ScheduleOverrideApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
body = opsgenie_swagger.CreateScheduleOverridePayload() # CreateScheduleOverridePayload | Request payload of created schedule override
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Create Schedule Override
    api_response = api_instance.create_schedule_override(identifier, body, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleOverrideApi->create_schedule_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **body** | [**CreateScheduleOverridePayload**](CreateScheduleOverridePayload.md)| Request payload of created schedule override | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**CreateScheduleOverrideResponse**](CreateScheduleOverrideResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule_override**
> SuccessResponse delete_schedule_override(identifier, alias, schedule_identifier_type=schedule_identifier_type)

Delete Schedule Override

Delete schedule override with given alias

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
api_instance = opsgenie_swagger.ScheduleOverrideApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
alias = 'alias_example' # str | Alias of the schedule override
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Delete Schedule Override
    api_response = api_instance.delete_schedule_override(identifier, alias, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleOverrideApi->delete_schedule_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **alias** | **str**| Alias of the schedule override | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_override**
> GetScheduleOverrideResponse get_schedule_override(identifier, alias, schedule_identifier_type=schedule_identifier_type)

Get Schedule Override

Gets schedule override details with given alias

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
api_instance = opsgenie_swagger.ScheduleOverrideApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
alias = 'alias_example' # str | Alias of the schedule override
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Get Schedule Override
    api_response = api_instance.get_schedule_override(identifier, alias, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleOverrideApi->get_schedule_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **alias** | **str**| Alias of the schedule override | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**GetScheduleOverrideResponse**](GetScheduleOverrideResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedule_override**
> ListScheduleOverrideResponse list_schedule_override(identifier, schedule_identifier_type=schedule_identifier_type)

List Schedule Overrides

Returns list of schedule overrides

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
api_instance = opsgenie_swagger.ScheduleOverrideApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # List Schedule Overrides
    api_response = api_instance.list_schedule_override(identifier, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleOverrideApi->list_schedule_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**ListScheduleOverrideResponse**](ListScheduleOverrideResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule_override**
> UpdateScheduleOverrideResponse update_schedule_override(identifier, alias, body, schedule_identifier_type=schedule_identifier_type)

Update Schedule Override

Update schedule override with given alias

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
api_instance = opsgenie_swagger.ScheduleOverrideApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
alias = 'alias_example' # str | Alias of the schedule override
body = opsgenie_swagger.UpdateScheduleOverridePayload() # UpdateScheduleOverridePayload | Request payload of update schedule override
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Update Schedule Override
    api_response = api_instance.update_schedule_override(identifier, alias, body, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleOverrideApi->update_schedule_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **alias** | **str**| Alias of the schedule override | 
 **body** | [**UpdateScheduleOverridePayload**](UpdateScheduleOverridePayload.md)| Request payload of update schedule override | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**UpdateScheduleOverrideResponse**](UpdateScheduleOverrideResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

