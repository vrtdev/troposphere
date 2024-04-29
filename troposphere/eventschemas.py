# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags
from .validators import boolean


class Discoverer(AWSObject):
    """
    `Discoverer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html>`__
    """

    resource_type = "AWS::EventSchemas::Discoverer"

    props: PropsDictType = {
        "CrossAccount": (boolean, False),
        "Description": (str, False),
        "SourceArn": (str, True),
        "Tags": (Tags, False),
    }


class Registry(AWSObject):
    """
    `Registry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html>`__
    """

    resource_type = "AWS::EventSchemas::Registry"

    props: PropsDictType = {
        "Description": (str, False),
        "RegistryName": (str, False),
        "Tags": (Tags, False),
    }


class RegistryPolicy(AWSObject):
    """
    `RegistryPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html>`__
    """

    resource_type = "AWS::EventSchemas::RegistryPolicy"

    props: PropsDictType = {
        "Policy": (dict, True),
        "RegistryName": (str, True),
        "RevisionId": (str, False),
    }


class Schema(AWSObject):
    """
    `Schema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html>`__
    """

    resource_type = "AWS::EventSchemas::Schema"

    props: PropsDictType = {
        "Content": (str, True),
        "Description": (str, False),
        "RegistryName": (str, True),
        "SchemaName": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }
