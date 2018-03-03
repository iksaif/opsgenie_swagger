# CreateNotificationRulePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the notification rule | 
**action_type** | [**NotificationActionType**](NotificationActionType.md) |  | 
**criteria** | [**Filter**](Filter.md) |  | [optional] 
**notification_time** | [**list[NotifyTime]**](NotifyTime.md) | List of Time Periods that notification for schedule start/end will be sent | [optional] 
**time_restriction** | [**TimeRestrictionInterval**](TimeRestrictionInterval.md) | Time interval that notification rule will work | [optional] 
**schedules** | [**list[ScheduleRecipient]**](ScheduleRecipient.md) | List of schedules that notification rule will be applied when on call of that schedule starts/ends. This field is valid for Schedule Start/End rules | [optional] 
**order** | **int** | The order of the notification rule within the notification rules with the same action type | [optional] 
**steps** | [**list[CreateNotificationRuleStepPayload]**](CreateNotificationRuleStepPayload.md) | List of steps that will be added to notification rule | [optional] 
**repeat** | [**NotificationRepeat**](NotificationRepeat.md) |  | [optional] 
**enabled** | **bool** | Defines if notification rule will be enabled or not when it is created | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


