# opsgenie_swagger.TeamRoutingRuleApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_team_routing_rule_order**](TeamRoutingRuleApi.md#change_team_routing_rule_order) | **POST** /v2/teams/{identifier}/routing-rules/{id}/change-order | Change Team Routing Rule Order
[**create_team_routing_rule**](TeamRoutingRuleApi.md#create_team_routing_rule) | **POST** /v2/teams/{identifier}/routing-rules | Create Team Routing Rule
[**delete_team_routing_rule**](TeamRoutingRuleApi.md#delete_team_routing_rule) | **DELETE** /v2/teams/{identifier}/routing-rules/{id} | Delete Team Routing Rule
[**get_team_routing_rule**](TeamRoutingRuleApi.md#get_team_routing_rule) | **GET** /v2/teams/{identifier}/routing-rules/{id} | Get Team Routing Rule
[**list_team_routing_rules**](TeamRoutingRuleApi.md#list_team_routing_rules) | **GET** /v2/teams/{identifier}/routing-rules | List Team Routing Rules
[**update_team_routing_rule**](TeamRoutingRuleApi.md#update_team_routing_rule) | **PATCH** /v2/teams/{identifier}/routing-rules/{id} | Update Team Routing Rule (Partial)


# **change_team_routing_rule_order**
> SuccessResponse change_team_routing_rule_order(identifier, id, body, team_identifier_type=team_identifier_type)

Change Team Routing Rule Order

Change the order of team routing rule with given id

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
api_instance = opsgenie_swagger.TeamRoutingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
id = 'id_example' # str | Id of the team routing rule
body = opsgenie_swagger.ChangeTeamRoutingRuleOrderPayload() # ChangeTeamRoutingRuleOrderPayload | Request payload of change team routing rule order action
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Change Team Routing Rule Order
    api_response = api_instance.change_team_routing_rule_order(identifier, id, body, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoutingRuleApi->change_team_routing_rule_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **id** | **str**| Id of the team routing rule | 
 **body** | [**ChangeTeamRoutingRuleOrderPayload**](ChangeTeamRoutingRuleOrderPayload.md)| Request payload of change team routing rule order action | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team_routing_rule**
> SuccessResponse create_team_routing_rule(identifier, body, team_identifier_type=team_identifier_type)

Create Team Routing Rule

Creates a new team routing rule

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
api_instance = opsgenie_swagger.TeamRoutingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
body = opsgenie_swagger.CreateTeamRoutingRulePayload() # CreateTeamRoutingRulePayload | Request payload of createTeamRoutingRule
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Create Team Routing Rule
    api_response = api_instance.create_team_routing_rule(identifier, body, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoutingRuleApi->create_team_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **body** | [**CreateTeamRoutingRulePayload**](CreateTeamRoutingRulePayload.md)| Request payload of createTeamRoutingRule | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_routing_rule**
> SuccessResponse delete_team_routing_rule(identifier, id, team_identifier_type=team_identifier_type)

Delete Team Routing Rule

Delete team routing rule with given id

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
api_instance = opsgenie_swagger.TeamRoutingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
id = 'id_example' # str | Id of the team routing rule
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Delete Team Routing Rule
    api_response = api_instance.delete_team_routing_rule(identifier, id, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoutingRuleApi->delete_team_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **id** | **str**| Id of the team routing rule | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_routing_rule**
> GetTeamRoutingRuleResponse get_team_routing_rule(identifier, id, team_identifier_type=team_identifier_type)

Get Team Routing Rule

Returns team routing rule with given id

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
api_instance = opsgenie_swagger.TeamRoutingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
id = 'id_example' # str | Id of the team routing rule
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # Get Team Routing Rule
    api_response = api_instance.get_team_routing_rule(identifier, id, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoutingRuleApi->get_team_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **id** | **str**| Id of the team routing rule | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**GetTeamRoutingRuleResponse**](GetTeamRoutingRuleResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_routing_rules**
> ListTeamRoutingRulesResponse list_team_routing_rules(identifier, team_identifier_type=team_identifier_type)

List Team Routing Rules

Returns list of team routing rules

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
api_instance = opsgenie_swagger.TeamRoutingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)

try:
    # List Team Routing Rules
    api_response = api_instance.list_team_routing_rules(identifier, team_identifier_type=team_identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoutingRuleApi->list_team_routing_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]

### Return type

[**ListTeamRoutingRulesResponse**](ListTeamRoutingRulesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_routing_rule**
> SuccessResponse update_team_routing_rule(identifier, id, team_identifier_type=team_identifier_type, body=body)

Update Team Routing Rule (Partial)

Update routing rule of the team

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
api_instance = opsgenie_swagger.TeamRoutingRuleApi(opsgenie_swagger.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the team
id = 'id_example' # str | Id of the team routing rule
team_identifier_type = 'id' # str | Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id' (optional) (default to id)
body = opsgenie_swagger.UpdateTeamRoutingRulePayload() # UpdateTeamRoutingRulePayload | Request payload of update Team Routing Rule action (optional)

try:
    # Update Team Routing Rule (Partial)
    api_response = api_instance.update_team_routing_rule(identifier, id, team_identifier_type=team_identifier_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamRoutingRuleApi->update_team_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the team | 
 **id** | **str**| Id of the team routing rule | 
 **team_identifier_type** | **str**| Type of the identifier. Possible values are &#39;id&#39; and &#39;name&#39;. Default value is &#39;id&#39; | [optional] [default to id]
 **body** | [**UpdateTeamRoutingRulePayload**](UpdateTeamRoutingRulePayload.md)| Request payload of update Team Routing Rule action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

