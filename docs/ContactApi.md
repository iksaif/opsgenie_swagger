# opsgenie_swagger.ContactApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactApi.md#create_contact) | **POST** /v2/users/{identifier}/contacts | Create Contact
[**delete_contact**](ContactApi.md#delete_contact) | **DELETE** /v2/users/{identifier}/contacts/{contactId} | Delete Contact
[**disable_contact**](ContactApi.md#disable_contact) | **POST** /v2/users/{identifier}/contacts/{contactId}/disable | Disable Contact
[**enable_contact**](ContactApi.md#enable_contact) | **POST** /v2/users/{identifier}/contacts/{contactId}/enable | Enable Contact
[**get_contact**](ContactApi.md#get_contact) | **GET** /v2/users/{identifier}/contacts/{contactId} | Get Contact
[**list_contacts**](ContactApi.md#list_contacts) | **GET** /v2/users/{identifier}/contacts | List Contacts
[**update_contact**](ContactApi.md#update_contact) | **PATCH** /v2/users/{identifier}/contacts/{contactId} | Update Contact (Partial)


# **create_contact**
> SuccessResponse create_contact(identifier, body=body)

Create Contact

Creates a new contact

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
api_instance = opsgenie_swagger.ContactApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
body = opsgenie_swagger.CreateContactPayload() # CreateContactPayload | Request payload of creating contact action (optional)

try:
    # Create Contact
    api_response = api_instance.create_contact(identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **body** | [**CreateContactPayload**](CreateContactPayload.md)| Request payload of creating contact action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> SuccessResponse delete_contact(identifier, contact_id)

Delete Contact

Delete contact using contact id

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
api_instance = opsgenie_swagger.ContactApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
contact_id = 'contact_id_example' # str | Id of the contact

try:
    # Delete Contact
    api_response = api_instance.delete_contact(identifier, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **contact_id** | **str**| Id of the contact | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_contact**
> SuccessResponse disable_contact(identifier, contact_id)

Disable Contact

Disable the contact of the user

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
api_instance = opsgenie_swagger.ContactApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
contact_id = 'contact_id_example' # str | Id of the contact

try:
    # Disable Contact
    api_response = api_instance.disable_contact(identifier, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->disable_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **contact_id** | **str**| Id of the contact | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_contact**
> SuccessResponse enable_contact(identifier, contact_id)

Enable Contact

Enable the contact of the user

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
api_instance = opsgenie_swagger.ContactApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
contact_id = 'contact_id_example' # str | Id of the contact

try:
    # Enable Contact
    api_response = api_instance.enable_contact(identifier, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->enable_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **contact_id** | **str**| Id of the contact | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> GetContactResponse get_contact(identifier, contact_id)

Get Contact

Returns contact with given id

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
api_instance = opsgenie_swagger.ContactApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
contact_id = 'contact_id_example' # str | Id of the contact

try:
    # Get Contact
    api_response = api_instance.get_contact(identifier, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **contact_id** | **str**| Id of the contact | 

### Return type

[**GetContactResponse**](GetContactResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> ListContactsResponse list_contacts(identifier)

List Contacts

Returns list of contacts

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
api_instance = opsgenie_swagger.ContactApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched

try:
    # List Contacts
    api_response = api_instance.list_contacts(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->list_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 

### Return type

[**ListContactsResponse**](ListContactsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> SuccessResponse update_contact(identifier, contact_id, body=body)

Update Contact (Partial)

Update contact of the user

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
api_instance = opsgenie_swagger.ContactApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user to be searched
contact_id = 'contact_id_example' # str | Id of the contact
body = opsgenie_swagger.UpdateContactPayload() # UpdateContactPayload | Request payload of update contact action (optional)

try:
    # Update Contact (Partial)
    api_response = api_instance.update_contact(identifier, contact_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user to be searched | 
 **contact_id** | **str**| Id of the contact | 
 **body** | [**UpdateContactPayload**](UpdateContactPayload.md)| Request payload of update contact action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

