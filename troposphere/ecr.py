# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean
from .validators.ecr import policytypes


class PublicRepository(AWSObject):
    """
    `PublicRepository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html>`__
    """

    resource_type = "AWS::ECR::PublicRepository"

    props: PropsDictType = {
        "RepositoryCatalogData": (dict, False),
        "RepositoryName": (str, False),
        "RepositoryPolicyText": (policytypes, False),
        "Tags": (Tags, False),
    }


class RegistryPolicy(AWSObject):
    """
    `RegistryPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html>`__
    """

    resource_type = "AWS::ECR::RegistryPolicy"

    props: PropsDictType = {
        "PolicyText": (policytypes, True),
    }


class ReplicationDestination(AWSProperty):
    """
    `ReplicationDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html>`__
    """

    props: PropsDictType = {
        "Region": (str, True),
        "RegistryId": (str, True),
    }


class RepositoryFilter(AWSProperty):
    """
    `RepositoryFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html>`__
    """

    props: PropsDictType = {
        "Filter": (str, True),
        "FilterType": (str, True),
    }


class ReplicationRule(AWSProperty):
    """
    `ReplicationRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html>`__
    """

    props: PropsDictType = {
        "Destinations": ([ReplicationDestination], True),
        "RepositoryFilters": ([RepositoryFilter], False),
    }


class ReplicationConfigurationProperty(AWSProperty):
    """
    `ReplicationConfigurationProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationconfiguration.html>`__
    """

    props: PropsDictType = {
        "Rules": ([ReplicationRule], True),
    }


class ReplicationConfiguration(AWSObject):
    """
    `ReplicationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-replicationconfiguration.html>`__
    """

    resource_type = "AWS::ECR::ReplicationConfiguration"

    props: PropsDictType = {
        "ReplicationConfigurationProperty": (ReplicationConfigurationProperty, True),
    }


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "EncryptionType": (str, True),
        "KmsKey": (str, False),
    }


class ImageScanningConfiguration(AWSProperty):
    """
    `ImageScanningConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html>`__
    """

    props: PropsDictType = {
        "ScanOnPush": (boolean, False),
    }


class LifecyclePolicy(AWSProperty):
    """
    `LifecyclePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html>`__
    """

    props: PropsDictType = {
        "LifecyclePolicyText": (str, False),
        "RegistryId": (str, False),
    }


class Repository(AWSObject):
    """
    `Repository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html>`__
    """

    resource_type = "AWS::ECR::Repository"

    props: PropsDictType = {
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "ImageScanningConfiguration": (ImageScanningConfiguration, False),
        "ImageTagMutability": (str, False),
        "LifecyclePolicy": (LifecyclePolicy, False),
        "RepositoryName": (str, False),
        "RepositoryPolicyText": (policytypes, False),
        "Tags": (Tags, False),
    }
