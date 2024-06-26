# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import Any, List, Optional

from ._client import CryptographyClient


__all__ = [
    "CryptographyClient",
]


def __dir__() -> List[str]:
    return __all__


# Allow importing these types for backwards compatibility, but exclude indexing types that shouldn't be in aio namespace


def __getattr__(name: str):
    requested: Optional[Any] = None
    if name == "EncryptionAlgorithm":
        from .. import EncryptionAlgorithm

        requested = EncryptionAlgorithm
    if name == "KeyWrapAlgorithm":
        from .. import KeyWrapAlgorithm

        requested = KeyWrapAlgorithm
    if name == "SignatureAlgorithm":
        from .. import SignatureAlgorithm

        requested = SignatureAlgorithm
    if name == "EncryptResult":
        from .. import EncryptResult

        requested = EncryptResult
    if name == "SignResult":
        from .. import SignResult

        requested = SignResult
    if name == "WrapResult":
        from .. import WrapResult

        requested = WrapResult
    if requested:
        return requested
    raise AttributeError(f"module 'azure.keyvault.keys.crypto.aio' has no attribute {name}")
