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
    python local_rulestacks_create_or_update_maximum_set_gen.py

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

    response = client.local_rulestacks.begin_create_or_update(
        resource_group_name="rgopenapi",
        local_rulestack_name="lrs1",
        resource={
            "identity": {
                "type": "None",
                "userAssignedIdentities": {"key16": {"clientId": "aaaa", "principalId": "aaaaaaaaaaaaaaa"}},
            },
            "location": "eastus",
            "properties": {
                "associatedSubscriptions": ["2bf4a339-294d-4c25-b0b2-ef649e9f5c27"],
                "defaultMode": "IPS",
                "description": "local rulestacks",
                "minAppIdVersion": "8.5.3",
                "panEtag": "2bf4a339-294d-4c25-b0b2-ef649e9f5c12",
                "panLocation": "eastus",
                "provisioningState": "Accepted",
                "scope": "LOCAL",
                "securityServices": {
                    "antiSpywareProfile": "default",
                    "antiVirusProfile": "default",
                    "dnsSubscription": "default",
                    "fileBlockingProfile": "default",
                    "outboundTrustCertificate": "default",
                    "outboundUnTrustCertificate": "default",
                    "urlFilteringProfile": "default",
                    "vulnerabilityProfile": "default",
                },
            },
            "tags": {"tagName": "value"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/stable/2023-09-01/examples/LocalRulestacks_CreateOrUpdate_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
