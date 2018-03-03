# UpdateScheduleRotationPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of rotation | [optional] 
**start_date** | **datetime** | Defines a date time as an override start. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically | [optional] 
**end_date** | **datetime** | Defines a date time as an override end. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically | [optional] 
**type** | **str** | Type of rotation. May be one of &#39;daily&#39;, &#39;weekly&#39; and &#39;hourly&#39; | [optional] 
**length** | **int** | Length of the rotation with default value 1 | [optional] 
**participants** | [**list[Recipient]**](Recipient.md) | List of escalations, teams, users or the reserved word none which will be used in schedule. Each of them can be used multiple times and will be rotated in the order they given. | [optional] 
**time_restriction** | [**TimeRestrictionInterval**](TimeRestrictionInterval.md) | Used to limit schedule rotation to certain day and time of the week, using multiple start and end times for each day of the week. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


