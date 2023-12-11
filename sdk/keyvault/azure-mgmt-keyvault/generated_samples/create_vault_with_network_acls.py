# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-keyvault
# USAGE
    python create_vault_with_network_acls.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = KeyVaultManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.vaults.begin_create_or_update(
        resource_group_name="sample-resource-group",
        vault_name="sample-vault",
        parameters={
            "location": "westus",
            "properties": {
                "enabledForDeployment": True,
                "enabledForDiskEncryption": True,
                "enabledForTemplateDeployment": True,
                "networkAcls": {
                    "bypass": "AzureServices",
                    "defaultAction": "Deny",
                    "ipRules": [{"value": "124.56.78.91"}, {"value": "'10.91.4.0/24'"}],
                    "virtualNetworkRules": [
                        {
                            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/subnet1"
                        }
                    ],
                },
                "sku": {"family": "A", "name": "standard"},
                "tenantId": "00000000-0000-0000-0000-000000000000",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/keyvault/resource-manager/Microsoft.KeyVault/stable/2023-07-01/examples/createVaultWithNetworkAcls.json
if __name__ == "__main__":
    main()
