# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class ApiKeyRestrictions(AWSProperty):
    """
    `ApiKeyRestrictions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-apikey-apikeyrestrictions.html>`__
    """

    props: PropsDictType = {
        "AllowActions": ([str], True),
        "AllowReferers": ([str], False),
        "AllowResources": ([str], True),
    }


class APIKey(AWSObject):
    """
    `APIKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html>`__
    """

    resource_type = "AWS::Location::APIKey"

    props: PropsDictType = {
        "Description": (str, False),
        "ExpireTime": (str, False),
        "ForceDelete": (boolean, False),
        "ForceUpdate": (boolean, False),
        "KeyName": (str, True),
        "NoExpiry": (boolean, False),
        "Restrictions": (ApiKeyRestrictions, True),
        "Tags": (Tags, False),
    }


class GeofenceCollection(AWSObject):
    """
    `GeofenceCollection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html>`__
    """

    resource_type = "AWS::Location::GeofenceCollection"

    props: PropsDictType = {
        "CollectionName": (str, True),
        "Description": (str, False),
        "KmsKeyId": (str, False),
        "Tags": (Tags, False),
    }


class MapConfiguration(AWSProperty):
    """
    `MapConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html>`__
    """

    props: PropsDictType = {
        "CustomLayers": ([str], False),
        "PoliticalView": (str, False),
        "Style": (str, True),
    }


class Map(AWSObject):
    """
    `Map <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html>`__
    """

    resource_type = "AWS::Location::Map"

    props: PropsDictType = {
        "Configuration": (MapConfiguration, True),
        "Description": (str, False),
        "MapName": (str, True),
        "PricingPlan": (str, False),
        "Tags": (Tags, False),
    }


class DataSourceConfiguration(AWSProperty):
    """
    `DataSourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "IntendedUse": (str, False),
    }


class PlaceIndex(AWSObject):
    """
    `PlaceIndex <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html>`__
    """

    resource_type = "AWS::Location::PlaceIndex"

    props: PropsDictType = {
        "DataSource": (str, True),
        "DataSourceConfiguration": (DataSourceConfiguration, False),
        "Description": (str, False),
        "IndexName": (str, True),
        "PricingPlan": (str, False),
        "Tags": (Tags, False),
    }


class RouteCalculator(AWSObject):
    """
    `RouteCalculator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html>`__
    """

    resource_type = "AWS::Location::RouteCalculator"

    props: PropsDictType = {
        "CalculatorName": (str, True),
        "DataSource": (str, True),
        "Description": (str, False),
        "PricingPlan": (str, False),
        "Tags": (Tags, False),
    }


class Tracker(AWSObject):
    """
    `Tracker <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html>`__
    """

    resource_type = "AWS::Location::Tracker"

    props: PropsDictType = {
        "Description": (str, False),
        "EventBridgeEnabled": (boolean, False),
        "KmsKeyEnableGeospatialQueries": (boolean, False),
        "KmsKeyId": (str, False),
        "PositionFiltering": (str, False),
        "Tags": (Tags, False),
        "TrackerName": (str, True),
    }


class TrackerConsumer(AWSObject):
    """
    `TrackerConsumer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html>`__
    """

    resource_type = "AWS::Location::TrackerConsumer"

    props: PropsDictType = {
        "ConsumerArn": (str, True),
        "TrackerName": (str, True),
    }
