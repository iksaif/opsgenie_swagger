# CreateSchedulePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the schedule | 
**description** | **str** | The description of schedule | [optional] 
**timezone** | **str** | Timezone of schedule | [optional] 
**enabled** | **bool** | Enable/disable state of schedule | [optional] 
**owner_team** | [**TeamMeta**](TeamMeta.md) | Owner team of the schedule, consisting id and/or name of the owner team | [optional] 
**rotations** | [**list[CreateScheduleRotationPayload]**](CreateScheduleRotationPayload.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


