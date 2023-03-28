# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AgentPoolProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AgentPoolProvisioningState."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    IN_PROGRESS = "InProgress"
    CANCELED = "Canceled"


class AutoUpgradeOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the Arc agents on the provisioned clusters be upgraded automatically to the
    latest version. Defaults to Enabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DeploymentState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Observed deployment state of the Arc Agents on the target cluster. Possible values include:
    'pending', 'provisioning', 'provisioned', 'deleting', 'failed', 'upgrading'.
    """

    PENDING = "pending"
    PROVISIONING = "provisioning"
    PROVISIONED = "provisioned"
    DELETING = "deleting"
    FAILED = "failed"
    UPGRADING = "upgrading"


class LicenseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LicenseType - The licenseType to use for Windows VMs. Windows_Server is used to enable Azure
    Hybrid User Benefits for Windows VMs. Possible values include: 'None', 'Windows_Server'.
    """

    WINDOWS_SERVER = "Windows_Server"
    NONE = "None"


class LoadBalancerSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LoadBalancerSku - The load balancer sku for the provisioned cluster. Possible values:
    'unstacked-haproxy', 'stacked-kube-vip', 'stacked-metallb', 'unmanaged'. The default is
    'unmanaged'.
    """

    UNSTACKED_HAPROXY = "unstacked-haproxy"
    STACKED_KUBE_VIP = "stacked-kube-vip"
    STACKED_METALLB = "stacked-metallb"
    UNMANAGED = "unmanaged"


class Mode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Mode - AgentPoolMode represents mode of an agent pool. Possible values include: 'System', 'LB',
    'User'. Default is 'User'.
    """

    SYSTEM = "System"
    LB = "LB"
    USER = "User"


class NetworkPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """NetworkPolicy - Network policy used for building Kubernetes network. Possible values include:
    'calico', 'flannel'. Default is 'calico'.
    """

    CALICO = "calico"
    FLANNEL = "flannel"


class OsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OsType - OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux.
    Possible values include: 'Linux', 'Windows'.
    """

    LINUX = "Linux"
    WINDOWS = "Windows"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProvisioningState."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    IN_PROGRESS = "InProgress"
    DELETING = "Deleting"
    UPDATING = "Updating"
    ACCEPTED = "Accepted"
    CREATED = "Created"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the provisioned cluster. The type SystemAssigned, includes a
    system created identity. The type None means no identity is assigned to the provisioned
    cluster.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"