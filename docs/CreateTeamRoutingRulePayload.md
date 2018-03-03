# CreateTeamRoutingRulePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the team routing rule | [optional] 
**order** | **int** | Order of team routing rule within the rules. order value is actually the index of the team routing rule. | [optional] 
**criteria** | [**Filter**](Filter.md) |  | [optional] 
**time_restriction** | [**TimeRestrictionInterval**](TimeRestrictionInterval.md) |  | [optional] 
**notify** | [**Recipient**](Recipient.md) |  | 
**timezone** | **str** | Timezone of team routing rule. If timezone field is not given, account timezone is used as default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


