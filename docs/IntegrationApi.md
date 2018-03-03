# opsgenie_swagger.IntegrationApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_integration**](IntegrationApi.md#authenticate_integration) | **POST** /v2/integrations/authenticate | Authenticate Integration
[**create_integration**](IntegrationApi.md#create_integration) | **POST** /v2/integrations | Create Integration
[**delete_integration**](IntegrationApi.md#delete_integration) | **DELETE** /v2/integrations/{id} | Delete Integration
[**disable_integration**](IntegrationApi.md#disable_integration) | **POST** /v2/integrations/{id}/disable | Disable Integration
[**enable_integration**](IntegrationApi.md#enable_integration) | **POST** /v2/integrations/{id}/enable | Enable Integration
[**get_integration**](IntegrationApi.md#get_integration) | **GET** /v2/integrations/{id} | Get Integration
[**list_integrations**](IntegrationApi.md#list_integrations) | **GET** /v2/integrations | List Integrations
[**update_integration**](IntegrationApi.md#update_integration) | **PUT** /v2/integrations/{id} | Update Integration


# **authenticate_integration**
> SuccessResponse authenticate_integration(body)

Authenticate Integration

Authenticates integration with given type

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.AuthenticateIntegrationPayload() # AuthenticateIntegrationPayload | Request payload to authenticate integration

try:
    # Authenticate Integration
    api_response = api_instance.authenticate_integration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->authenticate_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticateIntegrationPayload**](AuthenticateIntegrationPayload.md)| Request payload to authenticate integration | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_integration**
> CreateIntegrationResponse create_integration(body)

Create Integration

Creates a new integration

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.Integration() # Integration | Request payload of created integration

try:
    # Create Integration
    api_response = api_instance.create_integration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Integration**](Integration.md)| Request payload of created integration | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration**
> SuccessResponse delete_integration(id)

Delete Integration

Delete integration with given id

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id

try:
    # Delete Integration
    api_response = api_instance.delete_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_integration**
> DisableIntegrationResponse disable_integration(id)

Disable Integration

Disable integration with given ID

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id

try:
    # Disable Integration
    api_response = api_instance.disable_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->disable_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 

### Return type

[**DisableIntegrationResponse**](DisableIntegrationResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_integration**
> EnableIntegrationResponse enable_integration(id)

Enable Integration

Enable integration with given ID

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id

try:
    # Enable Integration
    api_response = api_instance.enable_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->enable_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 

### Return type

[**EnableIntegrationResponse**](EnableIntegrationResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration**
> GetIntegrationResponse get_integration(id)

Get Integration

Returns integration with given id

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id

try:
    # Get Integration
    api_response = api_instance.get_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 

### Return type

[**GetIntegrationResponse**](GetIntegrationResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integrations**
> ListIntegrationsResponse list_integrations(type=type, team_id=team_id, team_name=team_name)

List Integrations

Returns list of integrations with given parameters

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
type = 'type_example' # str | Type of the integration (For instance, \"API\" for API Integration). If type parameter is given, the result will be filtered by type (optional)
team_id = 'team_id_example' # str | The ID of the team. If the team ID parameter is given, the result will be filtered by teamId (optional)
team_name = 'team_name_example' # str | The name of the team. If the team name parameter is given, the result will be filtered by teamName (optional)

try:
    # List Integrations
    api_response = api_instance.list_integrations(type=type, team_id=team_id, team_name=team_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->list_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of the integration (For instance, \&quot;API\&quot; for API Integration). If type parameter is given, the result will be filtered by type | [optional] 
 **team_id** | **str**| The ID of the team. If the team ID parameter is given, the result will be filtered by teamId | [optional] 
 **team_name** | **str**| The name of the team. If the team name parameter is given, the result will be filtered by teamName | [optional] 

### Return type

[**ListIntegrationsResponse**](ListIntegrationsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration**
> UpdateIntegrationResponse update_integration(id, body)

Update Integration

Update integration with given id

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
api_instance = opsgenie_swagger.IntegrationApi(opsgenie_swagger.ApiClient(configuration))
id = 'id_example' # str | Integration Id
body = opsgenie_swagger.Integration() # Integration | Request payload of update integration action

try:
    # Update Integration
    api_response = api_instance.update_integration(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration Id | 
 **body** | [**Integration**](Integration.md)| Request payload of update integration action | 

### Return type

[**UpdateIntegrationResponse**](UpdateIntegrationResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

