# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.opensearchservice import validate_search_service_engine_version


class MasterUserOptions(AWSProperty):
    """
    `MasterUserOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html>`__
    """

    props: PropsDictType = {
        "MasterUserARN": (str, False),
        "MasterUserName": (str, False),
        "MasterUserPassword": (str, False),
    }


class Idp(AWSProperty):
    """
    `Idp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-idp.html>`__
    """

    props: PropsDictType = {
        "EntityId": (str, True),
        "MetadataContent": (str, True),
    }


class SAMLOptions(AWSProperty):
    """
    `SAMLOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "Idp": (Idp, False),
        "MasterBackendRole": (str, False),
        "MasterUserName": (str, False),
        "RolesKey": (str, False),
        "SessionTimeoutMinutes": (integer, False),
        "SubjectKey": (str, False),
    }


class AdvancedSecurityOptionsInput(AWSProperty):
    """
    `AdvancedSecurityOptionsInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`__
    """

    props: PropsDictType = {
        "AnonymousAuthDisableDate": (str, False),
        "AnonymousAuthEnabled": (boolean, False),
        "Enabled": (boolean, False),
        "InternalUserDatabaseEnabled": (boolean, False),
        "MasterUserOptions": (MasterUserOptions, False),
        "SAMLOptions": (SAMLOptions, False),
    }


class ColdStorageOptions(AWSProperty):
    """
    `ColdStorageOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-coldstorageoptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class ZoneAwarenessConfig(AWSProperty):
    """
    `ZoneAwarenessConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html>`__
    """

    props: PropsDictType = {
        "AvailabilityZoneCount": (integer, False),
    }


class ClusterConfig(AWSProperty):
    """
    `ClusterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html>`__
    """

    props: PropsDictType = {
        "ColdStorageOptions": (ColdStorageOptions, False),
        "DedicatedMasterCount": (integer, False),
        "DedicatedMasterEnabled": (boolean, False),
        "DedicatedMasterType": (str, False),
        "InstanceCount": (integer, False),
        "InstanceType": (str, False),
        "MultiAZWithStandbyEnabled": (boolean, False),
        "WarmCount": (integer, False),
        "WarmEnabled": (boolean, False),
        "WarmType": (str, False),
        "ZoneAwarenessConfig": (ZoneAwarenessConfig, False),
        "ZoneAwarenessEnabled": (boolean, False),
    }


class CognitoOptions(AWSProperty):
    """
    `CognitoOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "IdentityPoolId": (str, False),
        "RoleArn": (str, False),
        "UserPoolId": (str, False),
    }


class DomainEndpointOptions(AWSProperty):
    """
    `DomainEndpointOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html>`__
    """

    props: PropsDictType = {
        "CustomEndpoint": (str, False),
        "CustomEndpointCertificateArn": (str, False),
        "CustomEndpointEnabled": (boolean, False),
        "EnforceHTTPS": (boolean, False),
        "TLSSecurityPolicy": (str, False),
    }


class EBSOptions(AWSProperty):
    """
    `EBSOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html>`__
    """

    props: PropsDictType = {
        "EBSEnabled": (boolean, False),
        "Iops": (integer, False),
        "Throughput": (integer, False),
        "VolumeSize": (integer, False),
        "VolumeType": (str, False),
    }


class EncryptionAtRestOptions(AWSProperty):
    """
    `EncryptionAtRestOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "KmsKeyId": (str, False),
    }


class LogPublishingOption(AWSProperty):
    """
    `LogPublishingOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogsLogGroupArn": (str, False),
        "Enabled": (boolean, False),
    }


class NodeToNodeEncryptionOptions(AWSProperty):
    """
    `NodeToNodeEncryptionOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class WindowStartTime(AWSProperty):
    """
    `WindowStartTime <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-windowstarttime.html>`__
    """

    props: PropsDictType = {
        "Hours": (integer, True),
        "Minutes": (integer, True),
    }


class OffPeakWindow(AWSProperty):
    """
    `OffPeakWindow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindow.html>`__
    """

    props: PropsDictType = {
        "WindowStartTime": (WindowStartTime, False),
    }


class OffPeakWindowOptions(AWSProperty):
    """
    `OffPeakWindowOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindowoptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "OffPeakWindow": (OffPeakWindow, False),
    }


class SnapshotOptions(AWSProperty):
    """
    `SnapshotOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html>`__
    """

    props: PropsDictType = {
        "AutomatedSnapshotStartHour": (integer, False),
    }


class SoftwareUpdateOptions(AWSProperty):
    """
    `SoftwareUpdateOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-softwareupdateoptions.html>`__
    """

    props: PropsDictType = {
        "AutoSoftwareUpdateEnabled": (boolean, False),
    }


class VPCOptions(AWSProperty):
    """
    `VPCOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
    }


class Domain(AWSObject):
    """
    `Domain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`__
    """

    resource_type = "AWS::OpenSearchService::Domain"

    props: PropsDictType = {
        "AccessPolicies": (dict, False),
        "AdvancedOptions": (dict, False),
        "AdvancedSecurityOptions": (AdvancedSecurityOptionsInput, False),
        "ClusterConfig": (ClusterConfig, False),
        "CognitoOptions": (CognitoOptions, False),
        "DomainEndpointOptions": (DomainEndpointOptions, False),
        "DomainName": (str, False),
        "EBSOptions": (EBSOptions, False),
        "EncryptionAtRestOptions": (EncryptionAtRestOptions, False),
        "EngineVersion": (validate_search_service_engine_version, False),
        "IPAddressType": (str, False),
        "LogPublishingOptions": (dict, False),
        "NodeToNodeEncryptionOptions": (NodeToNodeEncryptionOptions, False),
        "OffPeakWindowOptions": (OffPeakWindowOptions, False),
        "SnapshotOptions": (SnapshotOptions, False),
        "SoftwareUpdateOptions": (SoftwareUpdateOptions, False),
        "Tags": (Tags, False),
        "VPCOptions": (VPCOptions, False),
    }


class ServiceSoftwareOptions(AWSProperty):
    """
    `ServiceSoftwareOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html>`__
    """

    props: PropsDictType = {
        "AutomatedUpdateDate": (str, False),
        "Cancellable": (boolean, False),
        "CurrentVersion": (str, False),
        "Description": (str, False),
        "NewVersion": (str, False),
        "OptionalDeployment": (boolean, False),
        "UpdateAvailable": (boolean, False),
        "UpdateStatus": (str, False),
    }
