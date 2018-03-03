# AutoTaskEmailIntegration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suppress_notifications** | **bool** | If enabled, notifications that come from alerts will be suppressed. Defaults to false | [optional] 
**ignore_teams_from_payload** | **bool** | If enabled, the integration will ignore teams sent in request payloads. Defaults to false | [optional] 
**ignore_recipients_from_payload** | **bool** | If enabled, the integration will ignore recipients sent in request payloads. Defaults to false | [optional] 
**recipients** | [**list[Recipient]**](Recipient.md) | Optional user, schedule, teams or escalation names to calculate which users will receive the notifications of the alert. Recipients which are exceeding the limit are ignored | [optional] 
**is_advanced** | **bool** |  | [optional] 
**feature_type** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**email_username** | **str** | The username part of the email address. It must be unique for each integration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


