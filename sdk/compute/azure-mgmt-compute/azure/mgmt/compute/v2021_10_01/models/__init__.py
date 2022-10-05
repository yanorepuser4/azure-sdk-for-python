# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import CommunityGalleryInfo
from ._models_py3 import DataDiskImageEncryption
from ._models_py3 import Disallowed
from ._models_py3 import DiskImageEncryption
from ._models_py3 import EncryptionImages
from ._models_py3 import Gallery
from ._models_py3 import GalleryApplication
from ._models_py3 import GalleryApplicationList
from ._models_py3 import GalleryApplicationUpdate
from ._models_py3 import GalleryApplicationVersion
from ._models_py3 import GalleryApplicationVersionList
from ._models_py3 import GalleryApplicationVersionPublishingProfile
from ._models_py3 import GalleryApplicationVersionUpdate
from ._models_py3 import GalleryArtifactPublishingProfileBase
from ._models_py3 import GalleryArtifactSource
from ._models_py3 import GalleryArtifactVersionSource
from ._models_py3 import GalleryDataDiskImage
from ._models_py3 import GalleryDiskImage
from ._models_py3 import GalleryExtendedLocation
from ._models_py3 import GalleryIdentifier
from ._models_py3 import GalleryImage
from ._models_py3 import GalleryImageFeature
from ._models_py3 import GalleryImageIdentifier
from ._models_py3 import GalleryImageList
from ._models_py3 import GalleryImageUpdate
from ._models_py3 import GalleryImageVersion
from ._models_py3 import GalleryImageVersionList
from ._models_py3 import GalleryImageVersionPublishingProfile
from ._models_py3 import GalleryImageVersionStorageProfile
from ._models_py3 import GalleryImageVersionUpdate
from ._models_py3 import GalleryList
from ._models_py3 import GalleryOSDiskImage
from ._models_py3 import GalleryTargetExtendedLocation
from ._models_py3 import GalleryUpdate
from ._models_py3 import ImagePurchasePlan
from ._models_py3 import InnerError
from ._models_py3 import ManagedArtifact
from ._models_py3 import OSDiskImageEncryption
from ._models_py3 import OSDiskImageSecurityProfile
from ._models_py3 import RecommendedMachineConfiguration
from ._models_py3 import RegionalReplicationStatus
from ._models_py3 import RegionalSharingStatus
from ._models_py3 import ReplicationStatus
from ._models_py3 import Resource
from ._models_py3 import ResourceRange
from ._models_py3 import SharingProfile
from ._models_py3 import SharingProfileGroup
from ._models_py3 import SharingStatus
from ._models_py3 import SharingUpdate
from ._models_py3 import SoftDeletePolicy
from ._models_py3 import TargetRegion
from ._models_py3 import UpdateResourceDefinition
from ._models_py3 import UserArtifactManage
from ._models_py3 import UserArtifactSource

from ._compute_management_client_enums import AggregatedReplicationState
from ._compute_management_client_enums import Architecture
from ._compute_management_client_enums import ConfidentialVMEncryptionType
from ._compute_management_client_enums import GalleryApplicationVersionPropertiesProvisioningState
from ._compute_management_client_enums import GalleryExpandParams
from ._compute_management_client_enums import GalleryExtendedLocationType
from ._compute_management_client_enums import GalleryImagePropertiesProvisioningState
from ._compute_management_client_enums import GalleryImageVersionPropertiesProvisioningState
from ._compute_management_client_enums import GalleryPropertiesProvisioningState
from ._compute_management_client_enums import GallerySharingPermissionTypes
from ._compute_management_client_enums import HostCaching
from ._compute_management_client_enums import HyperVGeneration
from ._compute_management_client_enums import OperatingSystemStateTypes
from ._compute_management_client_enums import OperatingSystemTypes
from ._compute_management_client_enums import ReplicationMode
from ._compute_management_client_enums import ReplicationState
from ._compute_management_client_enums import ReplicationStatusTypes
from ._compute_management_client_enums import SelectPermissions
from ._compute_management_client_enums import SharingProfileGroupTypes
from ._compute_management_client_enums import SharingState
from ._compute_management_client_enums import SharingUpdateOperationTypes
from ._compute_management_client_enums import StorageAccountType
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApiError",
    "ApiErrorBase",
    "CommunityGalleryInfo",
    "DataDiskImageEncryption",
    "Disallowed",
    "DiskImageEncryption",
    "EncryptionImages",
    "Gallery",
    "GalleryApplication",
    "GalleryApplicationList",
    "GalleryApplicationUpdate",
    "GalleryApplicationVersion",
    "GalleryApplicationVersionList",
    "GalleryApplicationVersionPublishingProfile",
    "GalleryApplicationVersionUpdate",
    "GalleryArtifactPublishingProfileBase",
    "GalleryArtifactSource",
    "GalleryArtifactVersionSource",
    "GalleryDataDiskImage",
    "GalleryDiskImage",
    "GalleryExtendedLocation",
    "GalleryIdentifier",
    "GalleryImage",
    "GalleryImageFeature",
    "GalleryImageIdentifier",
    "GalleryImageList",
    "GalleryImageUpdate",
    "GalleryImageVersion",
    "GalleryImageVersionList",
    "GalleryImageVersionPublishingProfile",
    "GalleryImageVersionStorageProfile",
    "GalleryImageVersionUpdate",
    "GalleryList",
    "GalleryOSDiskImage",
    "GalleryTargetExtendedLocation",
    "GalleryUpdate",
    "ImagePurchasePlan",
    "InnerError",
    "ManagedArtifact",
    "OSDiskImageEncryption",
    "OSDiskImageSecurityProfile",
    "RecommendedMachineConfiguration",
    "RegionalReplicationStatus",
    "RegionalSharingStatus",
    "ReplicationStatus",
    "Resource",
    "ResourceRange",
    "SharingProfile",
    "SharingProfileGroup",
    "SharingStatus",
    "SharingUpdate",
    "SoftDeletePolicy",
    "TargetRegion",
    "UpdateResourceDefinition",
    "UserArtifactManage",
    "UserArtifactSource",
    "AggregatedReplicationState",
    "Architecture",
    "ConfidentialVMEncryptionType",
    "GalleryApplicationVersionPropertiesProvisioningState",
    "GalleryExpandParams",
    "GalleryExtendedLocationType",
    "GalleryImagePropertiesProvisioningState",
    "GalleryImageVersionPropertiesProvisioningState",
    "GalleryPropertiesProvisioningState",
    "GallerySharingPermissionTypes",
    "HostCaching",
    "HyperVGeneration",
    "OperatingSystemStateTypes",
    "OperatingSystemTypes",
    "ReplicationMode",
    "ReplicationState",
    "ReplicationStatusTypes",
    "SelectPermissions",
    "SharingProfileGroupTypes",
    "SharingState",
    "SharingUpdateOperationTypes",
    "StorageAccountType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
