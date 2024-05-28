# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python nat_rule_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.nat_rules.begin_create_or_update(
        resource_group_name="rg1",
        gateway_name="gateway1",
        nat_rule_name="natRule1",
        nat_rule_parameters={
            "properties": {
                "externalMappings": [{"addressSpace": "192.168.21.0/24"}],
                "internalMappings": [{"addressSpace": "10.4.0.0/24"}],
                "ipConfigurationId": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworkGateways/cloudnet1-VNG/ipConfigurations/default",
                "mode": "EgressSnat",
                "type": "Static",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-11-01/examples/NatRulePut.json
if __name__ == "__main__":
    main()
