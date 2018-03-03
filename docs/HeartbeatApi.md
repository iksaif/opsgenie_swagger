# opsgenie_swagger.HeartbeatApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_heartbeat**](HeartbeatApi.md#create_heartbeat) | **POST** /v2/heartbeats | Create Heartbeat
[**delete_heartbeat**](HeartbeatApi.md#delete_heartbeat) | **DELETE** /v2/heartbeats/{name} | Delete Heartbeat
[**disable_heartbeat**](HeartbeatApi.md#disable_heartbeat) | **POST** /v2/heartbeats/{name}/disable | Disable Heartbeat
[**enable_heartbeat**](HeartbeatApi.md#enable_heartbeat) | **POST** /v2/heartbeats/{name}/enable | Enable Heartbeat
[**get_heartbeat**](HeartbeatApi.md#get_heartbeat) | **GET** /v2/heartbeats/{name} | Get Heartbeat
[**ping**](HeartbeatApi.md#ping) | **GET** /v2/heartbeats/{name}/ping | Ping Heartbeat
[**update_heartbeat**](HeartbeatApi.md#update_heartbeat) | **PATCH** /v2/heartbeats/{name} | Update Heartbeat (Partial)


# **create_heartbeat**
> CreateHeartbeatResponse create_heartbeat(body)

Create Heartbeat

Create a new heartbeat

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
api_instance = opsgenie_swagger.HeartbeatApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateHeartbeatPayload() # CreateHeartbeatPayload | Request payload of created heartbeat

try:
    # Create Heartbeat
    api_response = api_instance.create_heartbeat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->create_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateHeartbeatPayload**](CreateHeartbeatPayload.md)| Request payload of created heartbeat | 

### Return type

[**CreateHeartbeatResponse**](CreateHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_heartbeat**
> SuccessResponse delete_heartbeat(name)

Delete Heartbeat

Delete heartbeat with given name

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
api_instance = opsgenie_swagger.HeartbeatApi(opsgenie_swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Delete Heartbeat
    api_response = api_instance.delete_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->delete_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_heartbeat**
> DisableHeartbeatResponse disable_heartbeat(name)

Disable Heartbeat

Disable heartbeat request with given name

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
api_instance = opsgenie_swagger.HeartbeatApi(opsgenie_swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Disable Heartbeat
    api_response = api_instance.disable_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->disable_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**DisableHeartbeatResponse**](DisableHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_heartbeat**
> EnableHeartbeatResponse enable_heartbeat(name)

Enable Heartbeat

Enable heartbeat request with given name

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
api_instance = opsgenie_swagger.HeartbeatApi(opsgenie_swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Enable Heartbeat
    api_response = api_instance.enable_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->enable_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**EnableHeartbeatResponse**](EnableHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heartbeat**
> GetHeartbeatResponse get_heartbeat(name)

Get Heartbeat

Returns heartbeat with given name

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
api_instance = opsgenie_swagger.HeartbeatApi(opsgenie_swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Get Heartbeat
    api_response = api_instance.get_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->get_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**GetHeartbeatResponse**](GetHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> SuccessResponse ping(name)

Ping Heartbeat

Ping Heartbeat for given heartbeat name

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
api_instance = opsgenie_swagger.HeartbeatApi(opsgenie_swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Ping Heartbeat
    api_response = api_instance.ping(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_heartbeat**
> UpdateHeartbeatResponse update_heartbeat(name, body=body)

Update Heartbeat (Partial)

Update Heartbeatwith given name

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
api_instance = opsgenie_swagger.HeartbeatApi(opsgenie_swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat
body = opsgenie_swagger.UpdateHeartbeatPayload() # UpdateHeartbeatPayload | Request payload of update heartbeat action (optional)

try:
    # Update Heartbeat (Partial)
    api_response = api_instance.update_heartbeat(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->update_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 
 **body** | [**UpdateHeartbeatPayload**](UpdateHeartbeatPayload.md)| Request payload of update heartbeat action | [optional] 

### Return type

[**UpdateHeartbeatResponse**](UpdateHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

