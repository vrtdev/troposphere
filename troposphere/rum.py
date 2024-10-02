# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double


class MetricDefinition(AWSProperty):
    """
    `MetricDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html>`__
    """

    props: PropsDictType = {
        "DimensionKeys": (dict, False),
        "EventPattern": (str, False),
        "Name": (str, True),
        "Namespace": (str, False),
        "UnitLabel": (str, False),
        "ValueKey": (str, False),
    }


class MetricDestination(AWSProperty):
    """
    `MetricDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html>`__
    """

    props: PropsDictType = {
        "Destination": (str, True),
        "DestinationArn": (str, False),
        "IamRoleArn": (str, False),
        "MetricDefinitions": ([MetricDefinition], False),
    }


class AppMonitorConfiguration(AWSProperty):
    """
    `AppMonitorConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html>`__
    """

    props: PropsDictType = {
        "AllowCookies": (boolean, False),
        "EnableXRay": (boolean, False),
        "ExcludedPages": ([str], False),
        "FavoritePages": ([str], False),
        "GuestRoleArn": (str, False),
        "IdentityPoolId": (str, False),
        "IncludedPages": ([str], False),
        "MetricDestinations": ([MetricDestination], False),
        "SessionSampleRate": (double, False),
        "Telemetries": ([str], False),
    }


class CustomEvents(AWSProperty):
    """
    `CustomEvents <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-customevents.html>`__
    """

    props: PropsDictType = {
        "Status": (str, False),
    }


class AppMonitor(AWSObject):
    """
    `AppMonitor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html>`__
    """

    resource_type = "AWS::RUM::AppMonitor"

    props: PropsDictType = {
        "AppMonitorConfiguration": (AppMonitorConfiguration, False),
        "CustomEvents": (CustomEvents, False),
        "CwLogEnabled": (boolean, False),
        "Domain": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
