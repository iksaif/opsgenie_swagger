# CreateScheduleOverridePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A user defined identifier for the override | 
**user** | [**Recipient**](Recipient.md) | The user object who will take on call responsibility or reserved word none | 
**start_date** | **datetime** | Time for override starting | 
**end_date** | **datetime** | Time for override ending | 
**rotations** | [**list[ScheduleOverrideRotation]**](ScheduleOverrideRotation.md) | Identifier (id or name) of rotations that override will apply. When it&#39;s set, only specified schedule rotations will be overridden | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


