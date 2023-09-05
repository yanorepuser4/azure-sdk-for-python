# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.3)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import AcrAccessToken
from ._models import AcrErrorInfo
from ._models import AcrErrors
from ._models import AcrRefreshToken
from ._models import Annotations
from ._models import ArtifactManifestPlatform
from ._models import ArtifactManifestProperties
from ._models import ArtifactTagProperties
from ._models import ContainerRepositoryProperties
from ._models import DeleteRepositoryResult
from ._models import Descriptor
from ._models import FsLayer
from ._models import History
from ._models import ImageSignature
from ._models import JWK
from ._models import JWKHeader
from ._models import Manifest
from ._models import ManifestAttributesBase
from ._models import ManifestAttributesManifest
from ._models import ManifestList
from ._models import ManifestListAttributes
from ._models import ManifestWrapper
from ._models import ManifestWriteableProperties
from ._models import OCIIndex
from ._models import OCIManifest
from ._models import Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema
from ._models import PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema
from ._models import Platform
from ._models import RepositoryTags
from ._models import RepositoryWriteableProperties
from ._models import TagAttributesBase
from ._models import TagAttributesTag
from ._models import TagWriteableProperties
from ._models import V1Manifest
from ._models import V2Manifest

from ._enums import ArtifactArchitecture
from ._enums import ArtifactManifestOrder
from ._enums import ArtifactOperatingSystem
from ._enums import ArtifactTagOrder
from ._enums import PostContentSchemaGrantType
from ._enums import TokenGrantType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AcrAccessToken",
    "AcrErrorInfo",
    "AcrErrors",
    "AcrRefreshToken",
    "Annotations",
    "ArtifactManifestPlatform",
    "ArtifactManifestProperties",
    "ArtifactTagProperties",
    "ContainerRepositoryProperties",
    "DeleteRepositoryResult",
    "Descriptor",
    "FsLayer",
    "History",
    "ImageSignature",
    "JWK",
    "JWKHeader",
    "Manifest",
    "ManifestAttributesBase",
    "ManifestAttributesManifest",
    "ManifestList",
    "ManifestListAttributes",
    "ManifestWrapper",
    "ManifestWriteableProperties",
    "OCIIndex",
    "OCIManifest",
    "Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema",
    "PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema",
    "Platform",
    "RepositoryTags",
    "RepositoryWriteableProperties",
    "TagAttributesBase",
    "TagAttributesTag",
    "TagWriteableProperties",
    "V1Manifest",
    "V2Manifest",
    "ArtifactArchitecture",
    "ArtifactManifestOrder",
    "ArtifactOperatingSystem",
    "ArtifactTagOrder",
    "PostContentSchemaGrantType",
    "TokenGrantType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
