# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean
from .validators.sns import policytypes


class SubscriptionResource(AWSObject):
    """
    `SubscriptionResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html>`__
    """

    resource_type = "AWS::SNS::Subscription"

    props: PropsDictType = {
        "DeliveryPolicy": (dict, False),
        "Endpoint": (str, False),
        "FilterPolicy": (dict, False),
        "FilterPolicyScope": (str, False),
        "Protocol": (str, True),
        "RawMessageDelivery": (boolean, False),
        "RedrivePolicy": (dict, False),
        "Region": (str, False),
        "ReplayPolicy": (dict, False),
        "SubscriptionRoleArn": (str, False),
        "TopicArn": (str, True),
    }


class LoggingConfig(AWSProperty):
    """
    `LoggingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html>`__
    """

    props: PropsDictType = {
        "FailureFeedbackRoleArn": (str, False),
        "Protocol": (str, True),
        "SuccessFeedbackRoleArn": (str, False),
        "SuccessFeedbackSampleRate": (str, False),
    }


class Subscription(AWSProperty):
    """
    `Subscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-subscription.html>`__
    """

    props: PropsDictType = {
        "Endpoint": (str, True),
        "Protocol": (str, True),
    }


class Topic(AWSObject):
    """
    `Topic <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html>`__
    """

    resource_type = "AWS::SNS::Topic"

    props: PropsDictType = {
        "ArchivePolicy": (dict, False),
        "ContentBasedDeduplication": (boolean, False),
        "DataProtectionPolicy": (dict, False),
        "DeliveryStatusLogging": ([LoggingConfig], False),
        "DisplayName": (str, False),
        "FifoTopic": (boolean, False),
        "KmsMasterKeyId": (str, False),
        "SignatureVersion": (str, False),
        "Subscription": ([Subscription], False),
        "Tags": (Tags, False),
        "TopicName": (str, False),
        "TracingConfig": (str, False),
    }


class TopicInlinePolicy(AWSObject):
    """
    `TopicInlinePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html>`__
    """

    resource_type = "AWS::SNS::TopicInlinePolicy"

    props: PropsDictType = {
        "PolicyDocument": (dict, True),
        "TopicArn": (str, True),
    }


class TopicPolicy(AWSObject):
    """
    `TopicPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html>`__
    """

    resource_type = "AWS::SNS::TopicPolicy"

    props: PropsDictType = {
        "PolicyDocument": (policytypes, True),
        "Topics": ([str], True),
    }
