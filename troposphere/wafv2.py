# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.wafv2 import (
    validate_comparison_operator,
    validate_custom_response_bodies,
    validate_ipaddress_version,
    validate_positional_constraint,
    validate_transformation_type,
    wafv2_custom_body_response_content,
    wafv2_custom_body_response_content_type,
)


class IPSet(AWSObject):
    """
    `IPSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html>`__
    """

    resource_type = "AWS::WAFv2::IPSet"

    props: PropsDictType = {
        "Addresses": ([str], True),
        "Description": (str, False),
        "IPAddressVersion": (validate_ipaddress_version, True),
        "Name": (str, False),
        "Scope": (str, True),
        "Tags": (Tags, False),
    }


class LoggingConfigurationFieldToMatch(AWSProperty):
    """
    `LoggingConfigurationFieldToMatch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html>`__
    """

    props: PropsDictType = {
        "JsonBody": (dict, False),
        "Method": (dict, False),
        "QueryString": (dict, False),
        "SingleHeader": (dict, False),
        "UriPath": (dict, False),
    }


class LoggingConfiguration(AWSObject):
    """
    `LoggingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html>`__
    """

    resource_type = "AWS::WAFv2::LoggingConfiguration"

    props: PropsDictType = {
        "LogDestinationConfigs": ([str], True),
        "LoggingFilter": (dict, False),
        "RedactedFields": ([LoggingConfigurationFieldToMatch], False),
        "ResourceArn": (str, True),
    }


class RegexPatternSet(AWSObject):
    """
    `RegexPatternSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html>`__
    """

    resource_type = "AWS::WAFv2::RegexPatternSet"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, False),
        "RegularExpressionList": ([str], True),
        "Scope": (str, True),
        "Tags": (Tags, False),
    }


class CustomResponseBody(AWSProperty):
    """
    `CustomResponseBody <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html>`__
    """

    props: PropsDictType = {
        "Content": (wafv2_custom_body_response_content, True),
        "ContentType": (wafv2_custom_body_response_content_type, True),
    }


class ImmunityTimeProperty(AWSProperty):
    """
    `ImmunityTimeProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-immunitytimeproperty.html>`__
    """

    props: PropsDictType = {
        "ImmunityTime": (integer, True),
    }


class CaptchaConfig(AWSProperty):
    """
    `CaptchaConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaconfig.html>`__
    """

    props: PropsDictType = {
        "ImmunityTimeProperty": (ImmunityTimeProperty, False),
    }


class Label(AWSProperty):
    """
    `Label <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class CustomHTTPHeader(AWSProperty):
    """
    `CustomHTTPHeader <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class CustomRequestHandling(AWSProperty):
    """
    `CustomRequestHandling <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html>`__
    """

    props: PropsDictType = {
        "InsertHeaders": ([CustomHTTPHeader], True),
    }


class AllowAction(AWSProperty):
    """
    `AllowAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html>`__
    """

    props: PropsDictType = {
        "CustomRequestHandling": (CustomRequestHandling, False),
    }


class CustomResponse(AWSProperty):
    """
    `CustomResponse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html>`__
    """

    props: PropsDictType = {
        "CustomResponseBodyKey": (str, False),
        "ResponseCode": (integer, True),
        "ResponseHeaders": ([CustomHTTPHeader], False),
    }


class BlockAction(AWSProperty):
    """
    `BlockAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html>`__
    """

    props: PropsDictType = {
        "CustomResponse": (CustomResponse, False),
    }


class CaptchaAction(AWSProperty):
    """
    `CaptchaAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaaction.html>`__
    """

    props: PropsDictType = {
        "CustomRequestHandling": (CustomRequestHandling, False),
    }


class CountAction(AWSProperty):
    """
    `CountAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html>`__
    """

    props: PropsDictType = {
        "CustomRequestHandling": (CustomRequestHandling, False),
    }


class RuleAction(AWSProperty):
    """
    `RuleAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html>`__
    """

    props: PropsDictType = {
        "Allow": (AllowAction, False),
        "Block": (BlockAction, False),
        "Captcha": (CaptchaAction, False),
        "Count": (CountAction, False),
    }


class JsonMatchPattern(AWSProperty):
    """
    `JsonMatchPattern <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html>`__
    """

    props: PropsDictType = {
        "All": (dict, False),
        "IncludedPaths": ([str], False),
    }


class JsonBody(AWSProperty):
    """
    `JsonBody <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html>`__
    """

    props: PropsDictType = {
        "InvalidFallbackBehavior": (str, False),
        "MatchPattern": (JsonMatchPattern, True),
        "MatchScope": (str, True),
    }


class FieldToMatch(AWSProperty):
    """
    `FieldToMatch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html>`__
    """

    props: PropsDictType = {
        "AllQueryArguments": (dict, False),
        "Body": (dict, False),
        "JsonBody": (JsonBody, False),
        "Method": (dict, False),
        "QueryString": (dict, False),
        "SingleHeader": (dict, False),
        "SingleQueryArgument": (dict, False),
        "UriPath": (dict, False),
    }


class TextTransformation(AWSProperty):
    """
    `TextTransformation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html>`__
    """

    props: PropsDictType = {
        "Priority": (integer, True),
        "Type": (validate_transformation_type, True),
    }


class ByteMatchStatement(AWSProperty):
    """
    `ByteMatchStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "PositionalConstraint": (validate_positional_constraint, True),
        "SearchString": (str, False),
        "SearchStringBase64": (str, False),
        "TextTransformations": ([TextTransformation], True),
    }


class ForwardedIPConfiguration(AWSProperty):
    """
    `ForwardedIPConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html>`__
    """

    props: PropsDictType = {
        "FallbackBehavior": (str, True),
        "HeaderName": (str, True),
    }


class GeoMatchStatement(AWSProperty):
    """
    `GeoMatchStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html>`__
    """

    props: PropsDictType = {
        "CountryCodes": ([str], False),
        "ForwardedIPConfig": (ForwardedIPConfiguration, False),
    }


class IPSetForwardedIPConfiguration(AWSProperty):
    """
    `IPSetForwardedIPConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html>`__
    """

    props: PropsDictType = {
        "FallbackBehavior": (str, True),
        "HeaderName": (str, True),
        "Position": (str, True),
    }


class IPSetReferenceStatement(AWSProperty):
    """
    `IPSetReferenceStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "IPSetForwardedIPConfig": (IPSetForwardedIPConfiguration, False),
    }


class LabelMatchStatement(AWSProperty):
    """
    `LabelMatchStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Scope": (str, True),
    }


class ExcludedRule(AWSProperty):
    """
    `ExcludedRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class ManagedRuleGroupStatement(AWSProperty):
    """
    `ManagedRuleGroupStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html>`__
    """

    props: PropsDictType = {
        "ExcludedRules": ([ExcludedRule], False),
        "Name": (str, True),
        "VendorName": (str, True),
        "Version": (str, False),
    }


class RegexMatchStatement(AWSProperty):
    """
    `RegexMatchStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "RegexString": (str, True),
        "TextTransformations": ([TextTransformation], True),
    }


class RegexPatternSetReferenceStatement(AWSProperty):
    """
    `RegexPatternSetReferenceStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "FieldToMatch": (FieldToMatch, True),
        "TextTransformations": ([TextTransformation], True),
    }


class RuleGroupReferenceStatement(AWSProperty):
    """
    `RuleGroupReferenceStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "ExcludedRules": ([ExcludedRule], False),
    }


class SizeConstraintStatement(AWSProperty):
    """
    `SizeConstraintStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (validate_comparison_operator, True),
        "FieldToMatch": (FieldToMatch, True),
        "Size": (double, True),
        "TextTransformations": ([TextTransformation], True),
    }


class SqliMatchStatement(AWSProperty):
    """
    `SqliMatchStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "TextTransformations": ([TextTransformation], True),
    }


class XssMatchStatement(AWSProperty):
    """
    `XssMatchStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "TextTransformations": ([TextTransformation], True),
    }


class StatementThree(AWSProperty):
    """
    `StatementThree <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html>`__
    """

    props: PropsDictType = {
        "ByteMatchStatement": (ByteMatchStatement, False),
        "GeoMatchStatement": (GeoMatchStatement, False),
        "IPSetReferenceStatement": (IPSetReferenceStatement, False),
        "LabelMatchStatement": (LabelMatchStatement, False),
        "ManagedRuleGroupStatement": (ManagedRuleGroupStatement, False),
        "RegexMatchStatement": (RegexMatchStatement, False),
        "RegexPatternSetReferenceStatement": (RegexPatternSetReferenceStatement, False),
        "RuleGroupReferenceStatement": (RuleGroupReferenceStatement, False),
        "SizeConstraintStatement": (SizeConstraintStatement, False),
        "SqliMatchStatement": (SqliMatchStatement, False),
        "XssMatchStatement": (XssMatchStatement, False),
    }


class AndStatementTwo(AWSProperty):
    """
    `AndStatementTwo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html>`__
    """

    props: PropsDictType = {
        "Statements": ([StatementThree], True),
    }


class NotStatementTwo(AWSProperty):
    """
    `NotStatementTwo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html>`__
    """

    props: PropsDictType = {
        "Statement": (StatementThree, True),
    }


class OrStatementTwo(AWSProperty):
    """
    `OrStatementTwo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html>`__
    """

    props: PropsDictType = {
        "Statements": ([StatementThree], True),
    }


class RateBasedStatementTwo(AWSProperty):
    """
    `RateBasedStatementTwo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html>`__
    """

    props: PropsDictType = {
        "AggregateKeyType": (str, True),
        "ForwardedIPConfig": (ForwardedIPConfiguration, False),
        "Limit": (integer, True),
        "ScopeDownStatement": (StatementThree, False),
    }


class StatementTwo(AWSProperty):
    """
    `StatementTwo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html>`__
    """

    props: PropsDictType = {
        "AndStatement": (AndStatementTwo, False),
        "ByteMatchStatement": (ByteMatchStatement, False),
        "GeoMatchStatement": (GeoMatchStatement, False),
        "IPSetReferenceStatement": (IPSetReferenceStatement, False),
        "LabelMatchStatement": (LabelMatchStatement, False),
        "ManagedRuleGroupStatement": (ManagedRuleGroupStatement, False),
        "NotStatement": (NotStatementTwo, False),
        "OrStatement": (OrStatementTwo, False),
        "RateBasedStatement": (RateBasedStatementTwo, False),
        "RegexMatchStatement": (RegexMatchStatement, False),
        "RegexPatternSetReferenceStatement": (RegexPatternSetReferenceStatement, False),
        "RuleGroupReferenceStatement": (RuleGroupReferenceStatement, False),
        "SizeConstraintStatement": (SizeConstraintStatement, False),
        "SqliMatchStatement": (SqliMatchStatement, False),
        "XssMatchStatement": (XssMatchStatement, False),
    }


class AndStatementOne(AWSProperty):
    """
    `AndStatementOne <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html>`__
    """

    props: PropsDictType = {
        "Statements": ([StatementTwo], True),
    }


class NotStatementOne(AWSProperty):
    """
    `NotStatementOne <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html>`__
    """

    props: PropsDictType = {
        "Statement": (StatementTwo, True),
    }


class OrStatementOne(AWSProperty):
    """
    `OrStatementOne <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html>`__
    """

    props: PropsDictType = {
        "Statements": ([StatementTwo], True),
    }


class RateBasedStatementOne(AWSProperty):
    """
    `RateBasedStatementOne <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html>`__
    """

    props: PropsDictType = {
        "AggregateKeyType": (str, True),
        "ForwardedIPConfig": (ForwardedIPConfiguration, False),
        "Limit": (integer, True),
        "ScopeDownStatement": (StatementTwo, False),
    }


class StatementOne(AWSProperty):
    """
    `StatementOne <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html>`__
    """

    props: PropsDictType = {
        "AndStatement": (AndStatementOne, False),
        "ByteMatchStatement": (ByteMatchStatement, False),
        "GeoMatchStatement": (GeoMatchStatement, False),
        "IPSetReferenceStatement": (IPSetReferenceStatement, False),
        "LabelMatchStatement": (LabelMatchStatement, False),
        "ManagedRuleGroupStatement": (ManagedRuleGroupStatement, False),
        "NotStatement": (NotStatementOne, False),
        "OrStatement": (OrStatementOne, False),
        "RateBasedStatement": (RateBasedStatementOne, False),
        "RegexMatchStatement": (RegexMatchStatement, False),
        "RegexPatternSetReferenceStatement": (RegexPatternSetReferenceStatement, False),
        "RuleGroupReferenceStatement": (RuleGroupReferenceStatement, False),
        "SizeConstraintStatement": (SizeConstraintStatement, False),
        "SqliMatchStatement": (SqliMatchStatement, False),
        "XssMatchStatement": (XssMatchStatement, False),
    }


class VisibilityConfig(AWSProperty):
    """
    `VisibilityConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html>`__
    """

    props: PropsDictType = {
        "CloudWatchMetricsEnabled": (boolean, True),
        "MetricName": (str, True),
        "SampledRequestsEnabled": (boolean, True),
    }


class RuleGroupRule(AWSProperty):
    """
    `RuleGroupRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html>`__
    """

    props: PropsDictType = {
        "Action": (RuleAction, False),
        "CaptchaConfig": (CaptchaConfig, False),
        "Name": (str, True),
        "Priority": (integer, True),
        "RuleLabels": ([Label], False),
        "Statement": (StatementOne, True),
        "VisibilityConfig": (VisibilityConfig, True),
    }


class RuleGroup(AWSObject):
    """
    `RuleGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html>`__
    """

    resource_type = "AWS::WAFv2::RuleGroup"

    props: PropsDictType = {
        "Capacity": (integer, True),
        "CustomResponseBodies": (validate_custom_response_bodies, False),
        "Description": (str, False),
        "Name": (str, False),
        "Rules": ([RuleGroupRule], False),
        "Scope": (str, True),
        "Tags": (Tags, False),
        "VisibilityConfig": (VisibilityConfig, True),
    }


class DefaultAction(AWSProperty):
    """
    `DefaultAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html>`__
    """

    props: PropsDictType = {
        "Allow": (AllowAction, False),
        "Block": (BlockAction, False),
    }


class OverrideAction(AWSProperty):
    """
    `OverrideAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html>`__
    """

    props: PropsDictType = {
        "Count": (dict, False),
        "None": (dict, False),
    }


class WebACLRule(AWSProperty):
    """
    `WebACLRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html>`__
    """

    props: PropsDictType = {
        "Action": (RuleAction, False),
        "CaptchaConfig": (CaptchaConfig, False),
        "Name": (str, True),
        "OverrideAction": (OverrideAction, False),
        "Priority": (integer, True),
        "RuleLabels": ([Label], False),
        "Statement": (StatementOne, True),
        "VisibilityConfig": (VisibilityConfig, True),
    }


class WebACL(AWSObject):
    """
    `WebACL <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html>`__
    """

    resource_type = "AWS::WAFv2::WebACL"

    props: PropsDictType = {
        "CaptchaConfig": (CaptchaConfig, False),
        "CustomResponseBodies": (validate_custom_response_bodies, False),
        "DefaultAction": (DefaultAction, True),
        "Description": (str, False),
        "Name": (str, False),
        "Rules": ([WebACLRule], False),
        "Scope": (str, True),
        "Tags": (Tags, False),
        "VisibilityConfig": (VisibilityConfig, True),
    }


class WebACLAssociation(AWSObject):
    """
    `WebACLAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html>`__
    """

    resource_type = "AWS::WAFv2::WebACLAssociation"

    props: PropsDictType = {
        "ResourceArn": (str, True),
        "WebACLArn": (str, True),
    }
