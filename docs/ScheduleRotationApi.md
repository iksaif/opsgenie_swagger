# opsgenie_swagger.ScheduleRotationApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_rotation**](ScheduleRotationApi.md#create_schedule_rotation) | **POST** /v2/schedules/{identifier}/rotations | Create Schedule Rotation
[**delete_schedule_rotation**](ScheduleRotationApi.md#delete_schedule_rotation) | **DELETE** /v2/schedules/{identifier}/rotations/{id} | Delete Schedule Rotation
[**get_schedule_rotation**](ScheduleRotationApi.md#get_schedule_rotation) | **GET** /v2/schedules/{identifier}/rotations/{id} | Get Schedule Rotation
[**list_schedule_rotations**](ScheduleRotationApi.md#list_schedule_rotations) | **GET** /v2/schedules/{identifier}/rotations | List Schedule Rotations
[**update_schedule_rotation**](ScheduleRotationApi.md#update_schedule_rotation) | **PATCH** /v2/schedules/{identifier}/rotations/{id} | Update Schedule Rotation (Partial)


# **create_schedule_rotation**
> SuccessResponse create_schedule_rotation(identifier, body, schedule_identifier_type=schedule_identifier_type)

Create Schedule Rotation

Creates a new schedule rotation

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
api_instance = opsgenie_swagger.ScheduleRotationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
body = opsgenie_swagger.CreateScheduleRotationPayload() # CreateScheduleRotationPayload | Request payload of created schedule rotation
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Create Schedule Rotation
    api_response = api_instance.create_schedule_rotation(identifier, body, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleRotationApi->create_schedule_rotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **body** | [**CreateScheduleRotationPayload**](CreateScheduleRotationPayload.md)| Request payload of created schedule rotation | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule_rotation**
> SuccessResponse delete_schedule_rotation(identifier, id, schedule_identifier_type=schedule_identifier_type)

Delete Schedule Rotation

Delete schedule rotation with given identifier

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
api_instance = opsgenie_swagger.ScheduleRotationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
id = 'id_example' # str | Identifier of schedule rotation
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Delete Schedule Rotation
    api_response = api_instance.delete_schedule_rotation(identifier, id, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleRotationApi->delete_schedule_rotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **id** | **str**| Identifier of schedule rotation | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_rotation**
> GetScheduleRotationResponse get_schedule_rotation(identifier, id, schedule_identifier_type=schedule_identifier_type)

Get Schedule Rotation

Returns schedule rotation with given id

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
api_instance = opsgenie_swagger.ScheduleRotationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
id = 'id_example' # str | Identifier of schedule rotation
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Get Schedule Rotation
    api_response = api_instance.get_schedule_rotation(identifier, id, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleRotationApi->get_schedule_rotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **id** | **str**| Identifier of schedule rotation | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**GetScheduleRotationResponse**](GetScheduleRotationResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedule_rotations**
> ListScheduleRotationsResponse list_schedule_rotations(identifier, schedule_identifier_type=schedule_identifier_type)

List Schedule Rotations

Returns list of schedule rotations

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
api_instance = opsgenie_swagger.ScheduleRotationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # List Schedule Rotations
    api_response = api_instance.list_schedule_rotations(identifier, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleRotationApi->list_schedule_rotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**ListScheduleRotationsResponse**](ListScheduleRotationsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule_rotation**
> SuccessResponse update_schedule_rotation(identifier, id, body, schedule_identifier_type=schedule_identifier_type)

Update Schedule Rotation (Partial)

Update schedule rotation with given id

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
api_instance = opsgenie_swagger.ScheduleRotationApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of schedule which could be id or name
id = 'id_example' # str | Identifier of schedule rotation
body = opsgenie_swagger.UpdateScheduleRotationPayload() # UpdateScheduleRotationPayload | Request payload of update schedule rotation action
schedule_identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name' (optional) (default to id)

try:
    # Update Schedule Rotation (Partial)
    api_response = api_instance.update_schedule_rotation(identifier, id, body, schedule_identifier_type=schedule_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleRotationApi->update_schedule_rotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of schedule which could be id or name | 
 **id** | **str**| Identifier of schedule rotation | 
 **body** | [**UpdateScheduleRotationPayload**](UpdateScheduleRotationPayload.md)| Request payload of update schedule rotation action | 
 **schedule_identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;name&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

