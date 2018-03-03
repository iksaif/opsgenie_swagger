# UpdateUserPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | E-mail address of the user | [optional] 
**full_name** | **str** | Name of the user | [optional] 
**role** | [**UserRole**](UserRole.md) | Role of user. It may be one of owner, admin, user or the name of a custom role you&#39;ve created. | [optional] 
**skype_username** | **str** | Skype username of the user | [optional] 
**time_zone** | **str** | Timezone of the user. If not set, timezone of the customer will be used instead. | [optional] 
**locale** | **str** | Location information of the user. If not set, locale of the customer will be used instead. | [optional] 
**user_address** | [**UserAddress**](UserAddress.md) | Address of the user | [optional] 
**tags** | **list[str]** | List of labels attached to the user. You can label users to differentiate them from the rest. For example, you can add ITManager tag to differentiate people with this role from others. | [optional] 
**details** | **dict(str, list[str])** | Set of user defined properties. | [optional] 
**invitation_disabled** | **bool** | Invitation email will not be sent if set to true. Default value is false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


