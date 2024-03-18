# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.search import SearchManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-search
# USAGE
    python search_create_or_update_service_with_data_exfiltration.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SearchManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.services.begin_create_or_update(
        resource_group_name="rg1",
        search_service_name="mysearchservice",
        service={
            "location": "westus",
            "properties": {
                "disabledDataExfiltrationOptions": ["All"],
                "hostingMode": "default",
                "partitionCount": 1,
                "replicaCount": 3,
            },
            "sku": {"name": "standard"},
            "tags": {"app-name": "My e-commerce app"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/search/resource-manager/Microsoft.Search/preview/2024-03-01-preview/examples/SearchCreateOrUpdateServiceWithDataExfiltration.json
if __name__ == "__main__":
    main()
