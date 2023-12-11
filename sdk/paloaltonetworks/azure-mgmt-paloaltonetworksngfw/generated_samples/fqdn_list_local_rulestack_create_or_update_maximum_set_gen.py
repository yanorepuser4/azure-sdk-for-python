# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.paloaltonetworksngfw import PaloAltoNetworksNgfwMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-paloaltonetworksngfw
# USAGE
    python fqdn_list_local_rulestack_create_or_update_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PaloAltoNetworksNgfwMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="2bf4a339-294d-4c25-b0b2-ef649e9f5c27",
    )

    response = client.fqdn_list_local_rulestack.begin_create_or_update(
        resource_group_name="rgopenapi",
        local_rulestack_name="lrs1",
        name="armid1",
        resource={
            "properties": {
                "auditComment": "string",
                "description": "string",
                "etag": "aaaaaaaaaaaaaaaaaa",
                "fqdnList": ["string1", "string2"],
                "provisioningState": "Accepted",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/stable/2023-09-01/examples/FqdnListLocalRulestack_CreateOrUpdate_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
