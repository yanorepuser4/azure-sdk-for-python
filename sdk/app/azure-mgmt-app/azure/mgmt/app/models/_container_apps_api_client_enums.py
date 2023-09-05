# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access mode for storage
    """

    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"

class ActiveRevisionsMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ActiveRevisionsMode controls how active revisions are handled for the Container app:
    
    
    .. raw:: html
    
       <list><item>Multiple: multiple revisions can be active. If no value if provided, this is the
    default</item><item>Single: Only one revision can be active at a time. Revision weights can not
    be used in this mode</item></list>
    """

    MULTIPLE = "multiple"
    SINGLE = "single"

class AppProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells Dapr which protocol your application is using. Valid options are http and grpc. Default
    is http
    """

    HTTP = "http"
    GRPC = "grpc"

class BindingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Custom Domain binding type.
    """

    DISABLED = "Disabled"
    SNI_ENABLED = "SniEnabled"

class CertificateProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the certificate.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETE_FAILED = "DeleteFailed"
    PENDING = "Pending"

class ContainerAppProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Container App.
    """

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class CookieExpirationConvention(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The convention used when determining the session cookie's expiration.
    """

    FIXED_TIME = "FixedTime"
    IDENTITY_PROVIDER_DERIVED = "IdentityProviderDerived"

class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DnsVerificationTestResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DNS verification test result.
    """

    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"

class EnvironmentProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Environment.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    WAITING = "Waiting"
    INITIALIZATION_IN_PROGRESS = "InitializationInProgress"
    INFRASTRUCTURE_SETUP_IN_PROGRESS = "InfrastructureSetupInProgress"
    INFRASTRUCTURE_SETUP_COMPLETE = "InfrastructureSetupComplete"
    SCHEDULED_FOR_DELETE = "ScheduledForDelete"
    UPGRADE_REQUESTED = "UpgradeRequested"
    UPGRADE_FAILED = "UpgradeFailed"

class ForwardProxyConvention(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The convention used to determine the url of the request made.
    """

    NO_PROXY = "NoProxy"
    STANDARD = "Standard"
    CUSTOM = "Custom"

class IngressTransportMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Ingress transport protocol
    """

    AUTO = "auto"
    HTTP = "http"
    HTTP2 = "http2"

class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"

class RevisionHealthState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current health State of the revision
    """

    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    NONE = "None"

class RevisionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current provisioning State of the revision
    """

    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    FAILED = "Failed"
    DEPROVISIONING = "Deprovisioning"
    DEPROVISIONED = "Deprovisioned"

class SourceControlOperationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current provisioning State of the operation
    """

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class StorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage type for the volume. If not provided, use EmptyDir.
    """

    AZURE_FILE = "AzureFile"
    EMPTY_DIR = "EmptyDir"

class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of probe.
    """

    LIVENESS = "liveness"
    READINESS = "readiness"
    STARTUP = "startup"

class UnauthenticatedClientActionV2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action to take when an unauthenticated client attempts to access the app.
    """

    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"
    RETURN401 = "Return401"
    RETURN403 = "Return403"
