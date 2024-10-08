# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double


class AttachmentsConfiguration(AWSProperty):
    """
    `AttachmentsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-attachmentsconfiguration.html>`__
    """

    props: PropsDictType = {
        "AttachmentsControlMode": (str, True),
    }


class AutoSubscriptionConfiguration(AWSProperty):
    """
    `AutoSubscriptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-autosubscriptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "AutoSubscribe": (str, True),
        "DefaultSubscriptionType": (str, False),
    }


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
    }


class PersonalizationConfiguration(AWSProperty):
    """
    `PersonalizationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-personalizationconfiguration.html>`__
    """

    props: PropsDictType = {
        "PersonalizationControlMode": (str, True),
    }


class QAppsConfiguration(AWSProperty):
    """
    `QAppsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-qappsconfiguration.html>`__
    """

    props: PropsDictType = {
        "QAppsControlMode": (str, True),
    }


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html>`__
    """

    resource_type = "AWS::QBusiness::Application"

    props: PropsDictType = {
        "AttachmentsConfiguration": (AttachmentsConfiguration, False),
        "AutoSubscriptionConfiguration": (AutoSubscriptionConfiguration, False),
        "ClientIdsForOIDC": ([str], False),
        "Description": (str, False),
        "DisplayName": (str, True),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "IamIdentityProviderArn": (str, False),
        "IdentityCenterInstanceArn": (str, False),
        "IdentityType": (str, False),
        "PersonalizationConfiguration": (PersonalizationConfiguration, False),
        "QAppsConfiguration": (QAppsConfiguration, False),
        "RoleArn": (str, False),
        "Tags": (Tags, False),
    }


class DataSourceVpcConfiguration(AWSProperty):
    """
    `DataSourceVpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-datasourcevpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], True),
        "SubnetIds": ([str], True),
    }


class DocumentAttributeValue(AWSProperty):
    """
    `DocumentAttributeValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributevalue.html>`__
    """

    props: PropsDictType = {
        "DateValue": (str, False),
        "LongValue": (double, False),
        "StringListValue": ([str], False),
        "StringValue": (str, False),
    }


class DocumentAttributeCondition(AWSProperty):
    """
    `DocumentAttributeCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributecondition.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Operator": (str, True),
        "Value": (DocumentAttributeValue, False),
    }


class HookConfiguration(AWSProperty):
    """
    `HookConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-hookconfiguration.html>`__
    """

    props: PropsDictType = {
        "InvocationCondition": (DocumentAttributeCondition, False),
        "LambdaArn": (str, False),
        "RoleArn": (str, False),
        "S3BucketName": (str, False),
    }


class DocumentAttributeTarget(AWSProperty):
    """
    `DocumentAttributeTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributetarget.html>`__
    """

    props: PropsDictType = {
        "AttributeValueOperator": (str, False),
        "Key": (str, True),
        "Value": (DocumentAttributeValue, False),
    }


class InlineDocumentEnrichmentConfiguration(AWSProperty):
    """
    `InlineDocumentEnrichmentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration.html>`__
    """

    props: PropsDictType = {
        "Condition": (DocumentAttributeCondition, False),
        "DocumentContentOperator": (str, False),
        "Target": (DocumentAttributeTarget, False),
    }


class DocumentEnrichmentConfiguration(AWSProperty):
    """
    `DocumentEnrichmentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentenrichmentconfiguration.html>`__
    """

    props: PropsDictType = {
        "InlineConfigurations": ([InlineDocumentEnrichmentConfiguration], False),
        "PostExtractionHookConfiguration": (HookConfiguration, False),
        "PreExtractionHookConfiguration": (HookConfiguration, False),
    }


class DataSource(AWSObject):
    """
    `DataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html>`__
    """

    resource_type = "AWS::QBusiness::DataSource"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "Configuration": (dict, True),
        "Description": (str, False),
        "DisplayName": (str, True),
        "DocumentEnrichmentConfiguration": (DocumentEnrichmentConfiguration, False),
        "IndexId": (str, True),
        "RoleArn": (str, False),
        "SyncSchedule": (str, False),
        "Tags": (Tags, False),
        "VpcConfiguration": (DataSourceVpcConfiguration, False),
    }


class DocumentAttributeConfiguration(AWSProperty):
    """
    `DocumentAttributeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-documentattributeconfiguration.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Search": (str, False),
        "Type": (str, False),
    }


class IndexCapacityConfiguration(AWSProperty):
    """
    `IndexCapacityConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-indexcapacityconfiguration.html>`__
    """

    props: PropsDictType = {
        "Units": (double, False),
    }


class Index(AWSObject):
    """
    `Index <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html>`__
    """

    resource_type = "AWS::QBusiness::Index"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "CapacityConfiguration": (IndexCapacityConfiguration, False),
        "Description": (str, False),
        "DisplayName": (str, True),
        "DocumentAttributeConfigurations": ([DocumentAttributeConfiguration], False),
        "Tags": (Tags, False),
        "Type": (str, False),
    }


class S3(AWSProperty):
    """
    `S3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-s3.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
    }


class APISchema(AWSProperty):
    """
    `APISchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-apischema.html>`__
    """

    props: PropsDictType = {
        "Payload": (str, False),
        "S3": (S3, False),
    }


class CustomPluginConfiguration(AWSProperty):
    """
    `CustomPluginConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-custompluginconfiguration.html>`__
    """

    props: PropsDictType = {
        "ApiSchema": (APISchema, True),
        "ApiSchemaType": (str, True),
        "Description": (str, True),
    }


class BasicAuthConfiguration(AWSProperty):
    """
    `BasicAuthConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-basicauthconfiguration.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, True),
        "SecretArn": (str, True),
    }


class OAuth2ClientCredentialConfiguration(AWSProperty):
    """
    `OAuth2ClientCredentialConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, True),
        "SecretArn": (str, True),
    }


class PluginAuthConfiguration(AWSProperty):
    """
    `PluginAuthConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-pluginauthconfiguration.html>`__
    """

    props: PropsDictType = {
        "BasicAuthConfiguration": (BasicAuthConfiguration, False),
        "NoAuthConfiguration": (dict, False),
        "OAuth2ClientCredentialConfiguration": (
            OAuth2ClientCredentialConfiguration,
            False,
        ),
    }


class Plugin(AWSObject):
    """
    `Plugin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html>`__
    """

    resource_type = "AWS::QBusiness::Plugin"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "AuthConfiguration": (PluginAuthConfiguration, True),
        "CustomPluginConfiguration": (CustomPluginConfiguration, False),
        "DisplayName": (str, True),
        "ServerUrl": (str, False),
        "State": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class KendraIndexConfiguration(AWSProperty):
    """
    `KendraIndexConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-kendraindexconfiguration.html>`__
    """

    props: PropsDictType = {
        "IndexId": (str, True),
    }


class NativeIndexConfiguration(AWSProperty):
    """
    `NativeIndexConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-nativeindexconfiguration.html>`__
    """

    props: PropsDictType = {
        "IndexId": (str, True),
    }


class RetrieverConfiguration(AWSProperty):
    """
    `RetrieverConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-retrieverconfiguration.html>`__
    """

    props: PropsDictType = {
        "KendraIndexConfiguration": (KendraIndexConfiguration, False),
        "NativeIndexConfiguration": (NativeIndexConfiguration, False),
    }


class Retriever(AWSObject):
    """
    `Retriever <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html>`__
    """

    resource_type = "AWS::QBusiness::Retriever"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "Configuration": (RetrieverConfiguration, True),
        "DisplayName": (str, True),
        "RoleArn": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class OpenIDConnectProviderConfiguration(AWSProperty):
    """
    `OpenIDConnectProviderConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecretsArn": (str, True),
        "SecretsRole": (str, True),
    }


class SamlProviderConfiguration(AWSProperty):
    """
    `SamlProviderConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-samlproviderconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuthenticationUrl": (str, True),
    }


class IdentityProviderConfiguration(AWSProperty):
    """
    `IdentityProviderConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-identityproviderconfiguration.html>`__
    """

    props: PropsDictType = {
        "OpenIDConnectConfiguration": (OpenIDConnectProviderConfiguration, False),
        "SamlConfiguration": (SamlProviderConfiguration, False),
    }


class WebExperience(AWSObject):
    """
    `WebExperience <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html>`__
    """

    resource_type = "AWS::QBusiness::WebExperience"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "IdentityProviderConfiguration": (IdentityProviderConfiguration, False),
        "RoleArn": (str, False),
        "SamplePromptsControlMode": (str, False),
        "Subtitle": (str, False),
        "Tags": (Tags, False),
        "Title": (str, False),
        "WelcomeMessage": (str, False),
    }


class TextDocumentStatistics(AWSProperty):
    """
    `TextDocumentStatistics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-textdocumentstatistics.html>`__
    """

    props: PropsDictType = {
        "IndexedTextBytes": (double, False),
        "IndexedTextDocumentCount": (double, False),
    }


class IndexStatistics(AWSProperty):
    """
    `IndexStatistics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-indexstatistics.html>`__
    """

    props: PropsDictType = {
        "TextDocumentStatistics": (TextDocumentStatistics, False),
    }
