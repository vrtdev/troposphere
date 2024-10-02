# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class AttributeItem(AWSProperty):
    """
    `AttributeItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class AttributeDetails(AWSProperty):
    """
    `AttributeDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html>`__
    """

    props: PropsDictType = {
        "Attributes": ([AttributeItem], True),
        "Expression": (str, True),
    }


class Range(AWSProperty):
    """
    `Range <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html>`__
    """

    props: PropsDictType = {
        "Unit": (str, True),
        "Value": (integer, True),
    }


class Threshold(AWSProperty):
    """
    `Threshold <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html>`__
    """

    props: PropsDictType = {
        "Operator": (str, True),
        "Value": (str, True),
    }


class Conditions(AWSProperty):
    """
    `Conditions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html>`__
    """

    props: PropsDictType = {
        "ObjectCount": (integer, False),
        "Range": (Range, False),
        "Threshold": (Threshold, False),
    }


class CalculatedAttributeDefinition(AWSObject):
    """
    `CalculatedAttributeDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html>`__
    """

    resource_type = "AWS::CustomerProfiles::CalculatedAttributeDefinition"

    props: PropsDictType = {
        "AttributeDetails": (AttributeDetails, True),
        "CalculatedAttributeName": (str, True),
        "Conditions": (Conditions, False),
        "Description": (str, False),
        "DisplayName": (str, False),
        "DomainName": (str, True),
        "Statistic": (str, True),
        "Tags": (Tags, False),
    }


class ConflictResolution(AWSProperty):
    """
    `ConflictResolution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-conflictresolution.html>`__
    """

    props: PropsDictType = {
        "ConflictResolvingModel": (str, True),
        "SourceName": (str, False),
    }


class Consolidation(AWSProperty):
    """
    `Consolidation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-consolidation.html>`__
    """

    props: PropsDictType = {
        "MatchingAttributesList": (dict, True),
    }


class AutoMerging(AWSProperty):
    """
    `AutoMerging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html>`__
    """

    props: PropsDictType = {
        "ConflictResolution": (ConflictResolution, False),
        "Consolidation": (Consolidation, False),
        "Enabled": (boolean, True),
        "MinAllowedConfidenceScoreForMerging": (double, False),
    }


class S3ExportingConfig(AWSProperty):
    """
    `S3ExportingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-s3exportingconfig.html>`__
    """

    props: PropsDictType = {
        "S3BucketName": (str, True),
        "S3KeyName": (str, False),
    }


class ExportingConfig(AWSProperty):
    """
    `ExportingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-exportingconfig.html>`__
    """

    props: PropsDictType = {
        "S3Exporting": (S3ExportingConfig, False),
    }


class JobSchedule(AWSProperty):
    """
    `JobSchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-jobschedule.html>`__
    """

    props: PropsDictType = {
        "DayOfTheWeek": (str, True),
        "Time": (str, True),
    }


class Matching(AWSProperty):
    """
    `Matching <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html>`__
    """

    props: PropsDictType = {
        "AutoMerging": (AutoMerging, False),
        "Enabled": (boolean, True),
        "ExportingConfig": (ExportingConfig, False),
        "JobSchedule": (JobSchedule, False),
    }


class AttributeTypesSelector(AWSProperty):
    """
    `AttributeTypesSelector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html>`__
    """

    props: PropsDictType = {
        "Address": ([str], False),
        "AttributeMatchingModel": (str, True),
        "EmailAddress": ([str], False),
        "PhoneNumber": ([str], False),
    }


class MatchingRule(AWSProperty):
    """
    `MatchingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matchingrule.html>`__
    """

    props: PropsDictType = {
        "Rule": ([str], True),
    }


class RuleBasedMatching(AWSProperty):
    """
    `RuleBasedMatching <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html>`__
    """

    props: PropsDictType = {
        "AttributeTypesSelector": (AttributeTypesSelector, False),
        "ConflictResolution": (ConflictResolution, False),
        "Enabled": (boolean, True),
        "ExportingConfig": (ExportingConfig, False),
        "MatchingRules": ([MatchingRule], False),
        "MaxAllowedRuleLevelForMatching": (integer, False),
        "MaxAllowedRuleLevelForMerging": (integer, False),
        "Status": (str, False),
    }


class Domain(AWSObject):
    """
    `Domain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html>`__
    """

    resource_type = "AWS::CustomerProfiles::Domain"

    props: PropsDictType = {
        "DeadLetterQueueUrl": (str, False),
        "DefaultEncryptionKey": (str, False),
        "DefaultExpirationDays": (integer, True),
        "DomainName": (str, True),
        "Matching": (Matching, False),
        "RuleBasedMatching": (RuleBasedMatching, False),
        "Tags": (Tags, False),
    }


class EventStream(AWSObject):
    """
    `EventStream <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html>`__
    """

    resource_type = "AWS::CustomerProfiles::EventStream"

    props: PropsDictType = {
        "DomainName": (str, True),
        "EventStreamName": (str, True),
        "Tags": (Tags, False),
        "Uri": (str, True),
    }


class IncrementalPullConfig(AWSProperty):
    """
    `IncrementalPullConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html>`__
    """

    props: PropsDictType = {
        "DatetimeTypeFieldName": (str, False),
    }


class MarketoSourceProperties(AWSProperty):
    """
    `MarketoSourceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html>`__
    """

    props: PropsDictType = {
        "Object": (str, True),
    }


class S3SourceProperties(AWSProperty):
    """
    `S3SourceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "BucketPrefix": (str, False),
    }


class SalesforceSourceProperties(AWSProperty):
    """
    `SalesforceSourceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html>`__
    """

    props: PropsDictType = {
        "EnableDynamicFieldUpdate": (boolean, False),
        "IncludeDeletedRecords": (boolean, False),
        "Object": (str, True),
    }


class ServiceNowSourceProperties(AWSProperty):
    """
    `ServiceNowSourceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html>`__
    """

    props: PropsDictType = {
        "Object": (str, True),
    }


class ZendeskSourceProperties(AWSProperty):
    """
    `ZendeskSourceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html>`__
    """

    props: PropsDictType = {
        "Object": (str, True),
    }


class SourceConnectorProperties(AWSProperty):
    """
    `SourceConnectorProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html>`__
    """

    props: PropsDictType = {
        "Marketo": (MarketoSourceProperties, False),
        "S3": (S3SourceProperties, False),
        "Salesforce": (SalesforceSourceProperties, False),
        "ServiceNow": (ServiceNowSourceProperties, False),
        "Zendesk": (ZendeskSourceProperties, False),
    }


class SourceFlowConfig(AWSProperty):
    """
    `SourceFlowConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html>`__
    """

    props: PropsDictType = {
        "ConnectorProfileName": (str, False),
        "ConnectorType": (str, True),
        "IncrementalPullConfig": (IncrementalPullConfig, False),
        "SourceConnectorProperties": (SourceConnectorProperties, True),
    }


class ConnectorOperator(AWSProperty):
    """
    `ConnectorOperator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html>`__
    """

    props: PropsDictType = {
        "Marketo": (str, False),
        "S3": (str, False),
        "Salesforce": (str, False),
        "ServiceNow": (str, False),
        "Zendesk": (str, False),
    }


class TaskPropertiesMap(AWSProperty):
    """
    `TaskPropertiesMap <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html>`__
    """

    props: PropsDictType = {
        "OperatorPropertyKey": (str, True),
        "Property": (str, True),
    }


class Task(AWSProperty):
    """
    `Task <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html>`__
    """

    props: PropsDictType = {
        "ConnectorOperator": (ConnectorOperator, False),
        "DestinationField": (str, False),
        "SourceFields": ([str], True),
        "TaskProperties": ([TaskPropertiesMap], False),
        "TaskType": (str, True),
    }


class ScheduledTriggerProperties(AWSProperty):
    """
    `ScheduledTriggerProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html>`__
    """

    props: PropsDictType = {
        "DataPullMode": (str, False),
        "FirstExecutionFrom": (double, False),
        "ScheduleEndTime": (double, False),
        "ScheduleExpression": (str, True),
        "ScheduleOffset": (integer, False),
        "ScheduleStartTime": (double, False),
        "Timezone": (str, False),
    }


class TriggerProperties(AWSProperty):
    """
    `TriggerProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html>`__
    """

    props: PropsDictType = {
        "Scheduled": (ScheduledTriggerProperties, False),
    }


class TriggerConfig(AWSProperty):
    """
    `TriggerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html>`__
    """

    props: PropsDictType = {
        "TriggerProperties": (TriggerProperties, False),
        "TriggerType": (str, True),
    }


class FlowDefinition(AWSProperty):
    """
    `FlowDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "FlowName": (str, True),
        "KmsArn": (str, True),
        "SourceFlowConfig": (SourceFlowConfig, True),
        "Tasks": ([Task], True),
        "TriggerConfig": (TriggerConfig, True),
    }


class ObjectTypeMapping(AWSProperty):
    """
    `ObjectTypeMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class Integration(AWSObject):
    """
    `Integration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html>`__
    """

    resource_type = "AWS::CustomerProfiles::Integration"

    props: PropsDictType = {
        "DomainName": (str, True),
        "FlowDefinition": (FlowDefinition, False),
        "ObjectTypeName": (str, False),
        "ObjectTypeNames": ([ObjectTypeMapping], False),
        "Tags": (Tags, False),
        "Uri": (str, False),
    }


class ObjectTypeField(AWSProperty):
    """
    `ObjectTypeField <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html>`__
    """

    props: PropsDictType = {
        "ContentType": (str, False),
        "Source": (str, False),
        "Target": (str, False),
    }


class FieldMap(AWSProperty):
    """
    `FieldMap <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "ObjectTypeField": (ObjectTypeField, False),
    }


class ObjectTypeKey(AWSProperty):
    """
    `ObjectTypeKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html>`__
    """

    props: PropsDictType = {
        "FieldNames": ([str], False),
        "StandardIdentifiers": ([str], False),
    }


class KeyMap(AWSProperty):
    """
    `KeyMap <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "ObjectTypeKeyList": ([ObjectTypeKey], False),
    }


class ObjectType(AWSObject):
    """
    `ObjectType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html>`__
    """

    resource_type = "AWS::CustomerProfiles::ObjectType"

    props: PropsDictType = {
        "AllowProfileCreation": (boolean, False),
        "Description": (str, True),
        "DomainName": (str, True),
        "EncryptionKey": (str, False),
        "ExpirationDays": (integer, False),
        "Fields": ([FieldMap], False),
        "Keys": ([KeyMap], False),
        "ObjectTypeName": (str, True),
        "SourceLastUpdatedTimestampFormat": (str, False),
        "Tags": (Tags, False),
        "TemplateId": (str, False),
    }


class DestinationDetails(AWSProperty):
    """
    `DestinationDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
        "Uri": (str, True),
    }


class DomainStats(AWSProperty):
    """
    `DomainStats <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html>`__
    """

    props: PropsDictType = {
        "MeteringProfileCount": (double, False),
        "ObjectCount": (double, False),
        "ProfileCount": (double, False),
        "TotalSize": (double, False),
    }
