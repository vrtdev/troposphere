# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags


class Connection(AWSObject):
    """
    `Connection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.html>`__
    """

    resource_type = "AWS::CodeConnections::Connection"

    props: PropsDictType = {
        "ConnectionName": (str, True),
        "HostArn": (str, False),
        "ProviderType": (str, False),
        "Tags": (Tags, False),
    }
