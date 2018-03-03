# JiraServiceDeskIntegration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suppress_notifications** | **bool** | If enabled, notifications that come from alerts will be suppressed. Defaults to false | [optional] 
**ignore_teams_from_payload** | **bool** | If enabled, the integration will ignore teams sent in request payloads. Defaults to false | [optional] 
**ignore_recipients_from_payload** | **bool** | If enabled, the integration will ignore recipients sent in request payloads. Defaults to false | [optional] 
**recipients** | [**list[Recipient]**](Recipient.md) | Optional user, schedule, teams or escalation names to calculate which users will receive the notifications of the alert. Recipients which are exceeding the limit are ignored | [optional] 
**is_advanced** | **bool** |  | [optional] 
**feature_type** | **str** |  | [optional] 
**allow_configuration_access** | **bool** | This parameter is for allowing or restricting the configuration access. If configuration access is restricted, the integration will be limited to Alert API requests and sending heartbeats. Defaults to false | [optional] 
**allow_write_access** | **bool** | This parameter is for configuring the read-only access of integration. If the integration is limited to read-only access, the integration will not be authorized to perform any create, update or delete action within any domain. Defaults to true | [optional] 
**alert_filter** | [**AlertFilter**](AlertFilter.md) |  | [optional] 
**forwarding_enabled** | **bool** |  | [optional] 
**forwarding_action_mappings** | [**list[ActionMapping]**](ActionMapping.md) |  | [optional] 
**callback_type** | **str** |  | [optional] 
**updates_action_mappings** | [**list[ActionMapping]**](ActionMapping.md) |  | [optional] 
**updates_enabled** | **bool** |  | [optional] 
**bidirectional_callback_type** | **str** |  | [optional] 
**jira_username** | **str** |  | [optional] 
**jira_password** | **str** |  | [optional] 
**jira_url** | **str** |  | [optional] 
**project_key** | **str** |  | [optional] 
**issue_type_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


