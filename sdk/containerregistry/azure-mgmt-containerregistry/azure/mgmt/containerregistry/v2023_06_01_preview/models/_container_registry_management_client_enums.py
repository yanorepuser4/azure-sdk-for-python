# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Action(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action of IP ACL rule."""

    ALLOW = "Allow"


class ActionsRequired(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A message indicating if changes on the service provider require any updates on the consumer."""

    NONE = "None"
    RECREATE = "Recreate"


class ActivationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The activation status of the connected registry."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class AuditLogStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether audit logs are enabled on the connected registry."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class AzureADAuthenticationAsArmPolicyStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The value that indicates whether the policy is enabled or not."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class CertificateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of certificate location."""

    LOCAL_DIRECTORY = "LocalDirectory"


class ConnectedRegistryMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode of the connected registry resource that indicates the permissions of the registry."""

    READ_WRITE = "ReadWrite"
    READ_ONLY = "ReadOnly"
    REGISTRY = "Registry"
    MIRROR = "Mirror"


class ConnectionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current connection state of the connected registry."""

    ONLINE = "Online"
    OFFLINE = "Offline"
    SYNCING = "Syncing"
    UNHEALTHY = "Unhealthy"


class ConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private link service connection status."""

    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CredentialHealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The health status of credential."""

    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"


class CredentialName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the credential."""

    CREDENTIAL1 = "Credential1"


class DefaultAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default action of allow or deny when no other rules match."""

    ALLOW = "Allow"
    DENY = "Deny"


class EncryptionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether or not the encryption is enabled for container registry."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ExportPolicyStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The value that indicates whether the policy is enabled or not."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ImportMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """When Force, any existing target tags will be overwritten. When NoForce, any existing target
    tags will fail the operation before any copying begins.
    """

    NO_FORCE = "NoForce"
    FORCE = "Force"


class LastModifiedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that last modified the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class LogLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The verbosity of logs persisted on the connected registry."""

    DEBUG = "Debug"
    INFORMATION = "Information"
    WARNING = "Warning"
    ERROR = "Error"
    NONE = "None"


class NetworkRuleBypassOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to allow trusted Azure services to access a network restricted registry."""

    AZURE_SERVICES = "AzureServices"
    NONE = "None"


class PackageSourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of package source for a archive."""

    REMOTE = "remote"


class PasswordName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The password name."""

    PASSWORD = "password"
    PASSWORD2 = "password2"


class PipelineOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PipelineOptions."""

    OVERWRITE_TAGS = "OverwriteTags"
    OVERWRITE_BLOBS = "OverwriteBlobs"
    DELETE_SOURCE_BLOB_ON_SUCCESS = "DeleteSourceBlobOnSuccess"
    CONTINUE_ON_ERRORS = "ContinueOnErrors"


class PipelineRunSourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the source."""

    AZURE_STORAGE_BLOB = "AzureStorageBlob"


class PipelineRunTargetType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the target."""

    AZURE_STORAGE_BLOB = "AzureStorageBlob"


class PipelineSourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of source for the import pipeline."""

    AZURE_STORAGE_BLOB_CONTAINER = "AzureStorageBlobContainer"


class PolicyStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The value that indicates whether the policy is enabled or not."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the archive at the time the operation was called."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether or not public network access is allowed for the container registry."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RegistryUsageUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit of measurement."""

    COUNT = "Count"
    BYTES = "Bytes"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU name of the container registry. Required for registry creation."""

    CLASSIC = "Classic"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU tier based on the SKU name."""

    CLASSIC = "Classic"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class TlsStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether HTTPS is enabled for the login server."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TokenCertificateName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TokenCertificateName."""

    CERTIFICATE1 = "certificate1"
    CERTIFICATE2 = "certificate2"


class TokenPasswordName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The password name "password1" or "password2"."""

    PASSWORD1 = "password1"
    PASSWORD2 = "password2"


class TokenStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the token example enabled or disabled."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class TriggerStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current status of the source trigger."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TrustPolicyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of trust policy."""

    NOTARY = "Notary"


class WebhookAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """WebhookAction."""

    PUSH = "push"
    DELETE = "delete"
    QUARANTINE = "quarantine"
    CHART_PUSH = "chart_push"
    CHART_DELETE = "chart_delete"


class WebhookStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the webhook at the time the operation was called."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ZoneRedundancy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether or not zone redundancy is enabled for this container registry."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"
