# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AddonAutoscaling(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether VPA add-on is enabled and configured to scale AKS-managed add-ons."""

    ENABLED = "Enabled"
    """Feature to autoscale AKS-managed add-ons is enabled. The default VPA update mode is Initial
    #: mode."""
    DISABLED = "Disabled"
    """Feature to autoscale AKS-managed add-ons is disabled."""


class AgentPoolMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A cluster must have at least one 'System' Agent Pool at all times. For additional information
    on agent pool restrictions and best practices, see:
    https://docs.microsoft.com/azure/aks/use-system-pools.
    """

    SYSTEM = "System"
    """System agent pools are primarily for hosting critical system pods such as CoreDNS and
    #: metrics-server. System agent pools osType must be Linux. System agent pools VM SKU must have at
    #: least 2vCPUs and 4GB of memory."""
    USER = "User"
    """User agent pools are primarily for hosting your application pods."""


class AgentPoolSSHAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SSH access method of an agent pool."""

    LOCAL_USER = "LocalUser"
    """Can SSH onto the node as a local user using private key."""
    DISABLED = "Disabled"
    """SSH service will be turned off on the node."""


class AgentPoolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Agent Pool."""

    VIRTUAL_MACHINE_SCALE_SETS = "VirtualMachineScaleSets"
    """Create an Agent Pool backed by a Virtual Machine Scale Set."""
    AVAILABILITY_SET = "AvailabilitySet"
    """Use of this is strongly discouraged."""
    VIRTUAL_MACHINES = "VirtualMachines"
    """Create an Agent Pool backed by a Single Instance VM orchestration mode."""


class BackendPoolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the managed inbound Load Balancer BackendPool."""

    NODE_IP_CONFIGURATION = "NodeIPConfiguration"
    """The type of the managed inbound Load Balancer BackendPool.
    #: https://cloud-provider-azure.sigs.k8s.io/topics/loadbalancer/#configure-load-balancer-backend."""
    NODE_IP = "NodeIP"
    """The type of the managed inbound Load Balancer BackendPool.
    #: https://cloud-provider-azure.sigs.k8s.io/topics/loadbalancer/#configure-load-balancer-backend."""


class Code(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells whether the cluster is Running or Stopped."""

    RUNNING = "Running"
    """The cluster is running."""
    STOPPED = "Stopped"
    """The cluster is stopped."""


class ConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private link service connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Expander(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If not specified, the default is 'random'. See `expanders
    <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-expanders>`_
    for more information.
    """

    LEAST_WASTE = "least-waste"
    """Selects the node group that will have the least idle CPU (if tied, unused memory) after
    #: scale-up. This is useful when you have different classes of nodes, for example, high CPU or
    #: high memory nodes, and only want to expand those when there are pending pods that need a lot of
    #: those resources."""
    MOST_PODS = "most-pods"
    """Selects the node group that would be able to schedule the most pods when scaling up. This is
    #: useful when you are using nodeSelector to make sure certain pods land on certain nodes. Note
    #: that this won't cause the autoscaler to select bigger nodes vs. smaller, as it can add multiple
    #: smaller nodes at once."""
    PRIORITY = "priority"
    """Selects the node group that has the highest priority assigned by the user. It's configuration
    #: is described in more details `here
    #: <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md>`_."""
    RANDOM = "random"
    """Used when you don't have a particular need for the node groups to scale differently."""


class ExtendedLocationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of extendedLocation."""

    EDGE_ZONE = "EdgeZone"


class Format(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Format."""

    AZURE = "azure"
    """Return azure auth-provider kubeconfig. This format is deprecated in v1.22 and will be fully
    #: removed in v1.26. See: https://aka.ms/k8s/changes-1-26."""
    EXEC = "exec"
    """Return exec format kubeconfig. This format requires kubelogin binary in the path."""
    EXEC_ENUM = "exec"
    """Return exec format kubeconfig. This format requires kubelogin binary in the path."""


class GPUInstanceProfile(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU."""

    MIG1_G = "MIG1g"
    MIG2_G = "MIG2g"
    MIG3_G = "MIG3g"
    MIG4_G = "MIG4g"
    MIG7_G = "MIG7g"


class GuardrailsSupport(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the version is preview or stable."""

    PREVIEW = "Preview"
    """The version is preview. It is not recommended to use preview versions on critical production
    #: clusters. The preview version may not support all use-cases."""
    STABLE = "Stable"
    """The version is stable and can be used on critical production clusters."""


class IpFamily(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """To determine if address belongs IPv4 or IPv6 family."""

    I_PV4 = "IPv4"
    """IPv4 family"""
    I_PV6 = "IPv6"
    """IPv6 family"""


class IpvsScheduler(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IPVS scheduler, for more information please see
    http://www.linuxvirtualserver.org/docs/scheduling.html.
    """

    ROUND_ROBIN = "RoundRobin"
    """Round Robin"""
    LEAST_CONNECTION = "LeastConnection"
    """Least Connection"""


class IstioIngressGatewayMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Mode of an ingress gateway."""

    EXTERNAL = "External"
    """The ingress gateway is assigned a public IP address and is publicly accessible."""
    INTERNAL = "Internal"
    """The ingress gateway is assigned an internal IP address and cannot is accessed publicly."""


class KeyVaultNetworkAccessTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network access of key vault. The possible values are ``Public`` and ``Private``. ``Public``
    means the key vault allows public access from all networks. ``Private`` means the key vault
    disables public access and enables private link. The default value is ``Public``.
    """

    PUBLIC = "Public"
    PRIVATE = "Private"


class KubeletDiskType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the placement of emptyDir volumes, container runtime data root, and Kubelet
    ephemeral storage.
    """

    OS = "OS"
    """Kubelet will use the OS disk for its data."""
    TEMPORARY = "Temporary"
    """Kubelet will use the temporary disk for its data."""


class KubernetesSupportPlan(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Different support tiers for AKS managed clusters."""

    KUBERNETES_OFFICIAL = "KubernetesOfficial"
    """Support for the version is the same as for the open source Kubernetes offering. Official
    #: Kubernetes open source community support versions for 1 year after release."""
    AKS_LONG_TERM_SUPPORT = "AKSLongTermSupport"
    """Support for the version extended past the KubernetesOfficial support of 1 year. AKS continues
    #: to patch CVEs for another 1 year, for a total of 2 years of support."""


class Level(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The guardrails level to be used. By default, Guardrails is enabled for all namespaces except
    those that AKS excludes via systemExcludedNamespaces.
    """

    OFF = "Off"
    WARNING = "Warning"
    ENFORCEMENT = "Enforcement"


class LicenseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The license type to use for Windows VMs. See `Azure Hybrid User Benefits
    <https://azure.microsoft.com/pricing/hybrid-benefit/faq/>`_ for more details.
    """

    NONE = "None"
    """No additional licensing is applied."""
    WINDOWS_SERVER = "Windows_Server"
    """Enables Azure Hybrid User Benefits for Windows VMs."""


class LoadBalancerSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default is 'standard'. See `Azure Load Balancer SKUs
    <https://docs.microsoft.com/azure/load-balancer/skus>`_ for more information about the
    differences between load balancer SKUs.
    """

    STANDARD = "standard"
    """Use a a standard Load Balancer. This is the recommended Load Balancer SKU. For more information
    #: about on working with the load balancer in the managed cluster, see the `standard Load Balancer
    #: <https://docs.microsoft.com/azure/aks/load-balancer-standard>`_ article."""
    BASIC = "basic"
    """Use a basic Load Balancer with limited functionality."""


class ManagedClusterPodIdentityProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state of the pod identity."""

    ASSIGNED = "Assigned"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class ManagedClusterSKUName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of a managed cluster SKU."""

    BASE = "Base"
    """Base option for the AKS control plane."""


class ManagedClusterSKUTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If not specified, the default is 'Free'. See `AKS Pricing Tier
    <https://learn.microsoft.com/azure/aks/free-standard-pricing-tiers>`_ for more details.
    """

    PREMIUM = "Premium"
    """Cluster has premium capabilities in addition to all of the capabilities included in 'Standard'.
    #: Premium enables selection of LongTermSupport (aka.ms/aks/lts) for certain Kubernetes versions."""
    STANDARD = "Standard"
    """Recommended for mission-critical and production workloads. Includes Kubernetes control plane
    #: autoscaling, workload-intensive testing, and up to 5,000 nodes per cluster. Guarantees 99.95%
    #: availability of the Kubernetes API server endpoint for clusters that use Availability Zones and
    #: 99.9% of availability for clusters that don't use Availability Zones."""
    FREE = "Free"
    """The cluster management is free, but charged for VM, storage, and networking usage. Best for
    #: experimenting, learning, simple testing, or workloads with fewer than 10 nodes. Not recommended
    #: for production use cases."""


class Mode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specify which proxy mode to use ('IPTABLES' or 'IPVS')."""

    IPTABLES = "IPTABLES"
    """IPTables proxy mode"""
    IPVS = "IPVS"
    """IPVS proxy mode. Must be using Kubernetes version >= 1.22."""


class NetworkDataplane(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network dataplane used in the Kubernetes cluster."""

    AZURE = "azure"
    """Use Azure network dataplane."""
    CILIUM = "cilium"
    """Use Cilium network dataplane. See `Azure CNI Powered by Cilium
    #: <https://learn.microsoft.com/azure/aks/azure-cni-powered-by-cilium>`_ for more information."""


class NetworkMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This cannot be specified if networkPlugin is anything other than 'azure'."""

    TRANSPARENT = "transparent"
    """No bridge is created. Intra-VM Pod to Pod communication is through IP routes created by Azure
    #: CNI. See `Transparent Mode <https://docs.microsoft.com/azure/aks/faq#transparent-mode>`_ for
    #: more information."""
    BRIDGE = "bridge"
    """This is no longer supported"""


class NetworkPlugin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network plugin used for building the Kubernetes network."""

    AZURE = "azure"
    """Use the Azure CNI network plugin. See `Azure CNI (advanced) networking
    #: <https://docs.microsoft.com/azure/aks/concepts-network#azure-cni-advanced-networking>`_ for
    #: more information."""
    KUBENET = "kubenet"
    """Use the Kubenet network plugin. See `Kubenet (basic) networking
    #: <https://docs.microsoft.com/azure/aks/concepts-network#kubenet-basic-networking>`_ for more
    #: information."""
    NONE = "none"
    """Do not use a network plugin. A custom CNI will need to be installed after cluster creation for
    #: networking functionality."""


class NetworkPluginMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode the network plugin should use."""

    OVERLAY = "overlay"
    """Pods are given IPs from the PodCIDR address space but use Azure Routing Domains rather than
    #: Kubenet reference plugins host-local and bridge."""


class NetworkPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network policy used for building the Kubernetes network."""

    NONE = "none"
    """Network policies will not be enforced. This is the default value when NetworkPolicy is not
    #: specified."""
    CALICO = "calico"
    """Use Calico network policies. See `differences between Azure and Calico policies
    #: <https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities>`_
    #: for more information."""
    AZURE = "azure"
    """Use Azure network policies. See `differences between Azure and Calico policies
    #: <https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities>`_
    #: for more information."""
    CILIUM = "cilium"
    """Use Cilium to enforce network policies. This requires networkDataplane to be 'cilium'."""


class NodeOSUpgradeChannel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default is Unmanaged, but may change to either NodeImage or SecurityPatch at GA."""

    NONE = "None"
    """No attempt to update your machines OS will be made either by OS or by rolling VHDs. This means
    #: you are responsible for your security updates"""
    UNMANAGED = "Unmanaged"
    """OS updates will be applied automatically through the OS built-in patching infrastructure. Newly
    #: scaled in machines will be unpatched initially, and will be patched at some later time by the
    #: OS's infrastructure. Behavior of this option depends on the OS in question. Ubuntu and Mariner
    #: apply security patches through unattended upgrade roughly once a day around 06:00 UTC. Windows
    #: does not apply security patches automatically and so for them this option is equivalent to None
    #: till further notice"""
    SECURITY_PATCH = "SecurityPatch"
    """AKS will update the nodes VHD with patches from the image maintainer labelled "security only"
    #: on a regular basis. Where possible, patches will also be applied without reimaging to existing
    #: nodes. Some patches, such as kernel patches, cannot be applied to existing nodes without
    #: disruption. For such patches, the VHD will be updated, and machines will be rolling reimaged to
    #: that VHD following maintenance windows and surge settings. This option incurs the extra cost of
    #: hosting the VHDs in your node resource group."""
    NODE_IMAGE = "NodeImage"
    """AKS will update the nodes with a newly patched VHD containing security fixes and bugfixes on a
    #: weekly cadence. With the VHD update machines will be rolling reimaged to that VHD following
    #: maintenance windows and surge settings. No extra VHD cost is incurred when choosing this option
    #: as AKS hosts the images."""


class NodeProvisioningMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Once the mode it set to Auto, it cannot be changed back to Manual."""

    MANUAL = "Manual"
    """Nodes are provisioned manually by the user"""
    AUTO = "Auto"
    """Nodes are provisioned automatically by AKS using Karpenter. Fixed size Node Pools can still be
    #: created, but autoscaling Node Pools cannot be. (See aka.ms/aks/nap for more details)."""


class OSDiskType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested
    OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more
    information see `Ephemeral OS
    <https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os>`_.
    """

    MANAGED = "Managed"
    """Azure replicates the operating system disk for a virtual machine to Azure storage to avoid data
    #: loss should the VM need to be relocated to another host. Since containers aren't designed to
    #: have local state persisted, this behavior offers limited value while providing some drawbacks,
    #: including slower node provisioning and higher read/write latency."""
    EPHEMERAL = "Ephemeral"
    """Ephemeral OS disks are stored only on the host machine, just like a temporary disk. This
    #: provides lower read/write latency, along with faster node scaling and cluster upgrades."""


class OSSKU(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the OS SKU used by the agent pool. If not specified, the default is Ubuntu if
    OSType=Linux or Windows2019 if OSType=Windows. And the default Windows OSSKU will be changed to
    Windows2022 after Windows2019 is deprecated.
    """

    UBUNTU = "Ubuntu"
    """Use Ubuntu as the OS for node images."""
    MARINER = "Mariner"
    """Deprecated OSSKU. Microsoft recommends that new deployments choose 'AzureLinux' instead."""
    AZURE_LINUX = "AzureLinux"
    """Use AzureLinux as the OS for node images. Azure Linux is a container-optimized Linux distro
    #: built by Microsoft, visit https://aka.ms/azurelinux for more information."""
    CBL_MARINER = "CBLMariner"
    """Deprecated OSSKU. Microsoft recommends that new deployments choose 'AzureLinux' instead."""
    WINDOWS2019 = "Windows2019"
    """Use Windows2019 as the OS for node images. Unsupported for system node pools. Windows2019 only
    #: supports Windows2019 containers; it cannot run Windows2022 containers and vice versa."""
    WINDOWS2022 = "Windows2022"
    """Use Windows2022 as the OS for node images. Unsupported for system node pools. Windows2022 only
    #: supports Windows2022 containers; it cannot run Windows2019 containers and vice versa."""
    WINDOWS_ANNUAL = "WindowsAnnual"
    """Use Windows Annual Channel version as the OS for node images. Unsupported for system node
    #: pools. Details about supported container images and kubernetes versions under different AKS
    #: Annual Channel versions could be seen in https://aka.ms/aks/windows-annual-channel-details."""


class OSType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operating system type. The default is Linux."""

    LINUX = "Linux"
    """Use Linux."""
    WINDOWS = "Windows"
    """Use Windows."""


class OutboundType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This can only be set at cluster creation time and cannot be changed later. For more information
    see `egress outbound type <https://docs.microsoft.com/azure/aks/egress-outboundtype>`_.
    """

    LOAD_BALANCER = "loadBalancer"
    """The load balancer is used for egress through an AKS assigned public IP. This supports
    #: Kubernetes services of type 'loadBalancer'. For more information see `outbound type
    #: loadbalancer
    #: <https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-loadbalancer>`_."""
    USER_DEFINED_ROUTING = "userDefinedRouting"
    """Egress paths must be defined by the user. This is an advanced scenario and requires proper
    #: network configuration. For more information see `outbound type userDefinedRouting
    #: <https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-userdefinedrouting>`_."""
    MANAGED_NAT_GATEWAY = "managedNATGateway"
    """The AKS-managed NAT gateway is used for egress."""
    USER_ASSIGNED_NAT_GATEWAY = "userAssignedNATGateway"
    """The user-assigned NAT gateway associated to the cluster subnet is used for egress. This is an
    #: advanced scenario and requires proper network configuration."""


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"


class Protocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The network protocol of the port."""

    TCP = "TCP"
    """TCP protocol."""
    UDP = "UDP"
    """UDP protocol."""


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allow or deny public network access for AKS."""

    ENABLED = "Enabled"
    """Inbound/Outbound to the managedCluster is allowed."""
    DISABLED = "Disabled"
    """Inbound traffic to managedCluster is disabled, traffic from managedCluster is allowed."""
    SECURED_BY_PERIMETER = "SecuredByPerimeter"
    """Inbound/Outbound traffic is managed by Microsoft.Network/NetworkSecurityPerimeters."""


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """For more information see `use managed identities in AKS
    <https://docs.microsoft.com/azure/aks/use-managed-identity>`_.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    """Use an implicitly created system assigned managed identity to manage cluster resources. Master
    #: components in the control plane such as kube-controller-manager will use the system assigned
    #: managed identity to manipulate Azure resources."""
    USER_ASSIGNED = "UserAssigned"
    """Use a user-specified identity to manage cluster resources. Master components in the control
    #: plane such as kube-controller-manager will use the specified user assigned managed identity to
    #: manipulate Azure resources."""
    NONE = "None"
    """Do not use a managed identity for the Managed Cluster, service principal will be used instead."""


class RestrictionLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The restriction level applied to the cluster's node resource group."""

    UNRESTRICTED = "Unrestricted"
    """All RBAC permissions are allowed on the managed node resource group"""
    READ_ONLY = "ReadOnly"
    """Only */read RBAC permissions allowed on the managed node resource group"""


class ScaleDownMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes how VMs are added to or removed from Agent Pools. See `billing states
    <https://docs.microsoft.com/azure/virtual-machines/states-billing>`_.
    """

    DELETE = "Delete"
    """Create new instances during scale up and remove instances during scale down."""
    DEALLOCATE = "Deallocate"
    """Attempt to start deallocated instances (if they exist) during scale up and deallocate instances
    #: during scale down."""


class ScaleSetEvictionPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The eviction policy specifies what to do with the VM when it is evicted. The default is Delete.
    For more information about eviction see `spot VMs
    <https://docs.microsoft.com/azure/virtual-machines/spot-vms>`_.
    """

    DELETE = "Delete"
    """Nodes in the underlying Scale Set of the node pool are deleted when they're evicted."""
    DEALLOCATE = "Deallocate"
    """Nodes in the underlying Scale Set of the node pool are set to the stopped-deallocated state
    #: upon eviction. Nodes in the stopped-deallocated state count against your compute quota and can
    #: cause issues with cluster scaling or upgrading."""


class ScaleSetPriority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Virtual Machine Scale Set priority."""

    SPOT = "Spot"
    """Spot priority VMs will be used. There is no SLA for spot nodes. See `spot on AKS
    #: <https://docs.microsoft.com/azure/aks/spot-node-pool>`_ for more information."""
    REGULAR = "Regular"
    """Regular VMs will be used."""


class ServiceMeshMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Mode of the service mesh."""

    ISTIO = "Istio"
    """Istio deployed as an AKS addon."""
    DISABLED = "Disabled"
    """Mesh is disabled."""


class SnapshotType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of a snapshot. The default is NodePool."""

    NODE_POOL = "NodePool"
    """The snapshot is a snapshot of a node pool."""
    MANAGED_CLUSTER = "ManagedCluster"
    """The snapshot is a snapshot of a managed cluster."""


class TrustedAccessRoleBindingProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state of trusted access role binding."""

    CANCELED = "Canceled"
    DELETING = "Deleting"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies on which instance of the allowed days specified in daysOfWeek the maintenance occurs."""

    FIRST = "First"
    """First."""
    SECOND = "Second"
    """Second."""
    THIRD = "Third"
    """Third."""
    FOURTH = "Fourth"
    """Fourth."""
    LAST = "Last"
    """Last."""


class UpgradeChannel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """For more information see `setting the AKS cluster auto-upgrade channel
    <https://docs.microsoft.com/azure/aks/upgrade-cluster#set-auto-upgrade-channel>`_.
    """

    RAPID = "rapid"
    """Automatically upgrade the cluster to the latest supported patch release on the latest supported
    #: minor version. In cases where the cluster is at a version of Kubernetes that is at an N-2 minor
    #: version where N is the latest supported minor version, the cluster first upgrades to the latest
    #: supported patch version on N-1 minor version. For example, if a cluster is running version
    #: 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster first is
    #: upgraded to 1.18.6, then is upgraded to 1.19.1."""
    STABLE = "stable"
    """Automatically upgrade the cluster to the latest supported patch release on minor version N-1,
    #: where N is the latest supported minor version. For example, if a cluster is running version
    #: 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is upgraded
    #: to 1.18.6."""
    PATCH = "patch"
    """Automatically upgrade the cluster to the latest supported patch version when it becomes
    #: available while keeping the minor version the same. For example, if a cluster is running
    #: version 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is
    #: upgraded to 1.17.9."""
    NODE_IMAGE = "node-image"
    """Automatically upgrade the node image to the latest version available. Consider using
    #: nodeOSUpgradeChannel instead as that allows you to configure node OS patching separate from
    #: Kubernetes version patching"""
    NONE = "none"
    """Disables auto-upgrades and keeps the cluster at its current version of Kubernetes."""


class WeekDay(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The weekday enum."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class WorkloadRuntime(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the type of workload a node can run."""

    OCI_CONTAINER = "OCIContainer"
    """Nodes will use Kubelet to run standard OCI container workloads."""
    WASM_WASI = "WasmWasi"
    """Nodes will use Krustlet to run WASM workloads using the WASI provider (Preview)."""
    KATA_MSHV_VM_ISOLATION = "KataMshvVmIsolation"
    """Nodes can use (Kata + Cloud Hypervisor + Hyper-V) to enable Nested VM-based pods (Preview). Due
    #: to the use Hyper-V, AKS node OS itself is a nested VM (the root OS) of Hyper-V. Thus it can
    #: only be used with VM series that support Nested Virtualization such as Dv3 series."""
