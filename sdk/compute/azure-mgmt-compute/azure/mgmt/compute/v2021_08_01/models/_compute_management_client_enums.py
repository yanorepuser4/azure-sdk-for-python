# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessLevel."""

    NONE = "None"
    READ = "Read"
    WRITE = "Write"


class DiskCreateOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This enumerates the possible sources of a disk's creation."""

    EMPTY = "Empty"
    """Create an empty data disk of a size given by diskSizeGB."""
    ATTACH = "Attach"
    """Disk will be attached to a VM."""
    FROM_IMAGE = "FromImage"
    """Create a new disk from a platform image specified by the given imageReference or
    #: galleryImageReference."""
    IMPORT = "Import"
    """Create a disk by importing from a blob specified by a sourceUri in a storage account specified
    #: by storageAccountId."""
    COPY = "Copy"
    """Create a new disk or snapshot by copying from a disk or snapshot specified by the given
    #: sourceResourceId."""
    RESTORE = "Restore"
    """Create a new disk by copying from a backup recovery point."""
    UPLOAD = "Upload"
    """Create a new disk by obtaining a write token and using it to directly upload the contents of
    #: the disk."""
    COPY_START = "CopyStart"
    """Create a new disk by using a deep copy process, where the resource creation is considered
    #: complete only after all data has been copied from the source."""
    IMPORT_SECURE = "ImportSecure"
    """Similar to Import create option. Create a new Trusted Launch VM or Confidential VM supported
    #: disk by importing additional blob for VM guest state specified by securityDataUri in storage
    #: account specified by storageAccountId"""
    UPLOAD_PREPARED_SECURE = "UploadPreparedSecure"
    """Similar to Upload create option. Create a new Trusted Launch VM or Confidential VM supported
    #: disk and upload using write token in both disk and VM guest state"""


class DiskEncryptionSetIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported
    for new creations. Disk Encryption Sets can be updated with Identity type None during migration
    of subscription to a new Azure Active Directory tenant; it will cause the encrypted resources
    to lose access to the keys.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"


class DiskEncryptionSetType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of key used to encrypt the data of the disk."""

    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    """Resource using diskEncryptionSet would be encrypted at rest with Customer managed key that can
    #: be changed and revoked by a customer."""
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"
    """Resource using diskEncryptionSet would be encrypted at rest with two layers of encryption. One
    #: of the keys is Customer managed and the other key is Platform managed."""
    CONFIDENTIAL_VM_ENCRYPTED_WITH_CUSTOMER_KEY = "ConfidentialVmEncryptedWithCustomerKey"
    """Confidential VM supported disk and VM guest state would be encrypted with customer managed key."""


class DiskSecurityTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the SecurityType of the VM. Applicable for OS disks only."""

    TRUSTED_LAUNCH = "TrustedLaunch"
    """Trusted Launch provides security features such as secure boot and virtual Trusted Platform
    #: Module (vTPM)"""
    CONFIDENTIAL_VM_VMGUEST_STATE_ONLY_ENCRYPTED_WITH_PLATFORM_KEY = (
        "ConfidentialVM_VMGuestStateOnlyEncryptedWithPlatformKey"
    )
    """Indicates Confidential VM disk with only VM guest state encrypted"""
    CONFIDENTIAL_VM_DISK_ENCRYPTED_WITH_PLATFORM_KEY = "ConfidentialVM_DiskEncryptedWithPlatformKey"
    """Indicates Confidential VM disk with both OS disk and VM guest state encrypted with a platform
    #: managed key"""
    CONFIDENTIAL_VM_DISK_ENCRYPTED_WITH_CUSTOMER_KEY = "ConfidentialVM_DiskEncryptedWithCustomerKey"
    """Indicates Confidential VM disk with both OS disk and VM guest state encrypted with a customer
    #: managed key"""


class DiskState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This enumerates the possible state of the disk."""

    UNATTACHED = "Unattached"
    """The disk is not being used and can be attached to a VM."""
    ATTACHED = "Attached"
    """The disk is currently attached to a running VM."""
    RESERVED = "Reserved"
    """The disk is attached to a stopped-deallocated VM."""
    FROZEN = "Frozen"
    """The disk is attached to a VM which is in hibernated state."""
    ACTIVE_SAS = "ActiveSAS"
    """The disk currently has an Active SAS Uri associated with it."""
    ACTIVE_SAS_FROZEN = "ActiveSASFrozen"
    """The disk is attached to a VM in hibernated state and has an active SAS URI associated with it."""
    READY_TO_UPLOAD = "ReadyToUpload"
    """A disk is ready to be created by upload by requesting a write token."""
    ACTIVE_UPLOAD = "ActiveUpload"
    """A disk is created for upload and a write token has been issued for uploading to it."""


class DiskStorageAccountTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The sku name."""

    STANDARD_LRS = "Standard_LRS"
    """Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access."""
    PREMIUM_LRS = "Premium_LRS"
    """Premium SSD locally redundant storage. Best for production and performance sensitive workloads."""
    STANDARD_SSD_LRS = "StandardSSD_LRS"
    """Standard SSD locally redundant storage. Best for web servers, lightly used enterprise
    #: applications and dev/test."""
    ULTRA_SSD_LRS = "UltraSSD_LRS"
    """Ultra SSD locally redundant storage. Best for IO-intensive workloads such as SAP HANA, top tier
    #: databases (for example, SQL, Oracle), and other transaction-heavy workloads."""
    PREMIUM_ZRS = "Premium_ZRS"
    """Premium SSD zone redundant storage. Best for the production workloads that need storage
    #: resiliency against zone failures."""
    STANDARD_SSD_ZRS = "StandardSSD_ZRS"
    """Standard SSD zone redundant storage. Best for web servers, lightly used enterprise applications
    #: and dev/test that need storage resiliency against zone failures."""


class EncryptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of key used to encrypt the data of the disk."""

    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    """Disk is encrypted at rest with Platform managed key. It is the default encryption type. This is
    #: not a valid encryption type for disk encryption sets."""
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    """Disk is encrypted at rest with Customer managed key that can be changed and revoked by a
    #: customer."""
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"
    """Disk is encrypted at rest with 2 layers of encryption. One of the keys is Customer managed and
    #: the other key is Platform managed."""


class ExtendedLocationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of extendedLocation."""

    EDGE_ZONE = "EdgeZone"


class HyperVGeneration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The hypervisor generation of the Virtual Machine. Applicable to OS disks only."""

    V1 = "V1"
    V2 = "V2"


class NetworkAccessPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Policy for accessing the disk via network."""

    ALLOW_ALL = "AllowAll"
    """The disk can be exported or uploaded to from any network."""
    ALLOW_PRIVATE = "AllowPrivate"
    """The disk can be exported or uploaded to using a DiskAccess resource's private endpoints."""
    DENY_ALL = "DenyAll"
    """The disk cannot be exported."""


class OperatingSystemTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Operating System type."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PrivateEndpointServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private endpoint connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Policy for controlling export on the disk."""

    ENABLED = "Enabled"
    """You can generate a SAS URI to access the underlying data of the disk publicly on the internet
    #: when NetworkAccessPolicy is set to AllowAll. You can access the data via the SAS URI only from
    #: your trusted Azure VNET when NetworkAccessPolicy is set to AllowPrivate."""
    DISABLED = "Disabled"
    """You cannot access the underlying data of the disk publicly on the internet even when
    #: NetworkAccessPolicy is set to AllowAll. You can access the data via the SAS URI only from your
    #: trusted Azure VNET when NetworkAccessPolicy is set to AllowPrivate."""


class SnapshotStorageAccountTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The sku name."""

    STANDARD_LRS = "Standard_LRS"
    """Standard HDD locally redundant storage"""
    PREMIUM_LRS = "Premium_LRS"
    """Premium SSD locally redundant storage"""
    STANDARD_ZRS = "Standard_ZRS"
    """Standard zone redundant storage"""
