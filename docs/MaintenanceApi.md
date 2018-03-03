# opsgenie_swagger.MaintenanceApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_maintenance**](MaintenanceApi.md#cancel_maintenance) | **POST** /v1/maintenance/{id}/cancel | Cancel Maintenance
[**create_maintenance**](MaintenanceApi.md#create_maintenance) | **POST** /v1/maintenance | Create Maintenance
[**delete_maintenance**](MaintenanceApi.md#delete_maintenance) | **DELETE** /v1/maintenance/{id} | Delete Maintenance
[**get_maintenance**](MaintenanceApi.md#get_maintenance) | **GET** /v1/maintenance/{id} | Get Maintenance
[**list_maintenance**](MaintenanceApi.md#list_maintenance) | **GET** /v1/maintenance | List Maintenance
[**update_maintenance**](MaintenanceApi.md#update_maintenance) | **PUT** /v1/maintenance/{id} | Update Maintenance


# **cancel_maintenance**
> SuccessResponse cancel_maintenance(id)

Cancel Maintenance

Cancel maintenance with given id

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
api_instance = opsgenie_swagger.MaintenanceApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Identifier of the maintenance to be searched

try:
    # Cancel Maintenance
    api_response = api_instance.cancel_maintenance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->cancel_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the maintenance to be searched | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_maintenance**
> CreateMaintenanceResponse create_maintenance(body)

Create Maintenance

Creates a new maintenance

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
api_instance = opsgenie_swagger.MaintenanceApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.CreateMaintenancePayload() # CreateMaintenancePayload | Request payload of the maintenance object

try:
    # Create Maintenance
    api_response = api_instance.create_maintenance(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->create_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMaintenancePayload**](CreateMaintenancePayload.md)| Request payload of the maintenance object | 

### Return type

[**CreateMaintenanceResponse**](CreateMaintenanceResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_maintenance**
> SuccessResponse delete_maintenance(id)

Delete Maintenance

Delete maintenance with given identifier

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
api_instance = opsgenie_swagger.MaintenanceApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Identifier of the maintenance to be searched

try:
    # Delete Maintenance
    api_response = api_instance.delete_maintenance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->delete_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the maintenance to be searched | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance**
> GetMaintenanceResponse get_maintenance(id)

Get Maintenance

Returns maintenance with given id

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
api_instance = opsgenie_swagger.MaintenanceApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Identifier of the maintenance to be searched

try:
    # Get Maintenance
    api_response = api_instance.get_maintenance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->get_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the maintenance to be searched | 

### Return type

[**GetMaintenanceResponse**](GetMaintenanceResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_maintenance**
> ListMaintenanceResponse list_maintenance(type=type)

List Maintenance

List maintenance by type

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
api_instance = opsgenie_swagger.MaintenanceApi(opsgenie_swagger.ApiClient(configuration))
type = 'type_example' # str | Type of the maintenance list to be searched (optional)

try:
    # List Maintenance
    api_response = api_instance.list_maintenance(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->list_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of the maintenance list to be searched | [optional] 

### Return type

[**ListMaintenanceResponse**](ListMaintenanceResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_maintenance**
> UpdateMaintenanceResponse update_maintenance(id, body)

Update Maintenance

Update maintenance with given id

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
api_instance = opsgenie_swagger.MaintenanceApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Identifier of the maintenance to be searched
body = opsgenie_swagger.UpdateMaintenancePayload() # UpdateMaintenancePayload | Request payload of the maintenance object

try:
    # Update Maintenance
    api_response = api_instance.update_maintenance(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->update_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the maintenance to be searched | 
 **body** | [**UpdateMaintenancePayload**](UpdateMaintenancePayload.md)| Request payload of the maintenance object | 

### Return type

[**UpdateMaintenanceResponse**](UpdateMaintenanceResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

