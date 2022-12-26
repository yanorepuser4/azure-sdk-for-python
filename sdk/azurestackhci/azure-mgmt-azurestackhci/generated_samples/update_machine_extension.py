# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.azurestackhci import AzureStackHCIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-azurestackhci
# USAGE
    python update_machine_extension.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureStackHCIClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscriptionId}",
    )

    response = client.machine_extensions.begin_update(
        resource_group_name="myResourceGroup",
        name="myMachine",
        extension_name="CustomScriptExtension",
        extension_parameters={
            "properties": {
                "publisher": "Microsoft.Compute",
                "settings": {"commandToExecute": 'powershell.exe -c "Get-Process | Where-Object { $_.CPU -lt 100 }"'},
                "type": "CustomScriptExtension",
                "typeHandlerVersion": "1.10",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/preview/2021-09-01-preview/examples/UpdateMachineExtension.json
if __name__ == "__main__":
    main()
