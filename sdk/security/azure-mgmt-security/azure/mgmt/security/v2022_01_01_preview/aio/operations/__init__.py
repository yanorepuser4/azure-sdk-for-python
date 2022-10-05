# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._governance_rule_operations import GovernanceRuleOperations
from ._governance_rules_operations import GovernanceRulesOperations
from ._security_connector_governance_rule_operations import SecurityConnectorGovernanceRuleOperations
from ._security_connector_governance_rules_operations import SecurityConnectorGovernanceRulesOperations
from ._subscription_governance_rules_execute_status_operations import SubscriptionGovernanceRulesExecuteStatusOperations
from ._security_connector_governance_rules_execute_status_operations import (
    SecurityConnectorGovernanceRulesExecuteStatusOperations,
)
from ._governance_assignments_operations import GovernanceAssignmentsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "GovernanceRuleOperations",
    "GovernanceRulesOperations",
    "SecurityConnectorGovernanceRuleOperations",
    "SecurityConnectorGovernanceRulesOperations",
    "SubscriptionGovernanceRulesExecuteStatusOperations",
    "SecurityConnectorGovernanceRulesExecuteStatusOperations",
    "GovernanceAssignmentsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
