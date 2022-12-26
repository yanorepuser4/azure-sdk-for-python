# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.eventgrid import EventGridManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-eventgrid
# USAGE
    python system_topic_event_subscriptions_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = EventGridManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="5b4b650e-28b9-4790-b3ab-ddbd88d727c4",
    )

    response = client.system_topic_event_subscriptions.begin_update(
        resource_group_name="examplerg",
        system_topic_name="exampleSystemTopic1",
        event_subscription_name="exampleEventSubscriptionName1",
        event_subscription_update_parameters={
            "destination": {"endpointType": "WebHook", "properties": {"endpointUrl": "https://requestb.in/15ksip71"}},
            "filter": {
                "isSubjectCaseSensitive": True,
                "subjectBeginsWith": "existingPrefix",
                "subjectEndsWith": "newSuffix",
            },
            "labels": ["label1", "label2"],
        },
    ).result()
    print(response)


# x-ms-original-file: specification/eventgrid/resource-manager/Microsoft.EventGrid/stable/2022-06-15/examples/SystemTopicEventSubscriptions_Update.json
if __name__ == "__main__":
    main()
