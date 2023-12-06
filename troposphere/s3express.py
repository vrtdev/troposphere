# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType


class BucketPolicy(AWSObject):
    """
    `BucketPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html>`__
    """

    resource_type = "AWS::S3Express::BucketPolicy"

    props: PropsDictType = {
        "Bucket": (str, True),
        "PolicyDocument": (dict, True),
    }


class DirectoryBucket(AWSObject):
    """
    `DirectoryBucket <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html>`__
    """

    resource_type = "AWS::S3Express::DirectoryBucket"

    props: PropsDictType = {
        "BucketName": (str, False),
        "DataRedundancy": (str, True),
        "LocationName": (str, True),
    }
