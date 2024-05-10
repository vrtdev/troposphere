# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags
from .validators import integer


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html>`__
    """

    resource_type = "AWS::DocDBElastic::Cluster"

    props: PropsDictType = {
        "AdminUserName": (str, True),
        "AdminUserPassword": (str, False),
        "AuthType": (str, True),
        "BackupRetentionPeriod": (integer, False),
        "ClusterName": (str, True),
        "KmsKeyId": (str, False),
        "PreferredBackupWindow": (str, False),
        "PreferredMaintenanceWindow": (str, False),
        "ShardCapacity": (integer, True),
        "ShardCount": (integer, True),
        "ShardInstanceCount": (integer, False),
        "SubnetIds": ([str], False),
        "Tags": (Tags, False),
        "VpcSecurityGroupIds": ([str], False),
    }
