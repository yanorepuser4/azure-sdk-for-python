# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._patch import FaceClient
from ._patch import FaceSessionClient


from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "FaceClient",
    "FaceSessionClient",
]


_patch_sdk()
