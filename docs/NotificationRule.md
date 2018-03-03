# NotificationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**action_type** | [**NotificationActionType**](NotificationActionType.md) |  | [optional] 
**criteria** | [**Filter**](Filter.md) |  | [optional] 
**notification_time** | [**list[NotifyTime]**](NotifyTime.md) |  | [optional] 
**order** | **int** |  | [optional] 
**time_restriction** | [**TimeRestrictionInterval**](TimeRestrictionInterval.md) |  | [optional] 
**steps** | [**list[NotificationRuleStep]**](NotificationRuleStep.md) |  | [optional] 
**schedules** | [**list[ScheduleRecipient]**](ScheduleRecipient.md) |  | [optional] 
**repeat** | [**NotificationRepeat**](NotificationRepeat.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


