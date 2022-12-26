# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.botservice import AzureBotService

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-botservice
# USAGE
    python list_channels_by_bot_service.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureBotService(
        credential=DefaultAzureCredential(),
        subscription_id="subscription-id",
    )

    response = client.channels.list_by_resource_group(
        resource_group_name="OneResourceGroupName",
        resource_name="samplebotname",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/botservice/resource-manager/Microsoft.BotService/preview/2022-06-15-preview/examples/ListChannelsByBotService.json
if __name__ == "__main__":
    main()
