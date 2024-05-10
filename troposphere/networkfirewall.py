# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.networkfirewall import validate_rule_group_type


class SubnetMapping(AWSProperty):
    """
    `SubnetMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html>`__
    """

    props: PropsDictType = {
        "IPAddressType": (str, False),
        "SubnetId": (str, True),
    }


class Firewall(AWSObject):
    """
    `Firewall <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html>`__
    """

    resource_type = "AWS::NetworkFirewall::Firewall"

    props: PropsDictType = {
        "DeleteProtection": (boolean, False),
        "Description": (str, False),
        "FirewallName": (str, True),
        "FirewallPolicyArn": (str, True),
        "FirewallPolicyChangeProtection": (boolean, False),
        "SubnetChangeProtection": (boolean, False),
        "SubnetMappings": ([SubnetMapping], True),
        "Tags": (Tags, False),
        "VpcId": (str, True),
    }


class Dimension(AWSProperty):
    """
    `Dimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html>`__
    """

    props: PropsDictType = {
        "Value": (str, True),
    }


class PublishMetricAction(AWSProperty):
    """
    `PublishMetricAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html>`__
    """

    props: PropsDictType = {
        "Dimensions": ([Dimension], True),
    }


class ActionDefinition(AWSProperty):
    """
    `ActionDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html>`__
    """

    props: PropsDictType = {
        "PublishMetricAction": (PublishMetricAction, False),
    }


class CustomAction(AWSProperty):
    """
    `CustomAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html>`__
    """

    props: PropsDictType = {
        "ActionDefinition": (ActionDefinition, True),
        "ActionName": (str, True),
    }


class IPSet(AWSProperty):
    """
    `IPSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html>`__
    """

    props: PropsDictType = {
        "Definition": ([str], False),
    }


class PolicyVariables(AWSProperty):
    """
    `PolicyVariables <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-policyvariables.html>`__
    """

    props: PropsDictType = {
        "RuleVariables": (dict, False),
    }


class StatefulEngineOptions(AWSProperty):
    """
    `StatefulEngineOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html>`__
    """

    props: PropsDictType = {
        "RuleOrder": (str, False),
        "StreamExceptionPolicy": (str, False),
    }


class StatefulRuleGroupOverride(AWSProperty):
    """
    `StatefulRuleGroupOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
    }


class StatefulRuleGroupReference(AWSProperty):
    """
    `StatefulRuleGroupReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html>`__
    """

    props: PropsDictType = {
        "Override": (StatefulRuleGroupOverride, False),
        "Priority": (integer, False),
        "ResourceArn": (str, True),
    }


class StatelessRuleGroupReference(AWSProperty):
    """
    `StatelessRuleGroupReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html>`__
    """

    props: PropsDictType = {
        "Priority": (integer, True),
        "ResourceArn": (str, True),
    }


class FirewallPolicyProperty(AWSProperty):
    """
    `FirewallPolicyProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html>`__
    """

    props: PropsDictType = {
        "PolicyVariables": (PolicyVariables, False),
        "StatefulDefaultActions": ([str], False),
        "StatefulEngineOptions": (StatefulEngineOptions, False),
        "StatefulRuleGroupReferences": ([StatefulRuleGroupReference], False),
        "StatelessCustomActions": ([CustomAction], False),
        "StatelessDefaultActions": ([str], True),
        "StatelessFragmentDefaultActions": ([str], True),
        "StatelessRuleGroupReferences": ([StatelessRuleGroupReference], False),
        "TLSInspectionConfigurationArn": (str, False),
    }


class FirewallPolicy(AWSObject):
    """
    `FirewallPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html>`__
    """

    resource_type = "AWS::NetworkFirewall::FirewallPolicy"

    props: PropsDictType = {
        "Description": (str, False),
        "FirewallPolicy": (FirewallPolicyProperty, True),
        "FirewallPolicyName": (str, True),
        "Tags": (Tags, False),
    }


class LogDestinationConfig(AWSProperty):
    """
    `LogDestinationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html>`__
    """

    props: PropsDictType = {
        "LogDestination": (dict, True),
        "LogDestinationType": (str, True),
        "LogType": (str, True),
    }


class LoggingConfigurationProperty(AWSProperty):
    """
    `LoggingConfigurationProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogDestinationConfigs": ([LogDestinationConfig], True),
    }


class LoggingConfiguration(AWSObject):
    """
    `LoggingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html>`__
    """

    resource_type = "AWS::NetworkFirewall::LoggingConfiguration"

    props: PropsDictType = {
        "FirewallArn": (str, True),
        "FirewallName": (str, False),
        "LoggingConfiguration": (LoggingConfigurationProperty, True),
    }


class IPSetReference(AWSProperty):
    """
    `IPSetReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipsetreference.html>`__
    """

    props: PropsDictType = {
        "ReferenceArn": (str, False),
    }


class ReferenceSets(AWSProperty):
    """
    `ReferenceSets <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-referencesets.html>`__
    """

    props: PropsDictType = {
        "IPSetReferences": (dict, False),
    }


class PortSet(AWSProperty):
    """
    `PortSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html>`__
    """

    props: PropsDictType = {
        "Definition": ([str], False),
    }


class RuleVariables(AWSProperty):
    """
    `RuleVariables <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html>`__
    """

    props: PropsDictType = {
        "IPSets": (dict, False),
        "PortSets": (dict, False),
    }


class RulesSourceList(AWSProperty):
    """
    `RulesSourceList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html>`__
    """

    props: PropsDictType = {
        "GeneratedRulesType": (str, True),
        "TargetTypes": ([str], True),
        "Targets": ([str], True),
    }


class Header(AWSProperty):
    """
    `Header <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html>`__
    """

    props: PropsDictType = {
        "Destination": (str, True),
        "DestinationPort": (str, True),
        "Direction": (str, True),
        "Protocol": (str, True),
        "Source": (str, True),
        "SourcePort": (str, True),
    }


class RuleOption(AWSProperty):
    """
    `RuleOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html>`__
    """

    props: PropsDictType = {
        "Keyword": (str, True),
        "Settings": ([str], False),
    }


class StatefulRule(AWSProperty):
    """
    `StatefulRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
        "Header": (Header, True),
        "RuleOptions": ([RuleOption], True),
    }


class Address(AWSProperty):
    """
    `Address <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-address.html>`__
    """

    props: PropsDictType = {
        "AddressDefinition": (str, True),
    }


class PortRange(AWSProperty):
    """
    `PortRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-portrange.html>`__
    """

    props: PropsDictType = {
        "FromPort": (integer, True),
        "ToPort": (integer, True),
    }


class TCPFlagField(AWSProperty):
    """
    `TCPFlagField <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html>`__
    """

    props: PropsDictType = {
        "Flags": ([str], True),
        "Masks": ([str], False),
    }


class MatchAttributes(AWSProperty):
    """
    `MatchAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html>`__
    """

    props: PropsDictType = {
        "DestinationPorts": ([PortRange], False),
        "Destinations": ([Address], False),
        "Protocols": ([integer], False),
        "SourcePorts": ([PortRange], False),
        "Sources": ([Address], False),
        "TCPFlags": ([TCPFlagField], False),
    }


class RuleDefinition(AWSProperty):
    """
    `RuleDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html>`__
    """

    props: PropsDictType = {
        "Actions": ([str], True),
        "MatchAttributes": (MatchAttributes, True),
    }


class StatelessRule(AWSProperty):
    """
    `StatelessRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html>`__
    """

    props: PropsDictType = {
        "Priority": (integer, True),
        "RuleDefinition": (RuleDefinition, True),
    }


class StatelessRulesAndCustomActions(AWSProperty):
    """
    `StatelessRulesAndCustomActions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html>`__
    """

    props: PropsDictType = {
        "CustomActions": ([CustomAction], False),
        "StatelessRules": ([StatelessRule], True),
    }


class RulesSource(AWSProperty):
    """
    `RulesSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html>`__
    """

    props: PropsDictType = {
        "RulesSourceList": (RulesSourceList, False),
        "RulesString": (str, False),
        "StatefulRules": ([StatefulRule], False),
        "StatelessRulesAndCustomActions": (StatelessRulesAndCustomActions, False),
    }


class StatefulRuleOptions(AWSProperty):
    """
    `StatefulRuleOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html>`__
    """

    props: PropsDictType = {
        "RuleOrder": (str, False),
    }


class RuleGroupProperty(AWSProperty):
    """
    `RuleGroupProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html>`__
    """

    props: PropsDictType = {
        "ReferenceSets": (ReferenceSets, False),
        "RuleVariables": (RuleVariables, False),
        "RulesSource": (RulesSource, True),
        "StatefulRuleOptions": (StatefulRuleOptions, False),
    }


class RuleGroup(AWSObject):
    """
    `RuleGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html>`__
    """

    resource_type = "AWS::NetworkFirewall::RuleGroup"

    props: PropsDictType = {
        "Capacity": (integer, True),
        "Description": (str, False),
        "RuleGroup": (RuleGroupProperty, False),
        "RuleGroupName": (str, True),
        "Tags": (Tags, False),
        "Type": (validate_rule_group_type, True),
    }


class CheckCertificateRevocationStatus(AWSProperty):
    """
    `CheckCertificateRevocationStatus <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus.html>`__
    """

    props: PropsDictType = {
        "RevokedStatusAction": (str, False),
        "UnknownStatusAction": (str, False),
    }


class ServerCertificate(AWSProperty):
    """
    `ServerCertificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate.html>`__
    """

    props: PropsDictType = {
        "ResourceArn": (str, False),
    }


class ServerCertificateScope(AWSProperty):
    """
    `ServerCertificateScope <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html>`__
    """

    props: PropsDictType = {
        "DestinationPorts": ([PortRange], False),
        "Destinations": ([Address], False),
        "Protocols": ([integer], False),
        "SourcePorts": ([PortRange], False),
        "Sources": ([Address], False),
    }


class ServerCertificateConfiguration(AWSProperty):
    """
    `ServerCertificateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html>`__
    """

    props: PropsDictType = {
        "CertificateAuthorityArn": (str, False),
        "CheckCertificateRevocationStatus": (CheckCertificateRevocationStatus, False),
        "Scopes": ([ServerCertificateScope], False),
        "ServerCertificates": ([ServerCertificate], False),
    }


class TLSInspectionConfigurationProperty(AWSProperty):
    """
    `TLSInspectionConfigurationProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration.html>`__
    """

    props: PropsDictType = {
        "ServerCertificateConfigurations": ([ServerCertificateConfiguration], False),
    }


class TLSInspectionConfiguration(AWSObject):
    """
    `TLSInspectionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-tlsinspectionconfiguration.html>`__
    """

    resource_type = "AWS::NetworkFirewall::TLSInspectionConfiguration"

    props: PropsDictType = {
        "Description": (str, False),
        "TLSInspectionConfiguration": (TLSInspectionConfigurationProperty, True),
        "TLSInspectionConfigurationName": (str, True),
        "Tags": (Tags, False),
    }
