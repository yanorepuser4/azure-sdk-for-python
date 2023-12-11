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
    python search_create_query_key.py

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

    response = client.query_keys.create(
        resource_group_name="rg1",
        search_service_name="mysearchservice",
        name="Query key for browser-based clients",
    )
    print(response)


# x-ms-original-file: specification/search/resource-manager/Microsoft.Search/stable/2023-11-01/examples/SearchCreateQueryKey.json
if __name__ == "__main__":
    main()
