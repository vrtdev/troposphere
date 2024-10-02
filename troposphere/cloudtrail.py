# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class Destination(AWSProperty):
    """
    `Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-channel-destination.html>`__
    """

    props: PropsDictType = {
        "Location": (str, True),
        "Type": (str, True),
    }


class Channel(AWSObject):
    """
    `Channel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html>`__
    """

    resource_type = "AWS::CloudTrail::Channel"

    props: PropsDictType = {
        "Destinations": ([Destination], False),
        "Name": (str, False),
        "Source": (str, False),
        "Tags": (Tags, False),
    }


class AdvancedFieldSelector(AWSProperty):
    """
    `AdvancedFieldSelector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html>`__
    """

    props: PropsDictType = {
        "EndsWith": ([str], False),
        "Equals": ([str], False),
        "Field": (str, True),
        "NotEndsWith": ([str], False),
        "NotEquals": ([str], False),
        "NotStartsWith": ([str], False),
        "StartsWith": ([str], False),
    }


class AdvancedEventSelector(AWSProperty):
    """
    `AdvancedEventSelector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedeventselector.html>`__
    """

    props: PropsDictType = {
        "FieldSelectors": ([AdvancedFieldSelector], True),
        "Name": (str, False),
    }


class InsightSelector(AWSProperty):
    """
    `InsightSelector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html>`__
    """

    props: PropsDictType = {
        "InsightType": (str, False),
    }


class EventDataStore(AWSObject):
    """
    `EventDataStore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html>`__
    """

    resource_type = "AWS::CloudTrail::EventDataStore"

    props: PropsDictType = {
        "AdvancedEventSelectors": ([AdvancedEventSelector], False),
        "BillingMode": (str, False),
        "FederationEnabled": (boolean, False),
        "FederationRoleArn": (str, False),
        "IngestionEnabled": (boolean, False),
        "InsightSelectors": ([InsightSelector], False),
        "InsightsDestination": (str, False),
        "KmsKeyId": (str, False),
        "MultiRegionEnabled": (boolean, False),
        "Name": (str, False),
        "OrganizationEnabled": (boolean, False),
        "RetentionPeriod": (integer, False),
        "Tags": (Tags, False),
        "TerminationProtectionEnabled": (boolean, False),
    }


class ResourcePolicy(AWSObject):
    """
    `ResourcePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html>`__
    """

    resource_type = "AWS::CloudTrail::ResourcePolicy"

    props: PropsDictType = {
        "ResourceArn": (str, True),
        "ResourcePolicy": (dict, True),
    }


class DataResource(AWSProperty):
    """
    `DataResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Values": ([str], False),
    }


class EventSelector(AWSProperty):
    """
    `EventSelector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html>`__
    """

    props: PropsDictType = {
        "DataResources": ([DataResource], False),
        "ExcludeManagementEventSources": ([str], False),
        "IncludeManagementEvents": (boolean, False),
        "ReadWriteType": (str, False),
    }


class Trail(AWSObject):
    """
    `Trail <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html>`__
    """

    resource_type = "AWS::CloudTrail::Trail"

    props: PropsDictType = {
        "AdvancedEventSelectors": ([AdvancedEventSelector], False),
        "CloudWatchLogsLogGroupArn": (str, False),
        "CloudWatchLogsRoleArn": (str, False),
        "EnableLogFileValidation": (boolean, False),
        "EventSelectors": ([EventSelector], False),
        "IncludeGlobalServiceEvents": (boolean, False),
        "InsightSelectors": ([InsightSelector], False),
        "IsLogging": (boolean, True),
        "IsMultiRegionTrail": (boolean, False),
        "IsOrganizationTrail": (boolean, False),
        "KMSKeyId": (str, False),
        "S3BucketName": (str, True),
        "S3KeyPrefix": (str, False),
        "SnsTopicName": (str, False),
        "Tags": (Tags, False),
        "TrailName": (str, False),
    }
