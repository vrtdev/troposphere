# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import integer


class Agent(AWSObject):
    """
    `Agent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html>`__
    """

    resource_type = "AWS::DataSync::Agent"

    props: PropsDictType = {
        "ActivationKey": (str, False),
        "AgentName": (str, False),
        "SecurityGroupArns": ([str], False),
        "SubnetArns": ([str], False),
        "Tags": (Tags, False),
        "VpcEndpointId": (str, False),
    }


class AzureBlobSasConfiguration(AWSProperty):
    """
    `AzureBlobSasConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationazureblob-azureblobsasconfiguration.html>`__
    """

    props: PropsDictType = {
        "AzureBlobSasToken": (str, True),
    }


class LocationAzureBlob(AWSObject):
    """
    `LocationAzureBlob <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html>`__
    """

    resource_type = "AWS::DataSync::LocationAzureBlob"

    props: PropsDictType = {
        "AgentArns": ([str], True),
        "AzureAccessTier": (str, False),
        "AzureBlobAuthenticationType": (str, True),
        "AzureBlobContainerUrl": (str, False),
        "AzureBlobSasConfiguration": (AzureBlobSasConfiguration, False),
        "AzureBlobType": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class Ec2Config(AWSProperty):
    """
    `Ec2Config <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupArns": ([str], True),
        "SubnetArn": (str, True),
    }


class LocationEFS(AWSObject):
    """
    `LocationEFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html>`__
    """

    resource_type = "AWS::DataSync::LocationEFS"

    props: PropsDictType = {
        "AccessPointArn": (str, False),
        "Ec2Config": (Ec2Config, True),
        "EfsFilesystemArn": (str, False),
        "FileSystemAccessRoleArn": (str, False),
        "InTransitEncryption": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class LocationFSxLustre(AWSObject):
    """
    `LocationFSxLustre <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html>`__
    """

    resource_type = "AWS::DataSync::LocationFSxLustre"

    props: PropsDictType = {
        "FsxFilesystemArn": (str, False),
        "SecurityGroupArns": ([str], True),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class MountOptions(AWSProperty):
    """
    `MountOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html>`__
    """

    props: PropsDictType = {
        "Version": (str, False),
    }


class NFS(AWSProperty):
    """
    `NFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-nfs.html>`__
    """

    props: PropsDictType = {
        "MountOptions": (MountOptions, True),
    }


class SmbMountOptions(AWSProperty):
    """
    `SmbMountOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smbmountoptions.html>`__
    """

    props: PropsDictType = {
        "Version": (str, False),
    }


class SMB(AWSProperty):
    """
    `SMB <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html>`__
    """

    props: PropsDictType = {
        "Domain": (str, False),
        "MountOptions": (SmbMountOptions, True),
        "Password": (str, True),
        "User": (str, True),
    }


class ONTAPProtocol(AWSProperty):
    """
    `ONTAPProtocol <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html>`__
    """

    props: PropsDictType = {
        "NFS": (NFS, False),
        "SMB": (SMB, False),
    }


class LocationFSxONTAP(AWSObject):
    """
    `LocationFSxONTAP <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html>`__
    """

    resource_type = "AWS::DataSync::LocationFSxONTAP"

    props: PropsDictType = {
        "Protocol": (ONTAPProtocol, False),
        "SecurityGroupArns": ([str], True),
        "StorageVirtualMachineArn": (str, True),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class Protocol(AWSProperty):
    """
    `Protocol <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-protocol.html>`__
    """

    props: PropsDictType = {
        "NFS": (NFS, False),
    }


class LocationFSxOpenZFS(AWSObject):
    """
    `LocationFSxOpenZFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html>`__
    """

    resource_type = "AWS::DataSync::LocationFSxOpenZFS"

    props: PropsDictType = {
        "FsxFilesystemArn": (str, False),
        "Protocol": (Protocol, True),
        "SecurityGroupArns": ([str], True),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class LocationFSxWindows(AWSObject):
    """
    `LocationFSxWindows <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html>`__
    """

    resource_type = "AWS::DataSync::LocationFSxWindows"

    props: PropsDictType = {
        "Domain": (str, False),
        "FsxFilesystemArn": (str, False),
        "Password": (str, False),
        "SecurityGroupArns": ([str], True),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
        "User": (str, True),
    }


class NameNode(AWSProperty):
    """
    `NameNode <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html>`__
    """

    props: PropsDictType = {
        "Hostname": (str, True),
        "Port": (integer, True),
    }


class QopConfiguration(AWSProperty):
    """
    `QopConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html>`__
    """

    props: PropsDictType = {
        "DataTransferProtection": (str, False),
        "RpcProtection": (str, False),
    }


class LocationHDFS(AWSObject):
    """
    `LocationHDFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html>`__
    """

    resource_type = "AWS::DataSync::LocationHDFS"

    props: PropsDictType = {
        "AgentArns": ([str], True),
        "AuthenticationType": (str, True),
        "BlockSize": (integer, False),
        "KerberosKeytab": (str, False),
        "KerberosKrb5Conf": (str, False),
        "KerberosPrincipal": (str, False),
        "KmsKeyProviderUri": (str, False),
        "NameNodes": ([NameNode], True),
        "QopConfiguration": (QopConfiguration, False),
        "ReplicationFactor": (integer, False),
        "SimpleUser": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class OnPremConfig(AWSProperty):
    """
    `OnPremConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html>`__
    """

    props: PropsDictType = {
        "AgentArns": ([str], True),
    }


class LocationNFS(AWSObject):
    """
    `LocationNFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html>`__
    """

    resource_type = "AWS::DataSync::LocationNFS"

    props: PropsDictType = {
        "MountOptions": (MountOptions, False),
        "OnPremConfig": (OnPremConfig, True),
        "ServerHostname": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class LocationObjectStorage(AWSObject):
    """
    `LocationObjectStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html>`__
    """

    resource_type = "AWS::DataSync::LocationObjectStorage"

    props: PropsDictType = {
        "AccessKey": (str, False),
        "AgentArns": ([str], True),
        "BucketName": (str, False),
        "SecretKey": (str, False),
        "ServerCertificate": (str, False),
        "ServerHostname": (str, False),
        "ServerPort": (integer, False),
        "ServerProtocol": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class S3Config(AWSProperty):
    """
    `S3Config <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html>`__
    """

    props: PropsDictType = {
        "BucketAccessRoleArn": (str, True),
    }


class LocationS3(AWSObject):
    """
    `LocationS3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html>`__
    """

    resource_type = "AWS::DataSync::LocationS3"

    props: PropsDictType = {
        "S3BucketArn": (str, False),
        "S3Config": (S3Config, True),
        "S3StorageClass": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class LocationSMB(AWSObject):
    """
    `LocationSMB <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html>`__
    """

    resource_type = "AWS::DataSync::LocationSMB"

    props: PropsDictType = {
        "AgentArns": ([str], True),
        "Domain": (str, False),
        "MountOptions": (MountOptions, False),
        "Password": (str, False),
        "ServerHostname": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
        "User": (str, True),
    }


class ServerConfiguration(AWSProperty):
    """
    `ServerConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-serverconfiguration.html>`__
    """

    props: PropsDictType = {
        "ServerHostname": (str, True),
        "ServerPort": (integer, False),
    }


class ServerCredentials(AWSProperty):
    """
    `ServerCredentials <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-servercredentials.html>`__
    """

    props: PropsDictType = {
        "Password": (str, True),
        "Username": (str, True),
    }


class StorageSystem(AWSObject):
    """
    `StorageSystem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html>`__
    """

    resource_type = "AWS::DataSync::StorageSystem"

    props: PropsDictType = {
        "AgentArns": ([str], True),
        "CloudWatchLogGroupArn": (str, False),
        "Name": (str, False),
        "ServerConfiguration": (ServerConfiguration, True),
        "ServerCredentials": (ServerCredentials, False),
        "SystemType": (str, True),
        "Tags": (Tags, False),
    }


class FilterRule(AWSProperty):
    """
    `FilterRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html>`__
    """

    props: PropsDictType = {
        "FilterType": (str, False),
        "Value": (str, False),
    }


class ManifestConfigSourceS3(AWSProperty):
    """
    `ManifestConfigSourceS3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfigsources3.html>`__
    """

    props: PropsDictType = {
        "BucketAccessRoleArn": (str, False),
        "ManifestObjectPath": (str, False),
        "ManifestObjectVersionId": (str, False),
        "S3BucketArn": (str, False),
    }


class Source(AWSProperty):
    """
    `Source <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-source.html>`__
    """

    props: PropsDictType = {
        "S3": (ManifestConfigSourceS3, False),
    }


class ManifestConfig(AWSProperty):
    """
    `ManifestConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfig.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
        "Format": (str, False),
        "Source": (Source, True),
    }


class Options(AWSProperty):
    """
    `Options <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html>`__
    """

    props: PropsDictType = {
        "Atime": (str, False),
        "BytesPerSecond": (integer, False),
        "Gid": (str, False),
        "LogLevel": (str, False),
        "Mtime": (str, False),
        "ObjectTags": (str, False),
        "OverwriteMode": (str, False),
        "PosixPermissions": (str, False),
        "PreserveDeletedFiles": (str, False),
        "PreserveDevices": (str, False),
        "SecurityDescriptorCopyFlags": (str, False),
        "TaskQueueing": (str, False),
        "TransferMode": (str, False),
        "Uid": (str, False),
        "VerifyMode": (str, False),
    }


class TaskReportConfigDestinationS3(AWSProperty):
    """
    `TaskReportConfigDestinationS3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfigdestinations3.html>`__
    """

    props: PropsDictType = {
        "BucketAccessRoleArn": (str, False),
        "S3BucketArn": (str, False),
        "Subdirectory": (str, False),
    }


class Destination(AWSProperty):
    """
    `Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-destination.html>`__
    """

    props: PropsDictType = {
        "S3": (TaskReportConfigDestinationS3, False),
    }


class Deleted(AWSProperty):
    """
    `Deleted <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-deleted.html>`__
    """

    props: PropsDictType = {
        "ReportLevel": (str, False),
    }


class Skipped(AWSProperty):
    """
    `Skipped <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-skipped.html>`__
    """

    props: PropsDictType = {
        "ReportLevel": (str, False),
    }


class Transferred(AWSProperty):
    """
    `Transferred <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-transferred.html>`__
    """

    props: PropsDictType = {
        "ReportLevel": (str, False),
    }


class Verified(AWSProperty):
    """
    `Verified <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-verified.html>`__
    """

    props: PropsDictType = {
        "ReportLevel": (str, False),
    }


class Overrides(AWSProperty):
    """
    `Overrides <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html>`__
    """

    props: PropsDictType = {
        "Deleted": (Deleted, False),
        "Skipped": (Skipped, False),
        "Transferred": (Transferred, False),
        "Verified": (Verified, False),
    }


class TaskReportConfig(AWSProperty):
    """
    `TaskReportConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html>`__
    """

    props: PropsDictType = {
        "Destination": (Destination, True),
        "ObjectVersionIds": (str, False),
        "OutputType": (str, True),
        "Overrides": (Overrides, False),
        "ReportLevel": (str, False),
    }


class TaskSchedule(AWSProperty):
    """
    `TaskSchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html>`__
    """

    props: PropsDictType = {
        "ScheduleExpression": (str, False),
        "Status": (str, False),
    }


class Task(AWSObject):
    """
    `Task <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html>`__
    """

    resource_type = "AWS::DataSync::Task"

    props: PropsDictType = {
        "CloudWatchLogGroupArn": (str, False),
        "DestinationLocationArn": (str, True),
        "Excludes": ([FilterRule], False),
        "Includes": ([FilterRule], False),
        "ManifestConfig": (ManifestConfig, False),
        "Name": (str, False),
        "Options": (Options, False),
        "Schedule": (TaskSchedule, False),
        "SourceLocationArn": (str, True),
        "Tags": (Tags, False),
        "TaskReportConfig": (TaskReportConfig, False),
    }


class NfsMountOptions(AWSProperty):
    """
    `NfsMountOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfsmountoptions.html>`__
    """

    props: PropsDictType = {
        "Version": (str, False),
    }
