# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class LogConfigurationForChannel(AWSProperty):
    """
    `LogConfigurationForChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-logconfigurationforchannel.html>`__
    """

    props: PropsDictType = {
        "LogTypes": ([str], False),
    }


class DashPlaylistSettings(AWSProperty):
    """
    `DashPlaylistSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html>`__
    """

    props: PropsDictType = {
        "ManifestWindowSeconds": (double, False),
        "MinBufferTimeSeconds": (double, False),
        "MinUpdatePeriodSeconds": (double, False),
        "SuggestedPresentationDelaySeconds": (double, False),
    }


class HlsPlaylistSettings(AWSProperty):
    """
    `HlsPlaylistSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-hlsplaylistsettings.html>`__
    """

    props: PropsDictType = {
        "AdMarkupType": ([str], False),
        "ManifestWindowSeconds": (double, False),
    }


class RequestOutputItem(AWSProperty):
    """
    `RequestOutputItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html>`__
    """

    props: PropsDictType = {
        "DashPlaylistSettings": (DashPlaylistSettings, False),
        "HlsPlaylistSettings": (HlsPlaylistSettings, False),
        "ManifestName": (str, True),
        "SourceGroup": (str, True),
    }


class SlateSource(AWSProperty):
    """
    `SlateSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-slatesource.html>`__
    """

    props: PropsDictType = {
        "SourceLocationName": (str, False),
        "VodSourceName": (str, False),
    }


class TimeShiftConfiguration(AWSProperty):
    """
    `TimeShiftConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-timeshiftconfiguration.html>`__
    """

    props: PropsDictType = {
        "MaxTimeDelaySeconds": (double, True),
    }


class Channel(AWSObject):
    """
    `Channel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html>`__
    """

    resource_type = "AWS::MediaTailor::Channel"

    props: PropsDictType = {
        "Audiences": ([str], False),
        "ChannelName": (str, True),
        "FillerSlate": (SlateSource, False),
        "LogConfiguration": (LogConfigurationForChannel, False),
        "Outputs": ([RequestOutputItem], True),
        "PlaybackMode": (str, True),
        "Tags": (Tags, False),
        "Tier": (str, False),
        "TimeShiftConfiguration": (TimeShiftConfiguration, False),
    }


class ChannelPolicy(AWSObject):
    """
    `ChannelPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html>`__
    """

    resource_type = "AWS::MediaTailor::ChannelPolicy"

    props: PropsDictType = {
        "ChannelName": (str, True),
        "Policy": (dict, True),
    }


class HttpPackageConfiguration(AWSProperty):
    """
    `HttpPackageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html>`__
    """

    props: PropsDictType = {
        "Path": (str, True),
        "SourceGroup": (str, True),
        "Type": (str, True),
    }


class LiveSource(AWSObject):
    """
    `LiveSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html>`__
    """

    resource_type = "AWS::MediaTailor::LiveSource"

    props: PropsDictType = {
        "HttpPackageConfigurations": ([HttpPackageConfiguration], True),
        "LiveSourceName": (str, True),
        "SourceLocationName": (str, True),
        "Tags": (Tags, False),
    }


class AvailSuppression(AWSProperty):
    """
    `AvailSuppression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html>`__
    """

    props: PropsDictType = {
        "Mode": (str, False),
        "Value": (str, False),
    }


class Bumper(AWSProperty):
    """
    `Bumper <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html>`__
    """

    props: PropsDictType = {
        "EndUrl": (str, False),
        "StartUrl": (str, False),
    }


class CdnConfiguration(AWSProperty):
    """
    `CdnConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdSegmentUrlPrefix": (str, False),
        "ContentSegmentUrlPrefix": (str, False),
    }


class DashConfiguration(AWSProperty):
    """
    `DashConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html>`__
    """

    props: PropsDictType = {
        "ManifestEndpointPrefix": (str, False),
        "MpdLocation": (str, False),
        "OriginManifestType": (str, False),
    }


class HlsConfiguration(AWSProperty):
    """
    `HlsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html>`__
    """

    props: PropsDictType = {
        "ManifestEndpointPrefix": (str, False),
    }


class LivePreRollConfiguration(AWSProperty):
    """
    `LivePreRollConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdDecisionServerUrl": (str, False),
        "MaxDurationSeconds": (integer, False),
    }


class AdMarkerPassthrough(AWSProperty):
    """
    `AdMarkerPassthrough <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class ManifestProcessingRules(AWSProperty):
    """
    `ManifestProcessingRules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html>`__
    """

    props: PropsDictType = {
        "AdMarkerPassthrough": (AdMarkerPassthrough, False),
    }


class PlaybackConfiguration(AWSObject):
    """
    `PlaybackConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html>`__
    """

    resource_type = "AWS::MediaTailor::PlaybackConfiguration"

    props: PropsDictType = {
        "AdDecisionServerUrl": (str, True),
        "AvailSuppression": (AvailSuppression, False),
        "Bumper": (Bumper, False),
        "CdnConfiguration": (CdnConfiguration, False),
        "ConfigurationAliases": (dict, False),
        "DashConfiguration": (DashConfiguration, False),
        "HlsConfiguration": (HlsConfiguration, False),
        "LivePreRollConfiguration": (LivePreRollConfiguration, False),
        "ManifestProcessingRules": (ManifestProcessingRules, False),
        "Name": (str, True),
        "PersonalizationThresholdSeconds": (integer, False),
        "SlateAdUrl": (str, False),
        "Tags": (Tags, False),
        "TranscodeProfileName": (str, False),
        "VideoContentSourceUrl": (str, True),
    }


class SecretsManagerAccessTokenConfiguration(AWSProperty):
    """
    `SecretsManagerAccessTokenConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html>`__
    """

    props: PropsDictType = {
        "HeaderName": (str, False),
        "SecretArn": (str, False),
        "SecretStringKey": (str, False),
    }


class AccessConfiguration(AWSProperty):
    """
    `AccessConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-accessconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccessType": (str, False),
        "SecretsManagerAccessTokenConfiguration": (
            SecretsManagerAccessTokenConfiguration,
            False,
        ),
    }


class DefaultSegmentDeliveryConfiguration(AWSProperty):
    """
    `DefaultSegmentDeliveryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration.html>`__
    """

    props: PropsDictType = {
        "BaseUrl": (str, False),
    }


class HttpConfiguration(AWSProperty):
    """
    `HttpConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-httpconfiguration.html>`__
    """

    props: PropsDictType = {
        "BaseUrl": (str, True),
    }


class SegmentDeliveryConfiguration(AWSProperty):
    """
    `SegmentDeliveryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html>`__
    """

    props: PropsDictType = {
        "BaseUrl": (str, False),
        "Name": (str, False),
    }


class SourceLocation(AWSObject):
    """
    `SourceLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html>`__
    """

    resource_type = "AWS::MediaTailor::SourceLocation"

    props: PropsDictType = {
        "AccessConfiguration": (AccessConfiguration, False),
        "DefaultSegmentDeliveryConfiguration": (
            DefaultSegmentDeliveryConfiguration,
            False,
        ),
        "HttpConfiguration": (HttpConfiguration, True),
        "SegmentDeliveryConfigurations": ([SegmentDeliveryConfiguration], False),
        "SourceLocationName": (str, True),
        "Tags": (Tags, False),
    }


class VodSource(AWSObject):
    """
    `VodSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html>`__
    """

    resource_type = "AWS::MediaTailor::VodSource"

    props: PropsDictType = {
        "HttpPackageConfigurations": ([HttpPackageConfiguration], True),
        "SourceLocationName": (str, True),
        "Tags": (Tags, False),
        "VodSourceName": (str, True),
    }
